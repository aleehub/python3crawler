import urllib.request


# urlopen 无传参  基本采用GET方法提交
response = urllib.request.urlopen('https://kyfw.12306.cn/otn/leftTicket/queryT?leftTicketDTO.train_date=2019-10-01&leftTicketDTO.from_station=SZQ&leftTicketDTO.to_station=WCN&purpose_codes=ADULT')

print(type(response))
# <class 'http.client.HTTPResponse'>

# HTTPResponse对象:
#   attribution:
#       msg, 响应消息
print('response.msg:', response.msg)
#       version, 版本号
print('response.version:', response.version)
#       status, 状态码
print('response.status:', response.status)
#       reason,  响应状态
print('response.reason:', response.reason)
#       debuglevel,
print('response.debuglevel:', response.debuglevel)
#       closed
print('response.closed:', response.closed)


#   method:
#       read(),
print(response.read().decode())
#       readinto(),
#       getheader(name),   获取响应
#       getheaders(),    获取响应头信息
# print(response.getheaders())
# for i in response.getheaders():
#
#     for j in i:
#         print(j, end=':')
#     print()

#       fileno()    暂时无此方法
# print(response.fileno())







