import pytest
import requests
import yaml

with open("config.yaml") as f:
    user_set = yaml.safe_load(f)


@pytest.fixture()
def login():
    response = requests.post(user_set['url'], data={'username': user_set['username'], 'password': user_set['password']})
    response.encoding = 'utf-8'
    return response.json()['token']


@pytest.fixture()
def search_text():
    """Страницы постов НЕ пользователя меняются, тест 2 может упасть в зависимости от описания поста"""
    return 'В своём стремлении улучшить пользовательский опыт м'


@pytest.fixture()
def description():
    return 'New post for pytest in python'