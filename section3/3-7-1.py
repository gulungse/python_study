import sys
import io
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

class NcafeWriteAtt:
    #초기화 실행(webdriver 설정)
    def __init__(self):
        chrome_options = Options()
        chrome_options.add_argument("--headless") #CLI
        self.driver = webdriver.Chrome(chrome_options=chrome_options,executable_path="/Users/jeongho/Documents/section3/webdriver/chrome/chromedriver")  #드라이버 초기화
        self.driver.implicitly_wait(5)

    #네이버카페 로그인 && 출석체크
    def writeAttendCheck(self):
        self.driver.get('https://nid.naver.com/nidlogin.login')
        self.driver.find_element_by_name('id').send_keys('graphic_2002')
        self.driver.find_element_by_name('pw').send_keys('2358rlawjdgh')
        self.driver.find_element_by_xpath('//*[@id="frmNIDLogin"]/fieldset/input').click()
        self.driver.implicitly_wait(30)
        self.driver.get('http://cafe.naver.com/AttendanceView.nhn?search.clubid=13943780&search.menuid=116')
        self.driver.implicitly_wait(30)
        self.driver.switch_to_frame('http://cafe.naver.com/MyCafeIntro.nhn?clubid=13943780')
        #self.driver.switch_to_frame(self.driver.find_element(By.XPATH,value=".//iframe[@src='http://cafe.naver.com/AttendanceView.nhn?search.clubid=13943780&search.menuid=116']"))
        self.driver.find_element_by_id('cmtinput').send_keys('오랜만입니다!!')
        self.driver.find_element_by_xpath('//*[@id="main-area"]/div[6]/table/tbody/tr[4]/td/table/tbody/tr/td[3]/a/img').click()
        time.sleep(3)

        #소멸자
    def __del__(self):
        #self.driver.close() # 현재 실행 포커스된 영역을 종료
        self.driver.quit()  # 셀레늄의 전체 프로그램 종료
        print('Removed driver Object')

# 실행 영역
if __name__ == '__main__':
    #객체 생성
    a = NcafeWriteAtt()
    #시작 시간
    start_time = time.time()
    #프로그램 실행
    a.writeAttendCheck()
    #종료 시간 출력
    print("---Total %s seconds ---" % (time.time() - start_time))
    #객체 소멸
    del a
