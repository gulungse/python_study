import sys
import io
import urllib.request as dw
from urllib.parse import urlparse

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

imgurl = "https://ssl.pstatic.net/tveta/libs/1187/1187866/784d22033478cd4c9437_20180315181749662.png"
savePath1 = "/Users/jeongho/Documents/section2/homework.png"

dw.urlretrieve(imgurl,savePath1)

print("다운로드완료!")
