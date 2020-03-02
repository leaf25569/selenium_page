import requests

pa={'id':'1002,1003'}
a1=requests.get('http://www.baidu.com',params=pa)
print(a1.url)
print(a1.status_code)


print(a1.content)