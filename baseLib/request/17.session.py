import requests

requests.get('http://httpbin.org/cookies/set/number/123456798')
r = requests.get('http://httpbin.org/cookies')
print(r.text)

s = requests.Session()

s.get('http://httpbin.org/cookies/set/number/123456789')
r = s.get('http://httpbin.org/cookies')
print(r.text)