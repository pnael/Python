import requests

url = 'https://www.owenscorning.com/en-us'
myobj = {'somekey': 'somevalue'}

x = requests.post(url, data = myobj)
print(x.url)
print(x.encoding)
print(x.headers)
print(x.text)