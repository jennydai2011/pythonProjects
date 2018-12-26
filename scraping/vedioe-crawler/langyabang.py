#!"C:\Python362\python.exe"
import requests
import re
from bs4 import BeautifulSoup

BASE_URL = 'https://www.viki.com'
#main_url = 'https://www.youtube.com/watch?v=X337arDKgJg&list=PLkvG4EWPDB0kksjgUyEevqsvkDiJUYwpz'
main_url = BASE_URL+'/tv/22943c-nirvana-in-fire#modal-episode'
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}

#resp = requests.get(main_url)
resp = requests.get(main_url, headers=headers)
#没有下面这行，打印的结果中文是乱码
# resp.encoding = 'utf-8'
#html = resp.text
html = resp.content.decode()
#print(html)

link = re.findall(r'href="(\/videos\/.*?)"', html)[0]
#print(link)
print(BASE_URL+link)
print('下载页面')
#https://www.viki.com/videos/1080865v-nirvana-in-fire-episode-1

# #for di in link:
dest_resp = requests.get(BASE_URL+link, headers=headers)
#视频是二进制数据流，content就是为了获取二进制数据的方法
data = dest_resp.content
#print(data)
#<video id="video-player_Shaka_api" class="vjs-tech" preload="none" src="blob:https://www.viki.com/e7d2ad2e-69bb-420a-abde-4333efab3fc4"></video>
soup = BeautifulSoup(data, "html.parser")
dra = soup.findAll('video', attrs={'class':'vjs-tech'})
print(dra)
#保存数据的路径及文件名

# # path = 'C:\\tmp\\tv\\langyabang1.mp4'
# # f = open(path, 'wb')
# # f.write(data)
# # f.close()
# print('下载完成')

# soup = BeautifulSoup(html, "html.parser")
# #dramaList = soup.findAll('img', attrs={'id':'img'})
# #dramaList = soup.findAll('yt-img-shadow')
# dramaList = soup.findAll('div', attrs={'class':'thumbnail-description'})


# for di in dramaList:
#     diDiva = di.findAll('a')
#     print(diDiva[0])    
    
#     #url=diDiv[0].find('a')['href']
#     #print(url)


# #print(dramaList)

