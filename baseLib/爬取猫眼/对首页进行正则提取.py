import re

import requests

# 影片排名
pattern1 = re.compile('<dd>.*?board-index.*?>(.*?)</i>', re.S)

print(pattern1)

# 图片地址
pattern2 = re.compile('data-src="(.*?)"', re.S)

# 电影名字
pattern3 = re.compile('class="name".*?data-act.*?>(.*?)</a>', re.S)
# 主演
pattern4 = re.compile('主演：(.*?)</p>', re.S)
# 上映时间
pattern5 = re.compile('上映时间：(.*?)</p>', re.S)
# 分数
pattern6 = re.compile('class="score".*?integer">(.*?)</i>.*?fraction">(.*?)</i>')

# 汇总
pattern = re.compile(
    '<dd>.*?board-index.*?>(.*?)</i>.*?data-src="(.*?)".*?class="name".*?data-act.*?>(.*?)</a>.*?主演：(.*?)</p>.*?上映时间：(.*?)</p>.*?class="score".*?interger">(.*?)</i>.*?fraction">(.*?)</i>',
    re.S)