# urlparse 与 urlunparse 两种解析


import urllib.request
from urllib.parse import urlparse, urlunparse

result = urlparse("http://www.baidu.com/index.html;user?id=5#comment")

# print(type(result), result)

# print(result.scheme)

data = []
for i in result:
    data.append(i)

print(data)

print(urlunparse(data))

response = urllib.request.urlopen(urlunparse(data))

print(response.read().decode())
