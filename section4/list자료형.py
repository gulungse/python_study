# 리스트 자료형( 순서대로 정리, 중복 허용, 수정 가능, 삭제 가능)

#선언
a = []
b = list()
c = [1,2,1,3,2] # 중복가능
d = [0,1,'car','apple','apart'] #형태가 다른 (문자,숫자 가능)
e = [0,1,['car','apple','apart']] # 리스트 안에 또 리스트가 들어갈 수 있음


# #인덱싱
# print("#=========#")
# print('d -', type(d),d)
# print('d -', d[1])
# print('d -',d[0]+d[1]+d[1])
# print('e -', e[-1][1])


# # 슬라이싱
# print("#=========#")
# print('d -', d[0:3])
# print('d -', d[2:])

# # 연산
# print("#=========#")
# print('c+d =', c+d)
# print('c * 3 =', c*3)
# print('hi +c[0] =','hi'+str(c[0]))

#리스트 수정 삭제
# print("#=========#")
# c[0] =4
# print('c의 값은? :', c)
# c[1:2] = ['a','b','c']
# print('c의 값은? :', c)
# c[1] = ['a','b','b']
# print(c)
# c[1:1] = ['a','b','b']
# print(c)
# del c[3]
# print(c)


#리스트 함수
a = [5,2,3,1,4]
print("#=========#")
print('a -',a)
a.append(6)  #6번째 자리에 삽입
print('리스트에 삽입하라 :',a)
a.sort()
print('리스트를 정렬하라 :',a)
a.reverse()
print('리스트를 역순하라 :',a)
print('리스트의 4번째를 가져와라 :', a.index(4))
print('리스트의 1값은 몇개? :', a.count(1) ,'ea')
a.remove(2)
print('리스트에서 2를 지우고 출력하라 :',a)
print('리스트의 끝의 값을 지워라 :', a.pop())
print('리스트의 끝의 값이 지워지고 나머지는? :', a)
ex = [8,9]
a.extend(ex)
print('ex값을 extend하라 :',a)  # extend 함수를 통해 추가할 수도 있다.


#리스트 삭제 : del(인덱스번호로 지정해서 삭제) , remove(값을 지정해서 삭제) , pop(끝의 부분을 삭제)
while a:
    l = a.pop()
    print(l is 4)
