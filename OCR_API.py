import requests
import uuid
import time
import json

api_url = 'https://htacxyxwab.apigw.ntruss.com/custom/v1/19265/3afa64b3fd5507804c03d8feb7f9cdd58d892e02857b9d55f392552c8e63c090/general'
secret_key = 'a0VwQWt2SHNGV0F6SmFreFpjcG9UWmNuWWRVS3RPank='
image_file = "ocrinput.jpg"

request_json = {
    'images': [
        {
            'format': 'jpg',
            'name': 'demo'
        }
    ],
    'requestId': str(uuid.uuid4()),
    'version': 'V2',
    'timestamp': int(round(time.time() * 1000))
}

payload = {'message': json.dumps(request_json).encode('UTF-8')}
files = [
  ('file', open(image_file,'rb'))
]
headers = {
  'X-OCR-SECRET': secret_key
}

response = requests.request("POST", api_url, headers=headers, data = payload, files = files)

a=response.json()

b=open('result.json','w+')
b.write(str(a))

