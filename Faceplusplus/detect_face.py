import requests
import json


def detect(path_to_my_photo):
    files = {
        # api_key and api_secret are my credentials to use Face++, you can change them with yours or leave them like this
        'api_key': (None, 'usngPb4lq61KBloDSZhaUbOCwnu_OzYM'),
        'api_secret': (None, 'meZ3oBTdjYLLTiySy_yRUNjJ0JssVdJt'),
        'image_file': (path_to_my_photo, open(path_to_my_photo, 'rb')),
        'return_attributes': (None, 'gender,age,ethnicity,emotion')
    }

    response = requests.post('https://api-us.faceplusplus.com/facepp/v3/detect', files=files)
    print(response.json())
    f = open("response.json", "w")
    f.write(json.dumps(response.json(), indent=4))
    f.close()
