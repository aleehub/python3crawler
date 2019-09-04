import urllib.request
import urllib.parse




# urlopen(url,

# data=None,
# byte类型字节流参数，用到byte()方法，参数为字符串 和编码格式 ，字符串用urlencode方法将字典转换成字符串
data = bytes(urllib.parse.urlencode({'word': 'hello'}), encoding='utf-8')
response1 = urllib.request.urlopen('http://httpbin.org/post', data=data)
# print(response1.read().decode())


# timeout=socket._GLOBAL_DEFAULT_TIMEOUT,*,
# 超时时间，单位为秒，超过设定时间仍然没有响应则会抛出异常，不指定则会采用全局默认时间
response2 = urllib.request.urlopen('http://httpbin.org/get', timeout=0.1)
# print(response2.read().decode())
# 可以利用超时设置来控制网页如果长时间未响应，就跳过抓取，利用try except语句来实现：
import socket
import urllib.error

try:
    response = urllib.request.urlopen('http://httpbin.org/get', timeout=0.1)
except urllib.error.URLError as e:
    if isinstance(e.reason, socket.timeout):
        print('TIME OUT')


# cafile=None,      指定CA证书
# capath=None,      CA证书路径，以上两个证书在请求https链接才有用
# cadefault=False,  已弃用
# context=None      ssl.SSLContext类型，指定SSL设置
# )


