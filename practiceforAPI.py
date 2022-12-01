import requests
from bs4 import BeautifulSoup as bs
import json
import re


def api(name):

    url = 'http://apis.data.go.kr/1471000/DrbEasyDrugInfoService/getDrbEasyDrugList'
    params = {'serviceKey': 'PvrIUvAktOxd6AOTm2RPSs8ovw0vx517mITghrvn8+qD/IHJZQd4j+mjnD9nrT4/arMuTl44EGSvLLym15eBRQ==',
              'itemName': name, 'type': 'json'}
    response = requests.get(url, params=params).json()
    a = open('result.json', 'w+t', encoding='utf8')

    for key, value in response['body']['items'][0].items():
        if value != None:
            response['body']['items'][0][key] = re.sub(
                pattern='<[^>]*>', repl='', string=value)
            response['body']['items'][0][key] = re.sub(
                pattern='\n', repl='', string=response['body']['items'][0][key])
        else:
            pass
    a.close()

    print(response)
    json.dump(response['body']['items'][0], a, ensure_ascii=False)
    return a


# 인수는 약 이름, return은 해당하는 json['body']['items'] 이어야함
