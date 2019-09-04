import requests
import re

headers = {
'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36'
}
r = requests.get('http://www.zhihu.com/explore', headers=headers)
print(r.text)
print(r.status_code)

pattern = re.compile('explore-feed.*?question_link.*?>(.*?)</a>', re.S)

titles = re.findall(pattern, r.text)

print(titles)