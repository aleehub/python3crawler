import requests

data = {'name': 'germany', 'age': '22'}
headers = {
'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36'
}
r  = requests.post('http://httpbin.org/post', data=data,headers=headers)

print(r.text)
print(r.history)