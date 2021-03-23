import sys
from io import BytesIO
import requests
from PIL import Image
from geocoder import get_ll_span


def open_image(ll, spn, points=[], mode='map'):
    # рисует карту и точку на ней
    map_api_server = "http://static-maps.yandex.ru/1.x/"
    
    
    
    
    
    
    
    

    map_params = {
        "ll": ll,
        # "spn": spn,
        "l": mode,
    }
    print(points)
    if points:
        map_params['pt'] = '~'.join(points)
    response = requests.get(map_api_server, params=map_params)
    if response:
        Image.open(BytesIO(
            response.content)).show()
    else:
        print(response.status_code, response.reason)