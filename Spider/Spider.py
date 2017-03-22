import urllib.request
import urllib.parse
from bs4 import BeautifulSoup

url = "http://www.jnujaipur.ac.in"
urls = [url]  #sites to visit
visited = [url]     #visited sites or historic record

while len(urls) > 0:
    try:
        text = urllib.request.urlopen(urls[0]).read()
    except:
       i = 1

    beautifulsoup = BeautifulSoup(text,"lxml")
    print(len(urls))
    urls.pop(0)

    for tag in beautifulsoup.findAll('a',href=True):
        tag['href'] = urllib.parse.urljoin(url,tag['href'])

        if url in tag['href'] and tag['href'] not in visited:
            urls.append(tag['href'])
            visited.append(tag['href'])

for i,j in enumerate(visited):
    print(visited[i])

