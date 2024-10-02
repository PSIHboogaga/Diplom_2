import pytest
import requests
import allure
import helpers
from constants.urls_constants import UrlsConstants


@allure.feature('Проверка создания пользователя')
class TestApiCreateUser:
    @allure.title('Тест создания нового пользователя')
    @allure.description('Новый юзер создается')
    def test_create_new_user_successful(self, user_data_and_token):
        payload, response, token = user_data_and_token
        assert response.status_code == 200 and response.json()['success']

    @allure.title('тест создания дубликата пользователя')
    @allure.description('Ошибка при создании дубликата юзера')
    def test_create_duplicate_user_error(self, user_data_and_token):
        payload, response, token = user_data_and_token
        response = requests.post(UrlsConstants.CREATE_USER, data=payload)
        assert response.status_code == 403 and response.text == '{"success":false,"message":"User already exists"}'

    @allure.title('Тест ошибки при создании пользователя без обязательного параметра')
    @allure.description('Получение ошибки при попытке создать пользователя без обязательного параметра.')
    @pytest.mark.parametrize('field', ['email', 'password', 'name'])
    def test_create_user_no_required_field_error(self, field):
        payload = helpers.payload
        del payload[field]
        response = requests.post(UrlsConstants.CREATE_USER, data=payload)
        assert response.status_code == 403
        assert response.text == '{"success":false,"message":"Email, password and name are required fields"}'
