import sys
import io
import urllib.request as dw

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

imgurl = "http://post.phinf.naver.net/20150527_274/whtjdgus1666_1432689219314TApr5_JPEG/mug_obj_143268921826930359.jpg"
savePath = "/Users/jeongho/Documents/section2/test1.jpg"

dw.urlretrieve(imgurl, savePath)

print("다운로드 완료!")
print('ok')
