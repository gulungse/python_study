import sys
import io
import urllib.request as req
from urllib.parse import urlparse

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')


url = "http://www.encar.com"

mem = req.urlopen(url)

#print(type(mem))
#print("geturl",mem.geturl())

#print("status",mem.status)
#200 : 정상
#404 : 페이지 없음
#405 : 권한없음
#500 : 서버에러

#print("headers",mem.getheaders())
#print("info",mem.info())

#print("code",mem.getcode())

#print("read",mem.read(150).decode("utf-8")) # or euc-kr

print(urlparse("http://www.encar.com"))
