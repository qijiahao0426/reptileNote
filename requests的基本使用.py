import requests
url="https://www.baidu.com/"
response=requests.get(url)
response.encoding="utf-8"

print(response.text)
print(response.content)
print(response.content.decode('utf-8'))
print(response.headers)
print(response.status_code)
print(response.url)
print(response.request.headers)