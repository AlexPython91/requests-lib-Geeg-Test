"""
Написать тест с использованием pytest и request, в котором:
 - Адреса сайта, имя пользователя и пароль храняться в config.yaml
 - conftest.py содержит фикстуру авторизации по адресу https://test-stand.gb.ru/gateway/login с передачей параметров
 username и password и возвращающей токен авторизации
 - Тест с использованием DDT проверяет наличие поста с определенным заголовком в списке постов другого пользователя
 для этого выполняется get запрос по адресу: https://test-stand.gb.ru/api/posts с хедером, содержащим токен
 авторизации в прараметре 'X-Auth-Token'. Для отображения постов другого пользователя передается параметр
 "owner": "notMy"
 Login: ivanivanov697
 PW: bb5e16295e
 'content': 'test_content'
"""


import yaml
import requests

with open("config.yaml") as f:
    user_set = yaml.safe_load(f)


def posts(token):
    response = requests.get(user_set['posts'], headers={'X-Auth-Token': token}, params={'owner': 'notMe', 'page': 2})
    listTitle = []
    for i in response.json()['data']:
        listTitle.append(i['title'])
    return listTitle


def test_step2(login, search_text):
    assert search_text in posts(login)
