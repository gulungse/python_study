import pymysql
import simplejson as json
import datetime
import os.path

#데이터베이스 연결
conn = pymysql.connect(host='localhost', user='gulungse', password='rlawjdgh2358', db='python_app1', charset='utf8')


try:
    with conn.cursor() as c:      #conn.cursor(pymysql.cursors.Dictcursor) : 리스트형대(딕셔너리로 변환해서 가져와라)
        c.execute("SELECT * FROM users")
        #1개로우
        #print(c.fetchone())
        #선택 지정
        #print(c.fetchmany(3))
        #전체 로우
        #print(c.fetchall())


        #순회1
        c.execute("SELECT * FROM users ORDER BY id ASC")
        rows = c.fetchall()
        for row in rows:
            print('usage1 >', row)


        #순회2
        c.execute("SELECT * FROM users ORDER BY id DESC")
        for row in c.fetchall():
            print('usage2 >', row)


        #조건 조회
        param1 = (1,)
        c.execute("SELECT * FROM users WHERE id=%s", param1)
        print('param1 : ', c.fetchall())

        #조건조회2
        param2 = 1
        c.execute("SELECT * FROM users WHERE id='%d'" %param1)  #v파이썬 포멧팅  %d
        print('param2 : ', c.fetchall())

        #조건조회 3
        param3 = (4,5)
        c.execute("SELECT * FROM users WHERE id IN(%s, %s)", param3)
        print('param3 : ', c.fetchall())


finally:
    conn.close()
