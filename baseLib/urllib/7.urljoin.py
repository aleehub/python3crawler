# 利用urljoin 构成新的链接

# base
from urllib.parse import urljoin, urlparse, parse_qs

#
# result = urljoin('www.baidu.com', '?id=1')
#
# print(result)


# request = input("url:")

request = "www.baidu.com/?user=12&id=152"

result = urlparse(request)

print(result)

query = result.query

dict = {}

list=query.split("&")
for i in list:
    list2 = i.split("=")

    dict[list2[0]] = list2[1]

print(dict)

hh = parse_qs(query)

print(hh)
