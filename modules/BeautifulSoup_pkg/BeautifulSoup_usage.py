#!/usr/bin/env python
#-*- coding:utf-8 -*-

# 主要是进行python爬虫

#!/usr/bin/env python
#-*- coding:utf-8 -*-


from bs4 import BeautifulSoup


html = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title" name="dromouse"><b>The Dormouse's story</b></p>
<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1"><!-- Elsie --></a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>
<p class="story">...</p>
"""

if __name__ == '__main__':
    soup = BeautifulSoup(html, "html.parser")

    # print(soup.prettify())
    # print(soup.title)
    # print(soup.head)
    # print(soup.a)
    # print(soup.p)
    # print(type(soup.p))     # <class 'bs4.element.Tag'>
    # print(soup.name)        # [document]
    # print(soup.head.name)   # head
    print(soup.p.attrs)     # {'class': ['title'], 'name': 'dromouse'}
    print(soup.p['class'])  # ['title']
    print(soup.p.get('class'))  # ['title']





