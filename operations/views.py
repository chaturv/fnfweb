from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import View
from django.shortcuts import render
from django.contrib import messages

import pandas as pd
from datetime import datetime

from . import utils

from .dto import DishQuantities
from .dto import IngredientShoppingList

from .forms import DeliveryInfoForm
from .forms import OrderForm
from .forms import PromoSignUpForm

from .models import Order
from .models import OrderPackageDetails
from .models import Package
from .models import OrderPoller
from .models import ClientKids

from .services import DataService


class OperationsBaseView(View):
    def __init__(self, **kwargs):
        super(OperationsBaseView, self).__init__(**kwargs)
        self.context = {}

        received_orders = OrderPoller.objects.filter(is_captured=0).count()
        if received_orders != 0:
            self.context['received_orders'] = received_orders


class IndexView(OperationsBaseView):
    def get(self, request, *args, **kwargs):
        orders = DataService.get_all_orders()
        self.context['orders'] = orders

        return render(request, 'operations/index.html', self.context)


class CreateOrderView(OperationsBaseView):
    def post(self, request, *args, **kwargs):
        # POST request : we need to process the form data

        # make a copy of the request querydict to set package information
        mutable = request.POST.copy()

        # get packages and quantities of this order
        package_ids_str = mutable.get('package_ids')
        quantities_str = mutable.get('quantities')

        package_ids = utils.convert_to_list(package_ids_str)
        quantities = utils.convert_to_list(quantities_str)

        # map to lookup quantity against a package id when saving
        pkg_to_qty = {p: q for p, q in zip(package_ids, quantities)}

        # set on the mutable request querydict
        mutable.setlist('packages', package_ids)

        # create form instances and populate with data from the request:
        order_form = OrderForm(mutable)
        delivery_info_form = DeliveryInfoForm(mutable)

        # TODO : Rollback!
        if all([order_form.is_valid(), delivery_info_form.is_valid()]):
            # validate quantities
            if sum(quantities) == 0:
                self._build_error_context(request, order_form, delivery_info_form,
                                          pkg_to_qty, 'All entered quantities are zero')
                return render(request, 'operations/create-order.html', self.context)

            # get respective instances
            di = delivery_info_form.instance
            order = order_form.instance

            # set delivery status to assigned
            utils.assign_delivery(di)

            # save order
            order.save()
            # save delivery info after linking it with this order
            di.order = order
            di.save()

            # save order package details with quantity
            # query package data in bulk
            packages = Package.objects.in_bulk(package_ids)
            for _, pkg in packages.iteritems():
                package_qty = pkg_to_qty.get(pkg.id, 0)
                # ignore zero quantities
                if package_qty == 0:
                    continue

                opd = OrderPackageDetails()
                # set required params
                opd.order = order
                opd.package = pkg
                opd.package_qty = package_qty
                # save
                opd.save()

            return HttpResponseRedirect(reverse('operations:index'))
        else:
            self._build_error_context(request, order_form, delivery_info_form, pkg_to_qty, None)
            return render(request, 'operations/create-order.html', self.context)

    def _build_error_context(self, request, order_form, delivery_info_form, pkg_to_qty, message):
        packages = DataService.get_all_packages()
        # restore quantities
        for pkg in packages:
            pkg.qty = pkg_to_qty.get(pkg.id, 0)

        if message:
            messages.error(request, message)
        self.context.update({'order_form': order_form,
                             'delivery_info_form': delivery_info_form,
                             'packages': packages})

    def get(self, request, *args, **kwargs):
        # GET (or any other method) : we'll create a blank form
        order_form = OrderForm()
        delivery_info_form = DeliveryInfoForm()

        packages = DataService.get_all_packages()
        for pkg in packages:
            pkg.qty = 0

        self.context.update({'order_form': order_form,
                             'delivery_info_form': delivery_info_form,
                             'packages': packages})
        return render(request, 'operations/create-order.html', self.context)


