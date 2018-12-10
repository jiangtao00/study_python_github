#! usr/bin/env python
# -*- encoding=utf-8 -*-
# __author__ = "john"
# date = 11/2018


import requests
import pygal
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
r = requests.get(url)
print("Status code:", r.status_code)
# storage the API's feedback
response_dict = r.json()
# print(response_dict.keys())
# explore the information about the warehouse
repo_dicts = response_dict['items']
print("repositories returned:", len(repo_dicts))

# study the first warehouse
# repo_dict = repo_dicts[0]
# print("\nkeys:", len(repo_dict))
# for key in sorted(repo_dict.keys()):
#     print(key)
#
# print("\nSelected information about first repository:")
# print('Name:', repo_dict['name'])
# print('Owner:', repo_dict['owner']['login'])
# print('Stars:', repo_dict['stargazers_count'])
# print('Repository:', repo_dict['html_url'])
# print('Created:', repo_dict['created_at'])
# print('Updated:', repo_dict['updated_at'])
# print('Description:', repo_dict['description'])
# names, stars = [], []
names, plot_dicts = [], []
for repo_dict in repo_dicts:
    names.append(repo_dict['name'])
    plot_dict = {
        'value': repo_dict['stargazers_count'],
        'lable': repo_dict['description'],
        'xlink': repo_dict['html_url'],
    }
    plot_dicts.append(plot_dict)

# visible
my_style = LS('#333366', base_style=LCS)

my_config = pygal.Config()
my_config.x_label_rotation = 45
my_config.show_legend = False
my_config.title_font_size = 24
my_config.lable_font_size = 14
my_config.major_lable_font_size = 18
my_config.truncate_label = 15
my_config.show_y_guides = False
my_config.width = 1000


chart = pygal.Bar(my_config, style=my_style)
chart._title = "Most_starred python projects on Git"
chart.x_labels = names

chart.add('', plot_dicts)
chart.render_to_file('python_repos.svg')

