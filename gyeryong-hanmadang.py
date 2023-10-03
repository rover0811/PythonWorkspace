import requests

cookies = {
    'ASPSESSIONIDCQCRTSBQ': 'CGNDMJLBPBEPKOBCGMNCCBCI',
    'uid': '',
    'sToken': '',
    'sAddr': '',
}

headers = {
    'authority': 'smartid.ssu.ac.kr',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7',
    'cache-control': 'max-age=0',
    'content-type': 'application/x-www-form-urlencoded',
    # 'cookie': 'ASPSESSIONIDCQCRTSBQ=CGNDMJLBPBEPKOBCGMNCCBCI; uid=; sToken=; sAddr=',
    'origin': 'https://smartid.ssu.ac.kr',
    'referer': 'https://smartid.ssu.ac.kr/Symtra_sso/smln.asp?apiReturnUrl=https%3A%2F%2Fsaint.ssu.ac.kr%2FwebSSO%2Fsso.jsp',
    'sec-ch-ua': '"Chromium";v="110", "Not A(Brand";v="24", "Google Chrome";v="110"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'iframe',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36',
}

data = {
    'in_tp_bit': '0',
    'rqst_caus_cd': '03',
    'userid': id,
    'pwd': pwd,
}

response = requests.post('https://smartid.ssu.ac.kr/Symtra_sso/smln_pcs.asp', cookies=cookies, headers=headers, data=data)

if response.status_code == 200:
    print("성공")
    print(response.text)


# exec(open("./gyeryong-hanmadang.py").read())