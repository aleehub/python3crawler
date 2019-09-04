import requests

r = requests.get('http://httpbin.org/get')
print(type(r.text))
print(r.text)
print(type(r.json()))
print(r.json())
