# KFUEIT Latest News Crawler

from urllib.request import urlopen
url = 'https://www.kfueit.edu.pk/'
response = urlopen(url)
html = response.read()

from bs4 import BeautifulSoup as Soup
source_code = Soup(html, 'html.parser')
for h3 in source_code.find_all('h3'):
    a = h3.parent
    news_link = (a['href'])
    response = urlopen(news_link)
    news_data = Soup(response.read(), 'html.parser')
    title = news_data.title.text
    path = "D:/" + title + ".txt"
    print(path)
    f = open(path, 'w', encoding='utf-8')
    f.write(news_data.get_text())
    f.close()
