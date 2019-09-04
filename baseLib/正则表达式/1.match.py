import re


content = 'hello 123 4567 World_This is a regex Demo'

print(len(content))

result = re.match('^hello\s\d\d\d\s\d{4}\s\w{10}',content)

print(result)
# <_sre.SRE_Match object; span=(0, 25), match='hello 123 4567 World_This'>

# 输出匹配内容
print(result.group())
# hello 123 4567 World_This

# 输出匹配的范围
print(result.span())
# (0, 25)



