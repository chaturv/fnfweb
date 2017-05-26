from .models import DeliveryStatus
from .services import StaticDataService


def assign_delivery(delivery_info):
    statuses = StaticDataService.delivery_statuses
    for status in statuses:
        if status.name == DeliveryStatus.ASSIGNED:
            delivery_info.status = status
            break
    else:
        msg = 'Could not change delivery status to {ds}. ' \
              'Unable to find in list of of statuses : {all}'.format(ds=DeliveryStatus.ASSIGNED, all=statuses)
        raise Exception(msg)


def get_tax_rate():
    return StaticDataService.calc_parameters['tax_rate']


def get_online_store_prct():
    return StaticDataService.calc_parameters['online_store_prct']


def get_online_store_markup():
    return StaticDataService.calc_parameters['online_store_markup']


def convert_to_list(string_arr):
    """
    Convert a comma-separated string of values to a list of int
    :param string_arr:
    :return:
    """
    if isinstance(string_arr, list):
        return string_arr
    elif isinstance(string_arr, (str, unicode)):
        return [int(x) for x in string_arr.split(',')]
    else:
        raise Exception('[{s}] cannot be converted to a list'.format(s=string_arr))


def convert_to_string_arr(a_list):
    """
    Convert a list of int or str to a comma-separated string of values
    :param a_list:
    :return:
    """
    if isinstance(a_list, (str, unicode)):
        return a_list
    elif isinstance(a_list, list):
        a_list = [str(x) for x in a_list]
        return ','.join(a_list)
    else:
        raise Exception('[{l}] cannot be converted to a string array'.format(l=a_list))


def convert_to_int_list(string_arr):
    """
    Convert a list of str to list of int
    :param string_arr:
    :return:
    """
    if isinstance(string_arr, list):
        return [int(x) for x in string_arr]
    else:
        raise Exception('[{s}] cannot be converted to a list of int'.format(s=string_arr))