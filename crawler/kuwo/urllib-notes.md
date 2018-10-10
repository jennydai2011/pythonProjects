```
import urllib.request #python3 way
song_url = "http://www.kuwo.cn/yinyue/7033256/"
response = urllib.request.urlopen(song_url)

print(response.read().decode('utf-8'))

```
