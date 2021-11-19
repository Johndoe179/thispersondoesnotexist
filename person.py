import requests
from time import sleep

def download(fileName):
    f = open(fileName,'wb')
    f.write(requests.get('https://thispersondoesnotexist.com/image', headers={'User-Agent': 'My User Agent 1.0'}).content)
    f.close()

for i in range(50):
    sleep(0.7)
    download(str(i)+'.jpg')
