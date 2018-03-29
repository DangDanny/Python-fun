from urllib import request 
from urllib import parse

url = 'https://auth.fun.ac.jp/cgi-bin/Login.cgi'

data = {"uid":"p4617004","pwd":"V8kZecCx"}

headers = {
'Host': 'auth.fun.ac.jp',
'Connection': 'keep-alive',
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36',
'Accept': 'image/webp,image/apng,image/*,*/*;q=0.8',
'Accept-Encoding': 'gzip, deflate, br',
'Accept-Language': 'zh-CN,zh;q=0.9',
}



data = parse.urlencode(data).encode('utf-8')  
req = request.Request(url, headers=headers, data=data)  
page = request.urlopen(req).read()  
page = page.decode('utf-8')
print(page)
