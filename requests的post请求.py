import requests

langdetect_url = "http://fanyi.baidu.com/langdetect"
url='https://fanyi.baidu.com/v2transapi'

headers={
    'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36',
}


data={
    "from": "zh",
    "to": "en",
    "query": "你好",
    "simple_means_flag": "3",
    "sign": 232427.485594,
    "token": "9093238bb1474b8e6dbe431e963ab124",
    "transtype": "translang",
}

langdetect_resp = requests.post(langdetect_url, headers=headers, data={'query': '你好'})
code=langdetect_resp.status_code
print(code)

res=requests.post(url=url,headers=headers,data=data)

code=res.status_code
print(code)
if code==200:
    print('成功')
    data=res.json()
    print(data)
    # if data['err_no']==0:
    #     print('响应成功')
    #     print(data['data']['cands'])