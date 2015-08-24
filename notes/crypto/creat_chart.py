import urllib2
import json
import sys

flag = 'BTC_%s' %(sys.argv[1].upper())

src = urllib2.urlopen('https://poloniex.com/public?command=returnTicker')
dt  = src.read()
src.close()

dct = json.loads(dt)
price = float(dct[flag]['last'])

src = urllib2.urlopen('https://poloniex.com/public?command=returnOrderBook&currencyPair=%s&depth=100000' %flag)
dt  = src.read()
src.close()

dct = json.loads(dt)

bids = dct['bids']
asks = dct['asks']


bids_real = []
sum_btc = 0
sum_product = 0
for x in bids:
    cur_price = float(x[0])
    cur_want  = x[1]
    cur_btc   = cur_price * cur_want
    cur_product = cur_btc / price
    sum_btc   += cur_btc
    sum_product += cur_product
    bids_real.append([cur_price, cur_btc, sum_btc, cur_product, sum_product])

asks_real = []
sum_btc = 0
sum_product = 0
for x in asks:
    cur_price    = float(x[0])
    cur_product  = x[1]
    cur_btc      = price * cur_product
    sum_btc     += cur_btc
    sum_product += cur_product
    asks_real.append([cur_price, cur_btc, sum_btc, cur_product, sum_product])

bids_real.reverse()
real_list = bids_real + asks_real 

range = 0.1
while range <= 2:
    hdlr = open('/tmp/test%s' %(int(range*100 + 0.1)), 'w')
    for x in real_list:
        if x[0] <= price * (1 - range) or x[0] >= price * (1 + range):
            continue
        hdlr.write('\t'.join(str(y) for y in x) + '\n')
    hdlr.close()
    range += 0.1

