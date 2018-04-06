from urllib.parse import urljoin
# urljoin 은 절대경로를 치환할때 사용하기 유용
baseUrl = "http://www.test.com/html/a.html"

print(">>", urljoin(baseUrl, "b.html"))
