from bs4 import BeautifulSoup

import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')


html = """
<html>
<body>
<h1>파이썬 BeautifulSoup 공부</h1>
<p>태그 선택자</p>
<p>css 선택자</p>
</body>
</html>
"""
soup = BeautifulSoup(html, 'html.parser')

#print('soup', type(soup))
#print('prettify', soup.prettify())

h1 = soup.html.body.h1
#print('h1', h1)
print('h1의 내용은? :', h1.string)
p1 = soup.html.body.p
print('p1 : ',p1)
p2 = p1.next_sibling.next_sibling
print('p2 :', p2)

print("h1의 내용은 :", h1.string)
print("p1의 내용은 :", p1.string)
print("p2의 내용은 :", p2.string)
