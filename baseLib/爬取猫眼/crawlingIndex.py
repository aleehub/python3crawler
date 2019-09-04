import json
import re

import requests

def get_one_page(url):

    headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36',

    }

    response = requests.get(url, headers=headers)

    if response.status_code == requests.codes.ok:
        return response.text

    return None

def parse_one_page(html):

    pattern = re.compile(
        '<dd>.*?board-index.*?>(.*?)</i>.*?data-src="(.*?)".*?class="name".*?data-act.*?>(.*?)</a>.*?主演：(.*?)</p>.*?上映时间：(.*?)</p>.*?class="score".*?integer">(.*?)</i>.*?fraction">(.*?)</i>',
        re.S)

    items = re.findall(pattern, html)

    for item in items:

        yield {
            'index': item[0],
            'image': item[1],
            'title': item[2].strip(),
            'actor': item[3].strip(),
            'time': item[4],
            'score': item[5]+item[6],
        }

def write_to_file(content):
    with open("result.txt", 'a', encoding='utf8') as f:

        print(type(json.dumps(content)))

        f.write(json.dumps(content, ensure_ascii=False)+"\n")


def main(offset):

    url = 'http://maoyan.com/board/4?offset='+str(offset)

    html = get_one_page(url)

    for item in parse_one_page(html):

        write_to_file(item)


if __name__ == '__main__':

    for i in range(10):

        main(offset=i*10)