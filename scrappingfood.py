import urllib.request
from bs4 import BeautifulSoup

webpage = urllib.request.urlopen('http://m.soongguri.com/m_req/m_menu.php?rcd=2&sdt=20230206')
soup = BeautifulSoup(webpage, 'html.parser')

'''
    ?    rcd=2  &   sdt=20230206
    rcd=1 -> 학생식당
    rcd=2 -> 숭실도담식당

    sdt   -> 날짜

'''
print(soup)


def getTodayMenu(rcd:int, sdt:int):
    webpage=urllib.request.urlopen(f'http://m.soongguri.com/m_req/m_menu.php?rcd={rcd}&sdt={sdt}')
    soup:BeautifulSoup = BeautifulSoup(webpage, 'html.parser')
    if (rcd==1): #학생식당
        pass
        #일단 학생식당 부분은 pass

    if (rcd==2): #도담식당
        pass



