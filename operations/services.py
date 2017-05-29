from django.db import connection

from .models import Order
from .models import Package
from .models import DeliveryStatus
from .models import CalcParameters


class DataService:
    def __init__(self):
        pass

    @staticmethod
    def get_all_orders():
        orders = Order.objects.order_by('-order_date')
        # create new variables for display
        for o in orders:
            o.package_names = ', '.join([p.name for p in list(o.packages.all())])
            o.delivery_date = o.deliveryinfo_set.get().delivery_date
            o.delivery_charge = o.deliveryinfo_set.get().charge
        return orders

    @staticmethod
    def get_all_packages():
        return Package.objects.all()

    @staticmethod
    def get_shopping_list_details(order_ids, dish_ids=None):
        """
        :param order_ids: a list of order ids as int or str. Or a single order id as int or str
        :param dish_ids: Restrict shopping list to these dishes.
                         A list of dish ids as int or str. Or a single order id as int or str.
        :return: Return shopping list for the given orders
        """
        if isinstance(order_ids, str):
            order_ids = [int(order_ids)]
        if isinstance(order_ids, int):
            order_ids = [order_ids]
        if not isinstance(order_ids, list):
            raise Exception('Expecting a single order id or a list of order ids. Got [{ids}]'.format(ids=order_ids))

        SQL = """select
                    d.id dish_id,
                    d.name dish_name,
                    sum(op.package_qty) dish_qty,
                    i.name ingredient_name,
                    round(sum(di.ingredient_weight * op.package_qty), 2) total_ingredient_weight,
                    round(sum(di.ingredient_weight * (i.cost_price/i.measure) * op.package_qty), 2) total_cost_price
                from
                    orders o, order_package op, package_dish pd, dish d, dish_ingredient di, ingredient i
                where
                    o.id = op.order_id and
                    op.package_id = pd.package_id and
                    pd.dish_id = d.id and
                    d.id = di.dish_id and
                    di.ingredient_id = i.id and
                    o.id in ({ids})
                group by d.id,	d.name, i.name
                order by d.name, i.name""".format(ids=','.join([str(x) for x in order_ids]))

        with connection.cursor() as cursor:
            cursor.execute(SQL)
            rows = cursor.fetchall()

        # return a list of tuples rather than a tuple of tuples
        return [row for row in rows]


class StaticDataDao(type):
    @property
    def delivery_statuses(cls):
        if getattr(cls, '_delivery_statuses', None) is None:
            cls._delivery_statuses = list(DeliveryStatus.objects.all())
        return cls._delivery_statuses

    @property
    def calc_parameters(cls):
        if getattr(cls, '_calc_parameters', None) is None:
            m = {}
            for p in list(CalcParameters.objects.all()):
                m[p.name] = p.value
            cls._calc_parameters = m
        return cls._calc_parameters


class StaticDataService(object):
    __metaclass__ = StaticDataDao
