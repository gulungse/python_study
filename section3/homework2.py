import sys
import io
from selenium import webdriver
import time
from selenium.webdriver.chrome.options import Options

#CLI ( command ling interface)

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

#chrome_options = Options()
#chrome_options.add_argument("--headless")

#CLI환경에서 자동으로 웹드라이버내에서 작업되는 코드
#driver = webdriver.Chrome(chrome_options=chrome_options,executable_path='/Users/jeongho/Documents/section3/webdriver/chrome/chromedriver')

#브라우저가 직접 움직이는 모습을 확인가능
driver = webdriver.Chrome('/Users/jeongho/Documents/section3/webdriver/chrome/chromedriver')
driver.set_window_size(1050,800)
driver.implicitly_wait(3)

driver.get('http://www.encar.com/dc/dc_carsearchlist.do?carType=kor&searchType=model&TG.R=A#!%7B%22action%22%3A%22(And.Hidden.N._.(C.CarType.Y._.(C.Manufacturer.%ED%98%84%EB%8C%80._.(C.ModelGroup.%EC%8F%98%EB%82%98%ED%83%80._.Model.%EC%8F%98%EB%82%98%ED%83%80%20%EB%89%B4%20%EB%9D%BC%EC%9D%B4%EC%A6%88%20%ED%95%98%EC%9D%B4%EB%B8%8C%EB%A6%AC%EB%93%9C.))))%22%2C%22toggle%22%3A%7B%7D%2C%22layer%22%3A%22%22%2C%22sort%22%3A%22ModifiedDate%22%2C%22page%22%3A1%2C%22limit%22%3A20%7D')
time.sleep(7)   #로딩되기를 7초간 대기
driver.implicitly_wait(3)

driver.find_element_by_name('log').send_keys('gulungse@gmail.com') #로그인폼에서 셀렉트로 name="log"를 확인해서 log 를 찾아서 아이디를 넣어줘라
driver.implicitly_wait(1)
driver.find_element_by_name('pwd').send_keys('rlawjdgh2358')  #로그인폼에서 셀렉트로 name="pwd"를 확인해서 log 를 찾아서 비밀번호를 넣어줘라
driver.implicitly_wait(1)
driver.find_element_by_xpath('//*[@id="wp-submit"]').click()  # submit 즉, 아이디 비번입력후 로그인버튼을 눌러줘라
