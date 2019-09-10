import json


# json 转换前的字符串要是json格式，列表里的最后一个字典后不能有逗号
# 字典内的键值对，要是双引号


str1 = '''[
    {
        "name": "alee",
        "gender": "male",
        "birthday": "1992-10-28"
    },{
        "name": "alee",
        "gender": "male",
        "birthday": "1992-10-28"
    },{
        "name": "alee",
        "gender": "male",
        "birthday": "1992-10-28"
    }
]
'''
#
# print(type(str1))
# data = json.loads(str1)
# print(data)
# print(type(data))

with open('data.json', 'r') as file:

    str1=file.read()
    data = json.loads(str1)
    print(data)
    str2 = json.dumps(data, indent=2)
    print(str2)
    # print(str1)
    # print(type(str1))

