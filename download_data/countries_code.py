#! usr/bin/env python
# -*- encoding=utf-8 -*-
# __author__ = "john"
# date = 11/2018

from pygal_maps_world.i18n import COUNTRIES
def get_country_code(country_name):
    """get the code based on the country_name"""
    for code, name in COUNTRIES.items():
        if name == country_name:
            return code
        return None

