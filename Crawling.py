from selenium import webdriver

driver = webdriver.Chrome(
    r'C:/Users/smddu/Documents/chromedriver/chromedriver.exe')
driver.implicitly_wait(3)
driver.get(
    'https://logins.daum.net/accounts/signinform.do?url=https%3A%2F%2Fwww.daum.net%2F')

driver.find_element_by_name('id').send_keys('아이디')
driver.find_element_by_name('pw').send_keys('비밀번호')
driver.find_element_by_id('loginBtn').click()
