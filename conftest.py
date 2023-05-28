import pytest
import requests
import yaml


with open('config.yaml') as f:
    data = yaml.safe_load(f)
user = data['user']
password = data['password']
title = data['title']
description = data['description']
content = data['content']


@pytest.fixture()
def login():
    req = requests.post('https://test-stand.gb.ru/gateway/login', data={'username': user, 'password': password})
    return req.json()['token']


@pytest.fixture()
def create_new_post():
    create_post = requests.post('https://test-stand.gb.ru/gateway/posts', data={'title': title,
                                                                                'description': description,
                                                                                'content': content})
    return create_post.json()['data']


@pytest.fixture()
def check_text1():
    """
    При прогоне теста запрашиваемый контент меняется на странице. Тест может падать.
    """
    return 'test_content'


@pytest.fixture()
def check_text2():
    return 'Описание поста'
