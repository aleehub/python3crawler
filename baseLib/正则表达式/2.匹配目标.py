import re

content = 'hello 123456789 world_this is a regex demo'

result = re.match('^(hello)\s(\d+)\s(world)', content)

print(result)

print(result.group())

print(result.group(2))

# 就查询目标组成成元组返回
print(result.groups())

print(result.span())