
# coding: utf-8

from bs4 import BeautifulSoup

import urllib.request
resp=urllib.request.urlopen('https://www.douban.com/explore/')
content=resp.read()
soup = BeautifulSoup(content,'html.parser')

lis = soup.find("ul", class_="side-columns").find_all('li')
columnslist = []
for li in lis:
    columnslist.append(li.a['href'])

columnslist

resp=urllib.request.urlopen('https://www.douban.com/explore/column/5')
content=resp.read()
soup = BeautifulSoup(content,'html.parser')

articles = soup.find_all("div",class_="title")
articlelist = []
for article in articles:
    print(article.a['href'])

resp=urllib.request.urlopen('https://www.douban.com/note/622891788/')
content=resp.read()
soup = BeautifulSoup(content,'html.parser')

comments = soup.select('div[class="content report-comment"]')
for comment in comments:
    print(comment.a.string)
    print(comment.p.string)
    print('\b')

