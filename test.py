import pytest
import requests
from main import get_random_cat_image  # замените на имя вашего модуля


def test_get_random_cat_image_success(mocker):
    # Мокируем метод requests.get
    mock_response = mocker.patch('requests.get')
    mock_response.return_value.ok = True  # Эмулируем успешный ответ
    mock_response.return_value.json.return_value = [{'url': 'https://example.com/cat.jpg'}]

    url = get_random_cat_image()
    assert url == 'https://example.com/cat.jpg'


def test_get_random_cat_image_not_found(mocker):
    # Мокируем метод requests.get для возврата кода 404
    mock_response = mocker.patch('requests.get')
    mock_response.return_value.ok = False  # Эмулируем неуспешный ответ
    mock_response.return_value.status_code = 404

    # Важно: метод json не должен вызываться, поэтому обработаем его вызов
    mock_response.return_value.json.side_effect = requests.exceptions.HTTPError

    url = get_random_cat_image()
    assert url is None