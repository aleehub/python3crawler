import requests


# proxies = {
#     'http': 'http://10.10.1.10:3128'
# }

r = requests.get('http://172.16.64.1/goform/formWebAuthUserSubmit?userName=python29&userPasswd=qazwsx&userCommand=userAuth')


print(r.status_code)