from operator import itemgetter
from plotly.graph_objs import Bar
from plotly import offline
import requests

# Make api call and store response

url = 'https://hacker-news.firebaseio.com/v0/topstories.json'
r = requests.get(url)
print(f"status code {r.status_code}")

# Process info

submission_ids = r.json()
submission_dicts = []

for submission_id in submission_ids[:30]:
    # Make a seperate API call for each submission
    url = f'https://hacker-news.firebaseio.com/v0/item/{submission_id}.json'
    r = requests.get(url)
    print(f"id: {submission_id}\tstatus: {r.status_code}")
    response_dict = r.json()

    #Build dictionary
    submission_dict = {
        'title' : response_dict['title'],
        'hn_link' : response_dict['url'],
        'comments' : response_dict.get('descendants', 0)
    }
    submission_dicts.append(submission_dict)

submission_dicts = sorted(submission_dicts, key=itemgetter('comments'),reverse=True)
x, y = [],[]
for submission in submission_dicts:
    print(f"\nTitle: {submission['title']}")
    print(f"Discussion link: {submission['hn_link']}")
    print(f"Comments: {submission['comments']}")
    x.append(submission['title'])
    y.append(submission['comments'])

data = [{
    'type' : 'bar',
    'x' : x,
    'y' : y
}]

my_layout = {
    'title' : 'Most Popular Article By Comments',
    'xaxis' : {'title' : 'Names Of Articles'},
    'yaxis' : {'title' : "Number Of Comments"}
}

fig = {'data' : data, 'layout' : my_layout}
offline.plot(fig,filename='hn_data.html')