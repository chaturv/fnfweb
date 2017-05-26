from __future__ import unicode_literals

from django.db import models

CCY_MAX_DIGITS = 10
CCY_DECIMAL_PLACES = 2

MEASURE_MAX_DIGITS = 10
MEASURE_DECIMAL_PLACES = 2

SHORT_STR_MAX_LENGTH = 50
LONG_STR_MAX_LENGTH = 255
VERY_LONG_STR_MAX_LENGTH = 2048


# 1. Auto-incrementing primary key fields are automatically added to each model
# 2. Override db table name using class Meta. Other options available too


# list of measurement units
class MeasurementUnit(models.Model):
    name = models.CharField(max_length=SHORT_STR_MAX_LENGTH, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'measurement_unit'
        verbose_name = 'Measurement Unit'
        verbose_name_plural = 'Measurement Units'


# lifecycle status of an order
class OrderStatus(models.Model):
    name = models.CharField(max_length=SHORT_STR_MAX_LENGTH, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'order_status'
        verbose_name = 'Order Status'
        verbose_name_plural = 'Order Statuses'
        ordering = ['name']


# lifecycle status of a delivery
class DeliveryStatus(models.Model):
    # delivery statuses
    ASSIGNED = 'ASSIGNED'
    DELIVERED = 'DELIVERED'

    name = models.CharField(max_length=SHORT_STR_MAX_LENGTH, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'delivery_status'
        verbose_name = 'Delivery Status'
        verbose_name_plural = 'Delivery Statuses'
        ordering = ['name']


# Delivery partners
class DeliveryPartner(models.Model):
    govt_issued_id = models.CharField(max_length=SHORT_STR_MAX_LENGTH, unique=True)
    name = models.CharField(max_length=LONG_STR_MAX_LENGTH)
    billing_rate = models.DecimalField(max_digits=CCY_MAX_DIGITS, decimal_places=CCY_DECIMAL_PLACES)
    billing_unit = models.ForeignKey(MeasurementUnit, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'delivery_partner'
        verbose_name = 'Delivery Partner'
        verbose_name_plural = 'Delivery Partners'
        ordering = ['name']


# information about the delivery
class DeliveryInfo(models.Model):
    partner = models.ForeignKey(DeliveryPartner, on_delete=models.DO_NOTHING)
    delivery_date = models.DateField()
    actual_delivery_date = models.DateTimeField(blank=True, null=True)
    charge = models.DecimalField(max_digits=CCY_MAX_DIGITS, decimal_places=CCY_DECIMAL_PLACES)
    status = models.ForeignKey(DeliveryStatus, on_delete=models.DO_NOTHING)
    address_line_1 = models.CharField(max_length=LONG_STR_MAX_LENGTH)
    address_line_2 = models.CharField(max_length=LONG_STR_MAX_LENGTH, blank=True)
    unit_number = models.CharField(max_length=SHORT_STR_MAX_LENGTH)
    pin_code = models.IntegerField()

    def __str__(self):
        return self.partner.__str__()  # TODO:

    class Meta:
        db_table = 'delivery_info'
        verbose_name = 'Delivery Info'
        verbose_name_plural = 'Delivery Info'


# procurement sources
class IngredientSource(models.Model):
    name = models.CharField(max_length=LONG_STR_MAX_LENGTH, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'ingredient_source'
        verbose_name = 'Ingredient Source'
        verbose_name_plural = 'Ingredient Sources'
        ordering = ['name']


# ingredient categories
class IngredientCategory(models.Model):
    name = models.CharField(max_length=LONG_STR_MAX_LENGTH, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'ingredient_category'
        verbose_name = 'Ingredient Category'
        verbose_name_plural = 'Ingredient Categories'
        ordering = ['name']


# An ingredient
class Ingredient(models.Model):
    name = models.CharField(max_length=LONG_STR_MAX_LENGTH, unique=True)
    category = models.ForeignKey(IngredientCategory, on_delete=models.DO_NOTHING)
    source = models.ForeignKey(IngredientSource, on_delete=models.DO_NOTHING)
    brand_name = models.CharField(max_length=SHORT_STR_MAX_LENGTH, blank=True, null=True)
    cost_price = models.DecimalField(max_digits=CCY_MAX_DIGITS, decimal_places=CCY_DECIMAL_PLACES)
    unit = models.ForeignKey(MeasurementUnit, on_delete=models.DO_NOTHING)
    measure = models.DecimalField(max_digits=MEASURE_MAX_DIGITS, decimal_places=MEASURE_DECIMAL_PLACES)
    notes = models.CharField(max_length=VERY_LONG_STR_MAX_LENGTH, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'ingredient'
        verbose_name = 'Ingredient'
        verbose_name_plural = 'Ingredients'
        ordering = ['name']


# A dish
class Dish(models.Model):
    name = models.CharField(max_length=LONG_STR_MAX_LENGTH, unique=True)
    description = models.CharField(max_length=VERY_LONG_STR_MAX_LENGTH, blank=True)
    ingredients = models.ManyToManyField(Ingredient, through='DishIngredientDetails')
    portion_weight = models.DecimalField(max_digits=MEASURE_MAX_DIGITS, decimal_places=MEASURE_DECIMAL_PLACES)
    unit = models.ForeignKey(MeasurementUnit, on_delete=models.DO_NOTHING)
    portion_count = models.IntegerField()

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'dish'
        verbose_name = 'Dish'
        verbose_name_plural = 'Dishes'
        ordering = ['name']


# dish-ingredient intermediary table. explicitly defined to add extra fields like weight and unit of ingredients
class DishIngredientDetails(models.Model):
    ingredient = models.ForeignKey(Ingredient, on_delete=models.DO_NOTHING)
    dish = models.ForeignKey(Dish, on_delete=models.DO_NOTHING)
    ingredient_weight = models.DecimalField(max_digits=MEASURE_MAX_DIGITS, decimal_places=MEASURE_DECIMAL_PLACES)
    unit = models.ForeignKey(MeasurementUnit, on_delete=models.DO_NOTHING)

    def __str__(self):
        return '{d} - {i} ({iw} {unit})'.format(d=self.dish.name, i=self.ingredient.name, iw=self.ingredient_weight,
                                                unit=self.unit.name)

    class Meta:
        db_table = 'dish_ingredient'
        verbose_name = 'Dish Ingredient Detail'
        verbose_name_plural = 'Dish Ingredient Details'


# package category
class PackageCategory(models.Model):
    name = models.CharField(max_length=LONG_STR_MAX_LENGTH, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'package_category'
        verbose_name = 'Package Category'
        verbose_name_plural = 'Package Categories'
        ordering = ['name']


# A package
class Package(models.Model):
    name = models.CharField(max_length=LONG_STR_MAX_LENGTH, unique=True)
    category = models.ForeignKey(PackageCategory, on_delete=models.DO_NOTHING)
    sales_price = models.DecimalField(max_digits=MEASURE_MAX_DIGITS, decimal_places=MEASURE_DECIMAL_PLACES)
    description = models.CharField(max_length=VERY_LONG_STR_MAX_LENGTH, blank=True)
    dishes = models.ManyToManyField(Dish, db_table='package_dish')

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'package'
        verbose_name = 'Package'
        verbose_name_plural = 'Packages'
        ordering = ['name']


# A client
class Client(models.Model):
    first_name = models.CharField(max_length=LONG_STR_MAX_LENGTH)
    last_name = models.CharField(max_length=LONG_STR_MAX_LENGTH)
    phone_number = models.IntegerField()
    email = models.EmailField(unique=True)
    address_line_1 = models.CharField(max_length=LONG_STR_MAX_LENGTH)
    address_line_2 = models.CharField(max_length=LONG_STR_MAX_LENGTH, blank=True)
    unit_number = models.CharField(max_length=SHORT_STR_MAX_LENGTH)
    pin_code = models.IntegerField()

    def __str__(self):
        return '{f} {l}'.format(f=self.first_name, l=self.last_name)

    class Meta:
        db_table = 'client'
        verbose_name = 'Client'
        verbose_name_plural = 'Clients'
        ordering = ['last_name']


# An order
class Order(models.Model):
    order_date = models.DateField()
    created_ts = models.DateTimeField(auto_now_add=True)
    client = models.ForeignKey(Client, on_delete=models.DO_NOTHING)
    packages = models.ManyToManyField(Package, through='OrderPackageDetails')
    delivery = models.ForeignKey(DeliveryInfo, on_delete=models.DO_NOTHING)
    sales_price = models.DecimalField(max_digits=CCY_MAX_DIGITS, decimal_places=CCY_DECIMAL_PLACES)
    tax = models.DecimalField(max_digits=CCY_MAX_DIGITS, decimal_places=CCY_DECIMAL_PLACES)
    online_store_charge = models.DecimalField(max_digits=CCY_MAX_DIGITS, decimal_places=CCY_DECIMAL_PLACES)
    status = models.ForeignKey(OrderStatus, on_delete=models.DO_NOTHING)
    notes = models.CharField(max_length=VERY_LONG_STR_MAX_LENGTH, blank=True)

    def __str__(self):
        return 'Date : {dt}, Client : {c}'.format(dt=self.order_date, c=self.client)

    class Meta:
        db_table = 'orders'
        verbose_name = 'Order'
        verbose_name_plural = 'Orders'


class OrderPackageDetails(models.Model):
    order = models.ForeignKey(Order, on_delete=models.DO_NOTHING)
    package = models.ForeignKey(Package, on_delete=models.DO_NOTHING)
    package_qty = models.IntegerField()

    class Meta:
        db_table = 'order_package'
        verbose_name = 'Order Package'
        verbose_name_plural = 'Order Packages'


# employee role
class EmployeeRole(models.Model):
    name = models.CharField(max_length=SHORT_STR_MAX_LENGTH, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'employee_role'
        verbose_name = 'Employee Role'
        verbose_name_plural = 'Employee Roles'
        ordering = ['name']


# employee
class Employee(models.Model):
    govt_issued_id = models.CharField(max_length=SHORT_STR_MAX_LENGTH, unique=True)
    first_name = models.CharField(max_length=LONG_STR_MAX_LENGTH)
    last_name = models.CharField(max_length=LONG_STR_MAX_LENGTH)
    phone_number = models.IntegerField()
    email = models.EmailField(unique=True)
    role = models.ForeignKey(EmployeeRole, on_delete=models.DO_NOTHING)
    start_date = models.DateField()
    end_date = models.DateField()
    billing_rate = models.DecimalField(max_digits=CCY_MAX_DIGITS, decimal_places=CCY_DECIMAL_PLACES)
    billing_unit = models.ForeignKey(MeasurementUnit, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.first_name

    class Meta:
        db_table = 'employee'
        verbose_name = 'Employee'
        verbose_name_plural = 'Employees'
        ordering = ['last_name']


# employee billing
class EmployeeBilling(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.DO_NOTHING)
    billing_start_date = models.DateField()
    billing_end_date = models.DateField()
    duration = models.DecimalField(max_digits=MEASURE_MAX_DIGITS, decimal_places=MEASURE_DECIMAL_PLACES)

    def __str__(self):
        return self.employee

    class Meta:
        db_table = 'employee_billing'
        verbose_name = 'Employee Billing'
        verbose_name_plural = 'Employee Billing'


# facility
class Facility(models.Model):
    name = models.CharField(max_length=LONG_STR_MAX_LENGTH, unique=True)
    contact = models.CharField(max_length=LONG_STR_MAX_LENGTH)
    phone_number = models.IntegerField()
    email = models.EmailField(blank=True)
    address_line_1 = models.CharField(max_length=LONG_STR_MAX_LENGTH)
    address_line_2 = models.CharField(max_length=LONG_STR_MAX_LENGTH, blank=True)
    unit_number = models.CharField(max_length=SHORT_STR_MAX_LENGTH)
    pin_code = models.IntegerField()
    billing_rate = models.DecimalField(max_digits=CCY_MAX_DIGITS, decimal_places=CCY_DECIMAL_PLACES)
    billing_unit = models.ForeignKey(MeasurementUnit, on_delete=models.DO_NOTHING)
    notes = models.CharField(max_length=VERY_LONG_STR_MAX_LENGTH, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'facility'
        verbose_name = 'Facility'
        verbose_name_plural = 'Facilities'
        ordering = ['name']


# facility usage
class FacilityUsage(models.Model):
    facility = models.ForeignKey(Facility, on_delete=models.DO_NOTHING)
    billing_start_date = models.DateField()
    billing_end_date = models.DateField()
    duration = models.DecimalField(max_digits=MEASURE_MAX_DIGITS, decimal_places=MEASURE_DECIMAL_PLACES)

    def __str__(self):
        return self.facility

    class Meta:
        db_table = 'facility_usage'
        verbose_name = 'Facility Usage'
        verbose_name_plural = 'Facility Usage'


# Calculation Parameters
class CalcParameters(models.Model):
    name = models.CharField(max_length=SHORT_STR_MAX_LENGTH, unique=True)
    value = models.DecimalField(max_digits=MEASURE_MAX_DIGITS, decimal_places=3)
    description = models.CharField(max_length=SHORT_STR_MAX_LENGTH, blank=True, null=True)

    def __str__(self):
        return '{n} - {v}'.format(n=self.name, v=self.value)

    class Meta:
        db_table = 'calc_parameters'
        verbose_name = 'Calculation Parameter'
        verbose_name_plural = 'Calculation Parameters'
        ordering = ['name']


class OrderPoller(models.Model):
    received_ts = models.DateTimeField()
    message_id = models.CharField(max_length=SHORT_STR_MAX_LENGTH)
    message_snippet = models.CharField(max_length=VERY_LONG_STR_MAX_LENGTH)
    message_raw = models.TextField()
    is_captured = models.BooleanField(default=False)

    def __str__(self):
        return '{m_id} : {ts} : [{snippet}]'.format(m_id=self.message_id, ts=self.received_ts, snippet=self.message_snippet)

    class Meta:
        db_table = 'order_poller'
        ordering = ['-received_ts']


