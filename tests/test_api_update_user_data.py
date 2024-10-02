import requests
import allure
import helpers
from constants.urls_constants import UrlsConstants

@allure.feature('Проверка изменения данных пользователя')
class TestApiUpdateUserData:
    @allure.title('Тест изменения данных авторизованного юзера')
    @allure.description('Вносим изменения во все параметры. Данные авторизованного юзера меняются.')
    def test_auth_user_update_data_successful(self, user_data_and_token):
        payload, response, token = user_data_and_token
        payload = helpers.payload
        response = requests.patch(UrlsConstants.DELETE_USER, headers={'Authorization': token}, data=payload)
        assert response.status_code == 200 and response.json()['success']

    @allure.title('Тест изменения данных НЕ авторизованного юзера')
    @allure.description('Получение ошибки в ответе метода при попытке внести изменения без авторизации. Данные не меняются.')
    def test_noauth_user_update_data_error(self):
        payload = helpers.payload
        response = requests.patch(UrlsConstants.DELETE_USER, data=payload)
        assert response.status_code == 401
        assert response.text == '{"success":false,"message":"You should be authorised"}'
