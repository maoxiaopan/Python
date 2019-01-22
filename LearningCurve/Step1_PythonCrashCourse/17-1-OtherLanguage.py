import requests
import pygal

url = "https://api.github.com/search/repositories?q=language:JavaScript&sort=stars"
r = requests.get(url)
response_dict = r.json()
response_dicts = response_dict['items']
print(len(response_dict))
print("Total counts for JavaScript projects is: ", response_dict['total_count'])

# Show Bar Chart by list
name, link, stars,plot_dicts = [], [], [],[]
for response in response_dicts[:5]:
    name.append(response['name'])
    link.append(response['html_url'])
    stars.append(response['stargazers_count'])
    plot_dict={
        'value':response['stargazers_count'],
        'label':response['description'],
        'xlink':response['html_url'],
        }
    plot_dicts.append(plot_dict)



my_bar_config = pygal.Config()
my_bar_config.x_label_rotation = 45
my_bar_config.show_legend = False
my_bar = pygal.Bar(config=my_bar_config, style = pygal.style.LightColorizedStyle)
my_bar.title="Try my first Bar chart"
my_bar.x_labels = name
# my_bar.add('', stars)
my_bar.add('', plot_dicts)
# my_bar.render_to_file('JavaScriptRanking.svg')
# my_bar.render_to_file('JavaScriptRanking_Dicts.svg')
my_bar.render_in_browser()
