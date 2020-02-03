from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.common.exceptions import ElementNotVisibleException

from collections import defaultdict
import re
import socket
import urllib.request
from urllib import parse

get_ip = lambda: re.search(re.compile('\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}'),urllib.request.urlopen('http://checkip.dyndns.org').read().decode('utf-8')).group()
get_useragent = lambda wd: wd.execute_script('return navigator.userAgent;')

# 웹드라이버 불러오기
chromedriver_path = '../../chromedriver.exe'
wd = webdriver.Chrome(chromedriver_path)

# 로그인하기
wd.get('https://accounts.interpark.com/login/form')
wd.find_element_by_id('userId').send_keys(my_id)
wd.find_element_by_id('userPwd').send_keys(my_pwd)
wd.find_element_by_id('btn_login').click()

# 우선 접속
urls = dict()
#start_url = 'http://mticket.interpark.com/Goods/GoodsInfo/info'
#urls['GoodsCode'] = '19016582'
urls['GoodsCode'] = '19018738'
#wd.get('{0}?GoodsCode={1}&app_tapbar_state=fix'.format(start_url, urls['GoodsCode']))
base_url = 'https://moticket.interpark.com/' \
             'OneStop/' \
             'PlayDateTime?'
urls['UserAgent'] = get_useragent(wd)
urls['BrowserType'] = 'S'
urls['RemoteAddr'] = get_ip()
urls['BizCode'] = '15523'
urls['SessionID'] = wd.session_id
urls['SelectSeatCnt'] = '0'
urls['SportsYN'] = 'N'

# 직링 연결
urls['DirectURL'] = parse.urlencode(urls, encoding='utf-8', doseq=True)
print("직링:", base_url + urls['DirectURL'])
wd.get(base_url + urls['DirectURL'])

# 해당하는 날짜의 a 태그 찾아주기
play_date = '20200221'
print("날짜:", play_date)
wd.find_element_by_xpath('//a[@playdate="{0}"]'.format(play_date)).click()

# 해당하는 시간의 a태그 찾아주기
play_time = '8:00'
print("시간:", play_time)
links = wd.find_elements_by_xpath('//div[@class="seatContentTitle"]')
for link in links:
    if play_time in link.text:
        link.find_element_by_xpath('a[@href]').click()
        break

# 여기서 안심문자 코드를 입력해야함
#input()

# 좌석선택
seat_type = "R"
select_num = 1
iframes = wd.find_elements_by_tag_name('iframe')

wd.switch_to.frame(iframes[1])
links = wd.find_elements_by_xpath('//*[@id="TmgsTable"]/tbody/tr[1]/td/img[contains(@alt, "[{0}석]")]'.format(seat_type))
for link in links:
    if not select_num:
        break
    print(type(link))
    link.click()
    select_num -= 1


