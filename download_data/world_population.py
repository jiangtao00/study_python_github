#! usr/bin/env python
# -*- encoding=utf-8 -*-
# __author__ = "john"
# date = 11/2018

import json
from download_data.countries_code import get_country_code
# download the data in the list
filename = "population_data.json"
with open(filename) as f:
    pop_data = json.load(f)
for pop_dic in pop_data:
    if pop_dic['Year'] == 1963:
        country_name = pop_dic['Country Name']
        population = str(int(float(pop_dic['Value'])))
        # print(country_name + ':' + population)
        code = get_country_code(country_name)
        if code:
            print(code+':'+str(population))
        else:
            # print('Error - '+country_name)
            pass
