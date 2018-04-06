import sys
import io
from bs4 import BeautifulSoup
import requests
from fake_useragent import UserAgent

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

URL = "https://www.wishket.com/accounts/login/"

#Fake User-Agent 생성
ua = UserAgent()

with requests.Session() as s:
    #URL 연결 _ 토큰값을 얻기위해서 최초로 GET방식으로 페이지에 연결해서 토큰값을 얻어온다
    s.get(URL)
    #로그인정보 Payload
    LOGIN_INFO = {
        'identification' : 'gulungse',
        'password' : 'rlawjdgh2358',
        'csrfmiddlewaretoken' :s.cookies['csrftoken']
    }
    #print(s.headers)

    #요청
    response = s.post(URL,data=LOGIN_INFO,headers={'User-Agent' : str(ua.chrome), 'Referer':'https://www.wishket.com/accounts/login/'})
    #HTML 확인
    #print('response',response.text)

    if response.status_code == 200 and response.ok:
        soup = BeautifulSoup(response.text, 'html.parser') # response에 담긴정보를 html.parser를 이용해서 텍스트로 만들어라
        projectList = soup.select("table.table-responsive > tbody > tr") # response.text 에 담긴 정보에서 BeautifulSoup를 이용해서 선택자를 지정해주기
        #print(projectList)    #projectList 에는 선택자를 지정한 부분만 담긴다.
        for i in projectList:
            print(i.find('th').string,i.find('td').text) #th에 담긴 string(문자) , td에 담긴 string을 출력하라.
