import simplejson as json

#dict(json 선언)

data = {}
data['people'] = []
data['people'].append({
    'name' :'kim',
    'website' :'naver.com',
    'from' : 'seoul',
    'grade' : [95,77,89,91]
    })
data['people'].append({
    'name' :'park',
    'website' :'google.com',
    'from' : 'busan',
    'grade' : [65,27,79,31]
    })
data['people'].append({
    'name' : 'Lee',
    'website' :'daum.net',
    'from' : 'incheon',
    'grade' : [45,87,22,100]
    })

#print(data)

#json 파일쓰기(dump)

with open('/Users/jeongho/Documents/section4/member_2.json', 'w') as outfile:
    json.dump(data,outfile)

with open('/Users/jeongho/Documents/section4/member_2.json', 'r') as infile:
    r = json.load(infile)
    print(r)
    print("=======================")
    for p in r['people']:
        print('Name: ' + p['name'])
        print('Website: ' + p['website'])
        print('From: ' + p['from'])
        t = p['grade']
        grade = ''
        for g in t:
            grade = grade + ' ' +str(g)
        print('Grade: ',grade.lstrip())
        print('')
