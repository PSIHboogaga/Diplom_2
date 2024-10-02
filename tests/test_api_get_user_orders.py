import requests
import allure
from constants.urls_constants import UrlsConstants


@allure.feature('Проверка получения заказа конкретного пользователя')
class TestApiGetUserOrders:
    @allure.title('Тест получения заказа авторизованного пользователя')
    @allure.description('Получаем информация по заказу')
    def test_auth_user_get_order_successful(self, user_data_and_token):
        payload, response, token = user_data_and_token
        response = requests.get(UrlsConstants.ORDER, headers={'Authorization': token})
        assert response.status_code == 200 and response.json()['success']

    @allure.title('Тест получения заказа пользователя без авторизации')
    @allure.description('Получение ошибки при попытке получить инфо о заказе без авторизации')
    def test_no_auth_user_get_user_order_error(self):
        token = None
        response = requests.get(UrlsConstants.ORDER, headers={'Authorization': token})
        assert response.status_code == 401 and response.text == '{"success":false,"message":"You should be authorised"}'
