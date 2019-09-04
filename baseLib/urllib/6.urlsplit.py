from urllib.parse import urlsplit, urlunsplit


# 为一个元祖，可以通过两种方式来获取值，索引和属性
result = urlsplit("http://www.baidu.com/s?wd=alee")

print(result)

data = []
for i in result:
    data.append(i)


result2 = urlunsplit(data)
print(result2)


