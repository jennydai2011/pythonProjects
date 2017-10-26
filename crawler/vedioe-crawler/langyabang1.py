import urllib.request
import re
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup

#req = Request('https://www.viki.com/tv/22943c-nirvana-in-fire#modal-episode', headers={'User-Agent': 'Mozilla/5.0'})
#webpage = urlopen(req).read()

BASE_URL = 'https://www.viki.com/tv/22943c-nirvana-in-fire#modal-episode'
VEDIO_LINK_PATTERN = 'href="(\/videos\/.*nirvana-in-fire-episode-.*)"'

req = urllib.request.Request(BASE_URL, headers={'User-Agent': 'Mozilla/5.0'})
html = urllib.request.urlopen(req)
doc = html.read().decode('utf8')
# print(doc)
url_list = list(set(re.findall(VEDIO_LINK_PATTERN, doc)))
print(url_list)


#beautifulsoup - get video link
