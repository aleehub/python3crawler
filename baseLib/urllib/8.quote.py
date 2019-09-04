# 内容转换成为URL格式

from urllib.parse import quote, unquote

keyword = '壁纸'
url = 'http://www.baidu.com/s?wd=' + quote(keyword)

print(url)

print(unquote(url))