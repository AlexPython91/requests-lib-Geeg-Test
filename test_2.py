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

import requests


def get_posts(token):
    get = requests.get('https://test-stand.gb.ru/api/posts', headers={'X-Auth-Token': token}, params={'owner': 'notMe'})
    content_list = [i['content'] for i in get.json()['data']]
    return content_list


def create_post(token):
    post = requests.post('https://test-stand.gb.ru/gateway/posts', headers={'X-Auth-Token': token})
    return post.json()


def get_new_post(token):
    get_my_post = requests.get('https://test-stand.gb.ru/api/posts', headers={'X-Auth-Token': token})
    description_in_my_post = [i['description'] for i in get_my_post.json()['data']]
    return description_in_my_post


def test_step2(login, check_text1):
    assert check_text1 in get_posts(login)


def test_step3(login, check_text2):
    assert check_text2 in get_new_post(login)
