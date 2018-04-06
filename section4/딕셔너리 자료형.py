#딕셔너리 자료형 (key 와 value로 이루어짐) : (순서 없음 , 중복불가 , 수정가능 , 삭제가능)

#선언
a = {'name' : 'kim','phone':'01024742300','birth':19800224}
b = {0 : 'Hello World!'}
c = {'arr' : [0,1,2,3]}

print(type(a),a)
print(type(b),b)
print(type(c),c)

#출력
#print('a - ', a['address'])
print('a - ', a.get('address'))
print('c - ', type(c.get('arr')))

#딕셔너리 추가
a['address'] = 'Seoul'
print('a :' , a)
a['rank'] = [1,2,3]
print('a  - ', a)

print('a - ', list(a.keys()))  #리스트  a의 키값만을 가져와라
print('a - ', a.keys())

print('a - ', list(a.values())) #리스트 a의 밸류값만을 가져와라
print('a - ', a.values())

print('a - ', a.items())    #a 리스트의 튜플형으로 가져와라
print('a - ', list(a.items())[1])  #리스트 a의 튜플 1번을 가져와라
