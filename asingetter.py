import webbrowser as wb
import requests as r
import bs4
# -*- coding: utf-8 -*-

kw = 'watch'                  #r.form['keyword']
kwl = kw.split(",")
url = 'https://www.amazon.com/s/field-keywords='
d = []

for i in range(len(kwl)):
    for k in range(1,5):
        p = r.get(url + kwl[i] + '&pages=' + str(k))
        pages = bs4.BeautifulSoup(p.text, "html.parser")
        results = pages.select("#s-results-list-atf")
        x = results[0].findAll("li")
        for li in x:
            d.append(li.attrs.get('data-asin'))
    
print(d)
