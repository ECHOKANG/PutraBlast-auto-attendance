import requests
from bs4 import BeautifulSoup

url = 'https://upm-id-portal.upm.edu.my/sso/login?service=http%3A%2F%2Flearninghub.upm.edu.my%2Fblastdk%2Flogin%2Findex.php'
headers = {'User-Agent': ''}
data = {'username': '',
'password': '',
'lt': '',
'execution': '',
'submit': 'LOGIN',
}
res = requests.post(url,headers=headers,data=data)

soup = BeautifulSoup(res.text,'lxml')
print(res.status_code)
print(type(res))
#未完成，项目持续更新中