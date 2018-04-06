import sys
import io
import urllib.request as dw

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

imgUrl = "http://post.phinf.naver.net/20150527_274/whtjdgus1666_1432689219314TApr5_JPEG/mug_obj_143268921826930359.jpg"
htmlUrl = "http://www.google.co.kr"

savePath1 = "/Users/jeongho/Documents/section2/test1.jpg"
savePath2 = "/Users/jeongho/Documents/section2/index.html"

f = dw.urlopen(imgUrl).read()
f2 = dw.urlopen(htmlUrl).read()

saveFile1 = open(savePath1,'wb')
saveFile1.write(f)
saveFile1.close()


with open(savePath2,'wb') as saveFile2:
    saveFile2.write(f2)

print("다운로드완료!")
