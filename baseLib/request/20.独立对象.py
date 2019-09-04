from requests import Request, Session


url = 'http://httpbin.org/post'

data = {
    'name': "germany"
}

headers = {
    'User_Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36'
}

s = Session()

req = Request('POST', url, data=data, headers=headers)

prepped = s.prepare_request(req)

r = s.send(prepped)


print(r.text)

# {
#   "args": {},
#   "data": "",
#   "files": {},
#   "form": {
#     "name": "germany"
#   },
#   "headers": {
#     "Accept": "*/*",
#     "Accept-Encoding": "gzip, deflate",
#     "Content-Length": "12",
#     "Content-Type": "application/x-www-form-urlencoded",
#     "Host": "httpbin.org",
#     "User-Agent": "python-requests/2.22.0,Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36"
#   },
#   "json": null,
#   "origin": "113.92.159.175, 113.92.159.175",
#   "url": "https://httpbin.org/post"
# }