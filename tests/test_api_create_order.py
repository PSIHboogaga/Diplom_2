import requests
import allure
from constants.urls_constants import UrlsConstants
from constants.ingredients_constants import IngredientsConstants


@allure.feature('Проверка создания заказа')
class TestApiCreateOrder:
    @allure.title('Тест создания заказа для авторизованного юзера')
    @allure.description('Заказ создается.')
    def test_auth_user_create_order_successful(self, user_data_and_token):
        payload, response, token = user_data_and_token
        payload = IngredientsConstants.INGREDIENTS
        response = requests.post(UrlsConstants.ORDER, headers={'Authorization': token}, data=payload)
        assert response.status_code == 200 and response.json()['success']

    @allure.title('Тест создания заказа с ингредиентами без авторизации юзера')
    @allure.description('Заказ создается')
    def test_create_order_with_ingredients_user_no_auth_successful(self):
        payload = IngredientsConstants.INGREDIENTS
        response = requests.post(UrlsConstants.ORDER, data=payload)
        assert response.status_code == 200 and response.json()['success']

    @allure.title('Тест создания заказа без ингредиентов')
    @allure.description('Вывод ошибки при создании заказа без ингридиентов')
    def test_create_order_without_ingredients_error(self):
        payload = IngredientsConstants.WITHOUT_INGREDIENTS
        response = requests.post(UrlsConstants.ORDER, data=payload)
        assert response.status_code == 400
        assert response.text == '{"success":false,"message":"Ingredient ids must be provided"}'

    @allure.title('Тест создания заказа с некорректными ингридиенами')
    @allure.description('Вывод ошибки при попытке создать заказ с некорректными ингридиентами')
    def test_create_order_bad_ingredients_error(self):
        payload = IngredientsConstants.INCORRECT_INGREDIENTS
        response = requests.post(UrlsConstants.ORDER, data=payload)
        assert response.status_code == 500 and 'Internal Server Error' in response.text
