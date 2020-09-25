#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 19 23:42:43 2020

@author: daviesb
"""


class WineBottle():
    
    """
    WineBottle class with various attributes associated with a bottle of wine.
    Only vintage, producer, and name are required attributes
    """
            
    def __init__(self, vintage=None, producer=None, name=None, identifier=None, country=None, region=None, subregion=None, 
                 size=None, cellar=None, color=None, sweetness=None, wa_rating=None, my_rating=None, price=None, 
                 wine_class=None, wine_tier=None, store=None, purchase_date=None):
        self.vintage = vintage
        self.producer = producer
        self.name = name
        self.identifier = identifier
        self.country = country
        self.region = region
        self.subregion = region
        self.size = size
        self.cellar = cellar
        self.color = color
        self.sweetness = sweetness
        self.wa_rating = wa_rating
        self.my_rating = my_rating
        self.price = price
        self.wine_class = wine_class
        self.wine_tier = wine_tier
        self.store = store
        self.purchase_date = purchase_date
        


class WineCase():
    """
    Class to handle collections of WineBottle objects
    """
    
    def __init__(self, *bottles, name=None):
        self.bottles_in_case = (*bottles, )
        if name:
            self.name = name
        else:
            self.name = 'unknown_case'
        
        
    def add_bottles(self, *bottles):
        self.bottles_in_case.extend([*bottles])
            
        
    def remove_bottles(self, *bottles_removed):
        self.bottles_in_case = [bottle for bottle in self.bottles_in_case if bottle not in [*bottles_removed]]
        
        
    def show_bottles(self):
        print('-------------------------')
        print('Bottles from ' + self.name + ': ')
        for bottle in self.bottles_in_case:
            print(str(bottle.producer) + ' | ' + str(bottle.name) + ' | ' + str(bottle.vintage))
        
        
    def get_num_bottles(self):
        return len(self.bottles_in_case)
    
    
    def get_average_metric(self, metric):
        """
        Parameters
        ----------
        metric : numeric
            parameter must be a numeric attribute such as vintage or price.

        Returns
        -------
        float
            return average value of the metric for a given case.
        """
        _metric_sum = 0
        for bottle in self.bottles_in_case:
            _metric_sum += bottle.__dict__[metric]
        return _metric_sum / self.get_num_bottles()
    
            
        
        

# test = WineBottle(vintage=2012, producer='Jackse', name='Ghost Story', price=45.00)

# test2 = WineBottle(vintage=2013, producer='Jackse', name='Blah Blah', price=85.00)

# test3 = WineBottle(vintage=2019, producer='Truro', name='Special Edition', price=20.00)


# test_case = WineCase(test, test2, test3, name='Test_case')
# test_case.show_bottles()
# test_case.remove_bottles(test2, test3)
# test_case.show_bottles()
# test_case.add_bottles(test3, test2)
# test_case.show_bottles()


