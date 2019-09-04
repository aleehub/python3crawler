# 操作cookies, 处理代理设置的
import http.cookiejar, urllib.request

cookie = http.cookiejar.CookieJar()

handler = urllib.request.HTTPCookieProcessor(cookie)

openner = urllib.request.build_opener(handler)

response = openner.open('http://www.baidu.com')



for item in cookie:
    print(item.name+":"+item.value)