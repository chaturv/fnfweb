from django.contrib import admin

from .models import MeasurementUnit
from .models import OrderStatus
from .models import DeliveryStatus
from .models import DeliveryPartner
from .models import PackageCategory
from .models import Package
from .models import Ingredient
from .models import IngredientSource
from .models import IngredientCategory
from .models import Dish
from .models import DishIngredientDetails
from .models import Client
from .models import ClientKids
from .models import Employee
from .models import EmployeeRole
from .models import Facility
from .models import CalcParameters

# Register models here.

admin.site.register(MeasurementUnit)
admin.site.register(OrderStatus)
admin.site.register(DeliveryStatus)
admin.site.register(DeliveryPartner)
admin.site.register(PackageCategory)
admin.site.register(Package)
admin.site.register(Ingredient)
admin.site.register(IngredientSource)
admin.site.register(IngredientCategory)
admin.site.register(Dish)
admin.site.register(DishIngredientDetails)
admin.site.register(Client)
admin.site.register(ClientKids)
admin.site.register(Employee)
admin.site.register(EmployeeRole)
admin.site.register(Facility)
admin.site.register(CalcParameters)
