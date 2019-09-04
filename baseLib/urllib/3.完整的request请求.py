
# 利用urlopen可以实现最基本的请求，但是不足以构成完成的请求，要加入Header等信息，就可以利用Request类来构建

import urllib.request

request = urllib.request.Request('http://www.baidu.com')

response = urllib.request.urlopen(request)

print(response.read().decode())

# 利用Request类来配置参数：
# (self, url,                       请求URL
#       data=None,                  如果要传，则传byte(字节流)类型，如果是字典可以用urllib.parse.urlencode()转换
#       headers={},                 请求头，两种方式构造， 通过header参数直接构造，利用实例方法add_header()构造
#                                   添加请求头，最常用的是添加User_Agent来伪装成浏览器
# Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36

#       origin_req_host=None,       请求放的ip地址和host地址
#       unverifiable=False,         请求是否是无法验证的
#       method=None                 指示请求的方法
#       ):


from urllib import request, parse

url = 'http://www.httpbin.org/post'

# 直接构造headers 参数
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36',
    'Host': 'httpbin.org'
}
dict = {
    'name': 'Germey'
}
data = bytes(parse.urlencode(dict),encoding='utf-8')
req = request.Request(url=url, data=data, headers=headers, method='POST')

# 当没有指定headers参数时，则可以用add_header()方法来添加
req.add_header('User-Agent', 'value')

reponse = request.urlopen(req)
print(response.read().decode())

