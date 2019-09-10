import csv
# 引入csv库

with open('data.csv', 'w') as csvfile:

    # 列表的写入方式

    # 初始化写入对象，传入该键柄
    # 利用delimiter 可以修改列与列之间的分隔符
    writer = csv.writer(csvfile, delimiter='*')
    writer.writerow(['id', 'name', 'age'])

    writer.writerow(['10001', 'mike', '18'])
    writer.writerows(['10001', 'mike', '18'])
    # writer.writerows([['10001', 'mike', '18'],['10001', 'mike', '18'],['10001', 'mike', '18']])


with open('data2.csv', 'w', encoding='utf8') as csvfile:
    # 将字典保存在csv文件中
    # 先定义头部字段
    fieldnames = ['id', 'name', 'age']

    # 利用DicWriter 初始化一个字典写入对象
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    # 先写入头部信息
    writer.writeheader()
    writer.writerow({'id': "10001", 'name': '杨超越', 'age': "alee"})


# 读取

with open('data2.csv', 'r', encoding='utf8') as csvfile:
    reader = csv.reader(csvfile)
    print(type(reader))
    print(reader)
    for row in reader:
        print(type(row))
        # <class 'list'>
        print(row)
        # ['10001', '杨超越', 'alee']
