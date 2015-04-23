title: "Python Web"
date: 2015-04-23 17:29:00
tags:
---

There is an issue that our pyramid based website is so slowly, and the connection is always blocked whenever the client counts rise. It's started by [pserve](https://github.com/Pylons/pyramid/blob/master/pyramid/scripts/pserve.py), a script file inside pyramid project, and the configure file here:
```
[server:main]
use = egg:waitress#main
host = 0.0.0.0
port = xxx
```
The web server of it used is [waitress](http://waitress.readthedocs.org/en/latest/) [Github](https://github.com/Pylons/waitress) [The arguments](http://waitress.readthedocs.org/en/latest/arguments.html)

Waitress is a WSGI server. Here is the wikipedia page of [Web Server Gateway Interface](http://en.wikipedia.org/wiki/Web_Server_Gateway_Interface), and here is the official portal: [PIP3333](http://legacy.python.org/dev/peps/pep-3333/). Here are some tutorial [简介](http://wiki.woodpecker.org.cn/moin/WSGI)、[wsgi.org](http://wsgi.readthedocs.org/en/latest/)
