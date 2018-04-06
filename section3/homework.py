import sys
import io
import requests, json

#Rest : PUT , POST , GET , DELETE

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

r = requests.get('http://developer.wordpress.com')
print(r.text)
