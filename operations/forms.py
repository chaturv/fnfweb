from crispy_forms.bootstrap import PrependedText, FieldWithButtons, StrictButton
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field, HTML


from django.forms import DateInput
from django.forms import ModelForm

from . import models
from . import utils


class CustomDateInput(DateInput):
    input_type = 'date'


class OrderForm(ModelForm):
    def __init__(self, *args, **kwargs):
        self.helper = FormHelper()

        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-lg-2'
        self.helper.field_class = 'col-lg-4'
        self.helper.form_tag = False

        hidden_calc_inputs = """<input type="hidden" id="id_tax_rate" value="{tax_rate}"/>
                                <input type="hidden" id="id_online_store_prct" value="{online_store_prct}"/>
                                <input type="hidden" id="id_online_store_markup" value="{online_store_markup}"/>
                                <input type="hidden" id="id_ids_packages" name="package_ids"/>
                                <input type="hidden" id="id_quantities" name="quantities"/>
                             """.format(tax_rate=utils.get_tax_rate(),
                                        online_store_prct=utils.get_online_store_prct(),
                                        online_store_markup=utils.get_online_store_markup())

        self.helper.layout = Layout(
            Field('order_date'),
            Field('client'),
            Field('packages', template='operations/create-order-packages.html'),
            PrependedText('sales_price', text='$', id='id_sales_price'),
            PrependedText('tax', text='$', id="id_tax"),
            HTML(hidden_calc_inputs),
            Field('online_store_charge', template='operations/create-order-online-store-charge.html'),
            Field('status'),
            Field('notes'),
        )

        super(OrderForm, self).__init__(*args, **kwargs)


    class Meta:
        model = models.Order
        fields = ['order_date',
                  'client',
                  'packages',
                  'sales_price',
                  'tax',
                  'online_store_charge',
                  'status',
                  'notes']
        widgets = {
            'order_date': CustomDateInput(),
        }


class DeliveryInfoForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(DeliveryInfoForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()

        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-lg-2'
        self.helper.field_class = 'col-lg-4'
        self.helper.form_tag = False

        self.helper.layout = Layout(
            Field('delivery_date'),
            Field('partner'),
            PrependedText('charge', text='$', id='id_delivery_charge'),
            Field('address_line_1'),
            Field('address_line_2'),
            Field('unit_number'),
            Field('pin_code'),

        )

    class Meta:
        model = models.DeliveryInfo
        fields = ['delivery_date',
                  'partner',
                  'charge',
                  'address_line_1',
                  'address_line_2',
                  'unit_number',
                  'pin_code']
        widgets = {
            'delivery_date': CustomDateInput(),
        }


class PromoSignUpForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(PromoSignUpForm, self).__init__(*args, **kwargs)

        self.helper = FormHelper()

        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-md-2'
        self.helper.field_class = 'col-md-4'
        self.helper.form_tag = False

    class Meta:
        model = models.Client
        fields = ['first_name',
                  'last_name',
                  'phone_number',
                  'email',]
