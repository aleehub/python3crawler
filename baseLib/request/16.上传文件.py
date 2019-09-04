import requests

files = {
    'file': open('favicon.ico', 'rb')
}

r = requests.post('http://www.httpbin.org/post', files=files)

print(r.text)