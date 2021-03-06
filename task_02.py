#!/usr/bin/env python
# -*- coding: utf-8 -*-

from data import FRUIT  # Copy ``data.FRUIT`` into the global namespace 

def get_cost_per_item(shoplist):
    """

    Arg:
        shoplist(dict):Fruit dictionary keyed through  item name found in
        ``FRUIT``.The value of ``shoplist`` should be an integer indicating
        the number of units to purchase.

    Return:
        Returns the item and cost in list

    Examples:
        >>> print shoplist
        {'Raspberries': 3.99, 'Beet': 1, 'Peach': 24, 'Lime': 12}
        >>> print 'Spent Shoplist', get_cost_per_item(shoplist)
        Spent Shoplist {'Raspberries': 15.920100000000001, 'Peach': 95.76,
        'Lime': 7.08}
    """
    results = {key: shoplist[key] * FRUIT[key]
               for key in shoplist.iterkeys()
               if key in FRUIT}
    return results



def get_total_cost(shoplist):
    """Function returns sum of total cost per item in shoping list

    Args:
     shoplist(dict):keyed for item name as found in  ``FRUIT``. The value of
     ``shoplist`` should be an integer indicating the # of units to purchase.

    Examples:
        >>> print 'key/value ', get_cost_per_item({'Lime': 12,'Peach': 24,
        'Beet': 1})
        key/value  {'Peach': 95.76, 'Lime': 7.08}

        >>> print get_total_cost({'Lime': 12, 'Red Pear': 4, 'Peach': 24,
        'Beet': 1})
        112.8
    """
    # getting cost per item reult from total cost funct to get list cost
    items_cost = get_cost_per_item(shoplist)
    
    total_cost = sum(value for value in
                     get_cost_per_item(shoplist).itervalues())
    return total_cost


                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    
if __name__ == '__main__':
    shoplist = {'Beet': 1, 'Raspberries': 3.99, 'Lime': 12, 'Peach': 24}
    print shoplist
    print 'Spent Shoplist', get_cost_per_item(shoplist)
    print 'key/value ', get_cost_per_item({'Lime': 12,'Peach': 24,'Beet': 1})
    print get_total_cost({'Lime': 12, 'Red Pear': 4, 'Peach': 24, 'Beet': 1})
