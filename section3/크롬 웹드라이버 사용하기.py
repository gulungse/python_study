import sys
import io
from selenium import webdriver
import time
from selenium.webdriver.chrome.options import Options

#CLI ( command ling interface)

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

chrome_options = Options()
chrome_options.add_argument("--headless")
#CLI환경에서 자동으로 웹드라이버내에서 작업되는 코드
driver = webdriver.Chrome(chrome_options=chrome_options,executable_path='/Users/jeongho/Documents/section3/webdriver/chrome/chromedriver')
#브라우저가 직접 움직이는 모습을 확인가능
#driver = webdriver.Chrome('/Users/jeongho/Documents/section3/webdriver/chrome/chromedriver')

driver.implicitly_wait(5)

driver.get('https://google.com')
#time.sleep(5)

driver.save_screenshot('/Users/jeongho/Documents/section3/website1.png')

#driver.implicitly_wait(5)

driver.get('https://www.daum.net')
#time.sleep(5)

driver.save_screenshot('/Users/jeongho/Documents/section3/website2.png')

driver.quit()

print('스크린샷 저장완료')
