from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import View
from django.shortcuts import render
from django.contrib import messages

import pandas as pd

from . import utils

from .dto import DishQuantities
from .dto import IngredientShoppingList

from .forms import DeliveryInfoForm
from .forms import OrderForm

from .models import Order
from .models import OrderPackageDetails
from .models import Package
from .models import OrderPoller

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

        # get respective instances
        di = delivery_info_form.instance
        order = order_form.instance

        # set delivery status to assigned
        utils.assign_delivery(di)

        # TODO : Rollback!
        if all([order_form.is_valid(), delivery_info_form.is_valid()]):
            # save order
            order.save()
            # save delivery info after linking it with this order
            di.order = order
            di.save()

            # save order package details with quantity
            # query package data in bulk
            packages = Package.objects.in_bulk(package_ids)
            for _, pkg in packages.iteritems():
                package_qty = pkg_to_qty[pkg.id]
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
            print '*' * 40
            print "NOT VALID!!"
            # TODO: set errors
            self.context.update({'order_form': order_form,
                                 'delivery_info_form': delivery_info_form})
            return render(request, 'operations/create-order.html', self.context)

    def get(self, request, *args, **kwargs):
        # GET (or any other method) : we'll create a blank form
        order_form = OrderForm()
        delivery_info_form = DeliveryInfoForm()

        package_ids = DataService.get_all_packages()
        self.context.update({'order_form': order_form,
                             'delivery_info_form': delivery_info_form,
                             'packages': package_ids})
        return render(request, 'operations/create-order.html', self.context)


class GenerateShoppingListView(OperationsBaseView):
    def post(self, request, *args, **kwargs):
        order_ids = request.POST.getlist('order_ids')
        dish_ids = request.POST.getlist('dish_ids')

        if len(order_ids) != 0:
            # load orders
            ids = utils.convert_to_int_list(order_ids)
            rows = DataService.get_shopping_list_details(order_ids=ids, dish_ids=dish_ids)

            # create data frame to process data
            df = pd.DataFrame(data=rows,
                              columns=['dish_id', 'dish_name', 'dish_qty',
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
            df_dishes = df.drop_duplicates(['dish_id', 'dish_name', 'dish_qty'])
            # prepare DTO
            dish_quantities = []
            for row in df_dishes.itertuples():
                dish_quantities.append(DishQuantities(
                    row.dish_id, row.dish_name, row.dish_qty
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


class ShowPromo(OperationsBaseView):
    def get(self, request, *args, **kwargs):
        return HttpResponse("Not implemented")
