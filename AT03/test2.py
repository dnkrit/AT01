import pytest
from main2 import get_random_cat_image

def test_cat_api_success(mocker):
    mock_get = mocker.patch('main2.requests.get')
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = [
        {'url': 'https://cdn2.thecatapi.com/images/abc123.jpg'}
    ]

    image_url = get_random_cat_image()
    assert image_url == 'https://cdn2.thecatapi.com/images/abc123.jpg'


def test_cat_api_failure(mocker):
    mock_get = mocker.patch('main2.requests.get')
    mock_get.return_value.status_code = 404

    image_url = get_random_cat_image()
    assert image_url is None
