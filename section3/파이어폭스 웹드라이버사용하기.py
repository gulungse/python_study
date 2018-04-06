import sys
import io
from selenium import webdriver
import time
from selenium.webdriver.firefox.options import Options

#CLI ( command ling interface)

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

firefox_options = Options()
firefox_options.add_argument("--headless") #CLI

#CLI환경에서 자동으로 웹드라이버내에서 작업되는 코드
driver = webdriver.Firefox(firefox_options=firefox_options,executable_path='/Users/jeongho/Documents/section3/webdriver/firefox/geckodriver')
#브라우저가 직접 움직이는 모습을 확인가능
#driver = webdriver.Firefox('/Users/jeongho/Documents/section3/webdriver/firefox/geckodriver')

#driver.implicitly_wait(5)

driver.get('https://google.com')
#time.sleep(5)

driver.save_screenshot('/Users/jeongho/Documents/section3/ff.png')

#driver.implicitly_wait(5)

driver.get('https://www.daum.net')
#time.sleep(5)

driver.save_screenshot('/Users/jeongho/Documents/section3/ff.png')

driver.quit()

print('스크린샷 저장완료')
