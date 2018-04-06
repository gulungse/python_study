from bs4 import BeautifulSoup
import urllib.request as req
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

url = "http://www.hogaeng.co.kr/g4s/bbs/board_pc.php?bo_table=escape_skt"
res = req.urlopen(url).read()
soup = BeautifulSoup(res, "html.parser")


#print('결과 : ', soup.prettify())
top = soup.select("tr.bo_notice1 > td.td_subject > a")

#print(top)

for i,e in enumerate(top,1):
    print(i,e.string)
