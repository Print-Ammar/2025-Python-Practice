import requests
from plotly.graph_objs import Bar
from plotly import offline

# make api call and store response

url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
headers = {'Accept': 'application/vnd.github.v3+json'}
r = requests.get(url, headers=headers)
print(f"status code {r.status_code}")

# process results
response_dict = r.json()
repo_dicts = response_dict['items']
stars, labels, links = [], [], []

for repo_dict in repo_dicts:
    stars.append(repo_dict["stargazers_count"])
    owner = repo_dict['owner']['login']
    description = repo_dict["description"]
    label = f"{owner}<br />{description}"
    labels.append(label)
    repo_name = repo_dict['name']
    repo_url = repo_dict['html_url']
    repo_link = f"<a href='{repo_url}'>{repo_name}</a>"
    links.append(repo_link)


# make visualisation

data = [{
    'type' : 'bar',
    'x' : links,
    'y' : stars,
    'hovertext' : labels,
    'marker' : {
        'color' : 'rgb(60,100,150)',
        'line' : {'width' : 1.5, 'color' : 'rgb(25,25,25)'}
    }
}]

my_layout = {
    'title' : 'Most Starred Repositories On Github',
    'xaxis' : {'title':'Repositories'},
    'yaxis' : {'title':'stars'}
}

fig = {'data':data,'layout':my_layout}
offline.plot(fig, filename='Python_repos.html')

for repo in repo_dicts:
    print(f"The repo is {repo['name']} and the link is {repo["url"]}")