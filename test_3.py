import yaml
import requests

with open("config.yaml") as f:
    user_set = yaml.safe_load(f)


def new_post(token):
    response = requests.post(user_set['posts'], headers={'X-Auth-Token': token},
                             params={'title': user_set['title'],
                                     'description': user_set['description'],
                                     'content': user_set['content']})
    response.encoding = 'utf-8'
    return response.json()


def my_posts(token):
    response = requests.get(user_set['posts'], headers={'X-Auth-Token': token})
    description_list = []
    for i in response.json()['data']:
        description_list.append(i['description'])
    return description_list


def test_step3(login, description):
    new_post(login)
    assert description in my_posts(login)
