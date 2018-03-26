
import requests
from bs4 import BeautifulSoup
from urllib.request import urlopen

headers = {
  'User-Agent': 'Mozilla/5.0 (iPad; CPU OS 11_0 like Mac OS X) AppleWebKit/604.1.34 (KHTML, like Gecko) Version/11.0 Mobile/15A5341f Safari/604.1'
}#讓程式比較擬人一點，不易被隔離
res = requests.get('https://www.ptt.cc/bbs/ToS/M.1429859812.A.30E.html', headers=headers)

#print(res.text)
#html.parser是剖析器
soup = BeautifulSoup(res.text,'html.parser')
images = soup.select('a[href^=http://i.imgur]')

#print(images)

for image in images:
  print(image['href'])
  filename = image['href'].split('/')[3]#取得第三段名稱
  img = urlopen(image['href'])
  with open('./images/' + str(filename),'wb') as f:
    f.write(img.read())

