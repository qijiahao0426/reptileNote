import requests
# url="https://www.lmonkey.com/"
url="https://www.xicidaili.com/nn/" #503 拒绝请求
headers={
'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36'
}
res=requests.get(url=url,headers=headers)

code=res.status_code

print(code)

if code==200:
    with open('./test.html','w') as fp:
        fp.write(res.text)