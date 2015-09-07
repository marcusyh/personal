from htmldom import htmldom
from urllib.request import urlopen
conn = urlopen("http://coinmarketcap.com/currencies/views/all/")
html = conn.read()
conn.close()

dom = htmldom.HtmlDom(html)
dom = dom.createDom(html)
