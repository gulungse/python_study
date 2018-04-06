from bs4 import BeautifulSoup

import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

fp = open("cars.html",encoding="utf-8")

soup = BeautifulSoup(fp, "html.parser")

def car_func(selector):
#함수시작(def) - 함수명(car_func) - 함수내용 담길 변수명(selector)
    print("차량명 :", soup.select_one(selector).string)

car_lambda = lambda q : print("car_lambda", soup.select_one(q).string)



car_func("#gr")
car_func("li#gr")


car_lambda("#gr")
car_lambda("li#gr")