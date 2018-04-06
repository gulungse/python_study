import sys
import io
from bs4 import BeautifulSoup
import requests
import urllib.parse as rep
import urllib.request as req
import os

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

#로그인 유저정보
LOGIN_INFO = {
     'user_id' : 'gulungse@gmail.com',
     'user_pw' : 'rlawjdgh2358',
     'user-submit' : rep.quote_plus('로그인'),
     'user-cookie' : 1
}

#Session 생성 , with 구문안에서 유지
with requests.Session() as s:
    login_req = s.post('https://www.inflearn.com/wp-login.php?redirect_to=https%3A%2F%2Fwww.inflearn.com%2F', data=LOGIN_INFO)
    #HTML 소스확인
    #print('login_req',login_req.text)
    #Header 확인
    #print('headers',login_req.headers)
    if login_req.status_code == 200 and login_req.ok:
        post_one = s.get('https://www.inflearn.com/members/gulungse/course/course-stats')
        post_one.raise_for_status()
        soup = BeautifulSoup(post_one.text, 'html.parser')
        print(soup.prettify())
        # course = soup.select("div.course.mycourse > ul > li > div.row > a > img")
        # for i,z in enumerate(course,1):
        #     #print(z)
        #     fullFileName = os.path.join("/Users/jeongho/Documents/image_down",str(i)+'.jpg')  # str(i) 는 넘버값이 정수로 넘어오기때문에 문자로 변환
        #     req.urlretrieve(z['src'],fullFileName)
        #
        #     print('사진 다운로드 완료')
