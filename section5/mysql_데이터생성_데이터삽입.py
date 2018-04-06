import pymysql
import simplejson as json
import datetime
import os.path

#데이터베이스 연결
conn = pymysql.connect(host='localhost', user='gulungse', password='rlawjdgh2358', db='python_app1', charset='utf8')

#버전확인
#print('pymyslq ver=', pymysql.__version__)

#데이터베이스 선택
#conn.select_db('python_app1')


#cursor 연결
c = conn.cursor()
print(c)

#데이터베이스 생성
#c.execute('create database python_app2')

#커서 반환
#c.close()

#접속 해제
#conn.close()

#트랜젝션 선언
#conn.begin()

#트랜잭션 커밋
#conn.commit()

#트랜잭션 롤백
#conn.rollback()

#날짜 생성
now = datetime.datetime.now()
nowDateTime = now.strftime('%Y-%m-%d %H:%M:%S')
print('##현재시간## : ',nowDateTime)


#테이블생성
c.execute("CREATE TABLE IF NOT EXISTS users(id bigint(20) NOT NULL, \
                     username varchar(20),  \
                     email varchar(30), \
                     phone varchar(30), \
                     website varchar(30), \
                     regdate varchar(20) NOT NULL, PRIMARY KEY(id))" \
          )


#테이블 생성 실행
#conn.commit()

try:
    with conn.cursor() as c:
        #JSON을 mysql 에 저장
        with open('/Users/jeongho/Documents/section5/users.json', 'r') as infile:
            r = json.load(infile)
            userData = []
            for user in r:
                t = (user['id'], user['username'], user['email'], user['phone'], user['website'],nowDateTime)
                userData.append(t)
            c.executemany("INSERT INTO users(id, username, email, phone, website, regdate) VALUES (%s, %s, %s, %s,%s, %s)", userData)
        conn.commit()

finally:
    conn.close()
