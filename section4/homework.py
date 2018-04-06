import sys
import io
import urllib.request as req
from bs4 import BeautifulSoup
import os.path

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')


#다운로드 url

url ="http://www.weather.go.kr/wid/queryDFSRSS.jsp?zone=1150059000"
savename = "/Users/jeongho/Documents/section4/hwagok.xml"

if not os.path.exists(savename):
    req.urlretrieve(url, savename)

#BeautifulSoup 파싱
xml = open(savename, 'r', encoding="utf-8").read()
soup = BeautifulSoup(xml, 'html.parser')

#지역확인
info = {}
for location in soup.find_all("data"):
    hour = location.find("hour").string
    #print(hour)
    wether = location.find_all("tmn")
#    print(wether)
    if not (hour in info):
        info[hour] = []
    for tmn in wether:
        info[hour].append(tmn.string)

# # #print(info)
#print(info.keys())
#
# 각 지여결 날씨 텍스트 쓰기
with open('/Users/jeongho/Documents/section4/forecast.txt', 'wt') as f:
    for hour in sorted(info.keys()):
        print("+",hour)
        f.write(str(hour)+'\n')
        for n in info[hour]:
            print("-",n)
            f.write('\t'+str(n)+'\n')
