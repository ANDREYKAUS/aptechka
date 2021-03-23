import sys
from io import BytesIO
import requests
from PIL import Image
from geocoder import get_ll_span


def open_image(ll, spn, point, placemark='ya_en', mode='map'):
    map_api_server = "http://static-maps.yandex.ru/1.x/"
    map_params = {
        "ll": ll,
        "spn": spn,
        "l": mode,
        'pt': f'{point},{placemark}',
    }
    response = requests.get(map_api_server, params=map_params)

    Image.open(BytesIO(
        response.content)).show()

