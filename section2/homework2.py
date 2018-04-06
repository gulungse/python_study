from bs4 import BeautifulSoup
import urllib.request as req
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

url = "http://wwww.daum.net/"
res = req.urlopen(url).read()
soup = BeautifulSoup(res, "html.parser")


#print('결과 : ', soup.prettify())

top = soup.find_all("a", tabindex="-1")

#print(top)

for i,e in enumerate(top,1):
    print(i,e.string)
    
