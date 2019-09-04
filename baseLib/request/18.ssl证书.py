import requests
import time
begin = time.time()


response = requests.get('https://www.12306.cn')

    # print(response.status_code)

end = time.time()
print(end-begin, ":")