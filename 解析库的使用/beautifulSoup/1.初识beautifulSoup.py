from bs4 import BeautifulSoup

# 初始化成html对象 并且自动补全缺失标签
soup = BeautifulSoup('<p>Hello</p>', 'lxml')


# 整个beautifulSoup对象
print(type(soup), soup)
# <html><body><p>Hello</p></body></html>
# 元素标签对象
print(type(soup.p), soup.p)
# <p>Hello</p>

# 元素导航字符串
print(type(soup.p.string), soup.p.string)
# Hello

