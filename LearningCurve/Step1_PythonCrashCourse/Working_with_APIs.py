import requests
import pygal
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
r = requests.get(url)
print("Status Code: ", r.status_code)

response_dict = r.json()
print(response_dict.keys())

repo_dicts = response_dict['items']
print("Repositories received: ", len(repo_dicts))

# repo_dict = repo_dicts[0]
# print("\nKeys:", len(repo_dict))
#
# for key in repo_dict.keys():
#     print(key)

# print("\nSelected information about first repository:")
# print('Name:', repo_dict['name'])
# print('Owner:', repo_dict['owner']['login'])
# print('Stars:', repo_dict['stargazers_count'])
# print('Repository:', repo_dict['html_url'])
# print('Created:', repo_dict['created_at'])
# print('Updated:', repo_dict['updated_at'])
# print('Description:', repo_dict['description'])

names, stars = [],[]

for repo_dict in repo_dicts:
    names.append(repo_dict['name'])
    stars.append(repo_dict['stargazers_count'])




# Set graph color scheme
my_style = LS('#333366', base_style = LCS)
# Chose Bar chart template
chart = pygal.Bar(style = my_style, x_label_rotation=45, show_legend=False)
# Set title

"""Use Config() theme to setup bar plot"""
# my_config = pygal.Config()
# my_config.x_label_rotation = 45
# my_config.show_legend = False

chart.title = "Most Starred Python Projects in GitHub"
# Set x labels
chart.x_labels = names
# Drag and drop data into Bar chart template
chart.add('', stars)
# Output graph to svg fileß
chart.render_to_file('python_repos.svg')