import simplejson as json

#dict(json 선언)
data = {}
data['people'] = []
data['people'].append({
    'name' :'kim',
    'website' :'naver.com',
    'from' : 'seoul'
    })
data['people'].append({
    'name' :'park',
    'website' :'google.com',
    'from' : 'busan'
    })
data['people'].append({
    'name' : 'Lee',
    'website' :'daum.net',
    'from' : 'incheon'
    })

#print(data)

#Dict(json) - > str

e = json.dumps(data, indent=2)  # dumps 를 사용해서 딕셔너리에서 문자열로 변환 / indent : depth 들여쓰기등의 깊이를 정리해줌.
#print('형태는 :',type(e))
#print(e)

d = json.loads(e)
#print('형태는 :',type(d))
#print(d)

with open('/Users/jeongho/Documents/section4/member.json','w') as outfile:
    outfile.write(e)

with open('/Users/jeongho/Documents/section4/member.json','r') as infile:
    r = json.loads(infile.read())
    #print("=============")
    #print(r)
    for p in r['people']:
        print('Name :' + p['name'])
        print('Website :' + p['website'])
        print('From :' + p['from'])
        print("")
        
