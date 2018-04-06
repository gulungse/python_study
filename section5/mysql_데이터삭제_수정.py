import pymysql
import simplejson as json
import datetime
import os.path

#데이터베이스 연결
conn = pymysql.connect(host='localhost', user='gulungse', password='rlawjdgh2358', db='python_app1', charset='utf8')

try:
    with conn.cursor() as c:
        #데이터 수정
        c.execute("UPDATE users SET username = %s WHERE id = %s", ('niceman', 1))
        #데이터 수정2
        c.execute("UPDATE users SET username = '%s' WHERE id = '%d'" % ('goodboy', 2))

        #중간데이터 확인
        c.execute("SELECT * FROM users ORDER BY id DESC")
        for row in c.fetchall():
            print('check1 : ', row)

        #데이터 삭제
        c.execute("DELETE FROM users WHERE id = %s",(1,))
        #데이터 삭제2
        c.execute("DELETE FROM users WHERE id = '%s'" % (2,))

        #중간데이터2
        c.execute("SELECT * FROM users ORDER BY id DESC")
        for row in c.fetchall():
            print('check2 : ', row)

    conn.commit()

finally:
    conn.close()
