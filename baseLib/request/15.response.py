import requests

headers = {
'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36'
}

r= requests.get('http://www.jianshu.com', headers=headers)

print(type(r.status_code), r.status_code)

print(type(r.headers), r.headers)

print(type(r.cookies), r.cookies)

print(type(r.url), r.url)

print(type(r.history), r.history)

print(requests.codes.ok)