class GenerateShoppingListView(OperationsBaseView):
    def post(self, request, *args, **kwargs):
        order_ids = request.POST.getlist('order_ids')
        dish_ids = request.POST.getlist('dish_ids')

        if len(order_ids) != 0:
            # load orders
            ids = utils.convert_to_list(order_ids)
            rows = DataService.get_shopping_list_details(order_ids=ids, dish_ids=dish_ids)

            # create data frame to process data
            df = pd.DataFrame(data=rows,
                              columns=['dish_id', 'dish_name', 'dish_qty', 'portion_count',
                                       'ingredient_name', 'total_ingredient_weight', 'total_cost_price'])

            if dish_ids:
                dish_ids = utils.convert_to_int_list(dish_ids)
                df_filtered = df[df['dish_id'].isin(dish_ids)]
            else:
                df_filtered = df

            # sum up ingredients weight and cost
            df_ingrds = df_filtered.groupby(['ingredient_name'])['total_ingredient_weight', 'total_cost_price'].sum()
            # prepare DTO
            ingrds_shopping_list = []
            for row in df_ingrds.itertuples():
                ingrds_shopping_list.append(IngredientShoppingList(
                    row[0], row.total_ingredient_weight, row.total_cost_price
                ))

            # get dishes quantities by dropping dupes
            df_dishes = df.drop_duplicates(['dish_id', 'dish_name', 'dish_qty', 'portion_count'])
            # prepare DTO
            dish_quantities = []
            for row in df_dishes.itertuples():
                dish_quantities.append(DishQuantities(
                    row.dish_id, row.dish_name, row.dish_qty, row.portion_count
                ))

            # add to context
            order_ids_str = utils.convert_to_string_arr(order_ids)
            self.context.update({'ingredients_shopping_list': ingrds_shopping_list,
                                 'dish_quantities': dish_quantities,
                                 'order_ids': order_ids_str})
            if dish_ids:
                self.context['selected_dish_ids'] = utils.convert_to_string_arr(dish_ids)

            return render(request, 'operations/generate-shopping-list.html', self.context)
        else:
            orders = DataService.get_all_orders()
            self.context.update({
                'orders': orders
            })

            messages.error(request, 'Select at least one order to generate shopping list')
            return render(request, 'operations/index.html', self.context)


class CompleteOrderView(OperationsBaseView):
    def get(self, request, *args, **kwargs):
        return HttpResponse("Not implemented")


class DeleteOrderView(OperationsBaseView):
    def post(self, request, *args, **kwargs):
        order_ids = request.POST.getlist('order_ids')

        if len(order_ids) != 0:
            order_ids = utils.convert_to_int_list(order_ids)

            opds = OrderPackageDetails.objects.filter(order_id__in=order_ids)
            opds.delete()

            orders = Order.objects.filter(id__in=order_ids)
            out = orders.delete()
            count = out[1]['operations.Order']

            messages.success(request, '{count} order(s) deleted'.format(count=count))
            return HttpResponseRedirect(reverse('operations:index'))
        else:
            messages.error(request, 'Select at least one order to delete')
            return HttpResponseRedirect(reverse('operations:index'))


class PromoSignUpView(OperationsBaseView):
    def get(self, request, *args, **kwargs):
        self.context.update({'promo_signup_form': PromoSignUpForm()})

        return render(request, 'operations/promo-signup.html', self.context)

    def post(self, request, *args, **kwargs):
        form = PromoSignUpForm(request.POST)

        # TODO: Rollback!
        if form.is_valid():
            client = form.instance

            # get phone number
            phone_number = request.POST.get('phone_number')
            client.phone_number = phone_number if phone_number else 0

            # set blanks for fields we are not capturing
            client.address_line_1 = ''
            client.address_line_2 = ''
            client.unit_number = ''
            client.pin_code = 0

            # save
            client.save()

            # save birthdays if entered
            bday_dates = request.POST.getlist('bdayDate')
            if bday_dates:
                client_kids = []
                for bd in bday_dates:
                    if bd:  # not a blank string
                        try:
                            birth_date = datetime.strptime(bd, '%Y-%m-%d')
                            client_kids.append(ClientKids(client=client, birth_date=birth_date))
                        except ValueError as ex:
                            messages.error(request, 'Please enter a valid birthday: {bd}'.format(bd=bd))
                            # TODO : Update date field values
                            self.context.update({'promo_signup_form': form})
                            return render(request, 'operations/promo-signup.html', self.context)

                for ck in client_kids:
                    ck.save()

            # TODO: send email

            self.context.update({'f_name': client.first_name})
            return render(request, 'operations/promo-signup-success.html', self.context)
        else:
            self.context.update({'promo_signup_form': form})
            return render(request, 'operations/promo-signup.html', self.context)
