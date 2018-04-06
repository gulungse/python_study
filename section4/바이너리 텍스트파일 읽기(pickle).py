import pickle #객체,텍스트 직렬화, 역직렬화

#변수 선언 ( 파일 이름과 데이터 )
bfilename = '/Users/jeongho/Documents/section4/test.bin'
tfilename = '/Users/jeongho/Documents/section4/test.txt'

data1 = 77
data2 = "Hello, world!"
data3 = ["car","apple","house"]

with open(bfilename, 'wb') as f:
    pickle.dump(data1,f)
    pickle.dump(data2,f)
    pickle.dump(data3,f)


with open(tfilename, 'wt') as f:
    f.write(str(data1))
    f.write('\n')
    f.write(data2)
    f.write('\n')
    f.writelines('\n'.join(data3))

#바이너리 읽기
with open(bfilename, 'rb') as f:
    b = pickle.load(f)
    print(type(b), 'Binary Read1  |  ',b)
    b = pickle.load(f)
    print(type(b), 'Binary Read1  |  ',b)
    b = pickle.load(f)
    print(type(b), 'Binary Read1  |  ',b)

#텍스트 일기
with open(tfilename, 'rt') as f:
    for i, line in enumerate(f,1):
        print(type(line), 'Text Read' + str(i) + ' | ',line,end='')
        
