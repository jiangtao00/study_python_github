#! usr/bin/env python
# -*- encoding=utf-8 -*-
# __author__ = "john"
# date = 11/2018


from pygal_maps_world.i18n import COUNTRIES
for country_code in sorted(COUNTRIES.keys()):
    print(country_code, COUNTRIES[country_code])

