import urllib2
import json
import sys

MAX = 0.02
MIN = 0.000005
RULE = 0.1


def get_raw(flag, price, source):
    raw_list = []
    sum_btc = 0
    sum_product = 0
    for x in source:
        cur_price    = float(x[0])
        cur_source   = x[1]
        if 'bids' == flag:
            cur_btc      = cur_price * cur_source
            cur_product  = cur_btc / price
        else:
            cur_product  = cur_source
            cur_btc      = price * cur_product
        sum_btc     += cur_btc
        sum_product += cur_product
        raw_list.append([cur_price, cur_source, cur_btc, sum_btc, cur_product, sum_product])
    return raw_list

def remove_fate(dlist):
    raw_sum = dlist[-1][3]
    print raw_sum
    cur_sum = 0
    for d in dlist:
        if d[2] > raw_sum * MAX:
            d.append(d[2] * -0.01 - 2)
            d.append(cur_sum)
            continue
        cur_sum += d[2]
        d.append(d[2])
        d.append(cur_sum)

def mark_robot(dlist):
    trust_sum = dlist[-1][6]
    for d in dlist:
        if d[2] < trust_sum * MIN:
            d[6] *= -1

def add_count(price, dlist):
    delta_sum   = 0
    delta_count = 0

    delta_price = price * RULE 
    for d in dlist:
        if abs(d[0] - price) > delta_price:
            break
        if d[6] < 0:
            continue
        delta_count += 1
        delta_sum   += d[6]

    avg_price = delta_sum /delta_count

    count = 0
    for d in dlist:
        count += 1
        d.append(delta_sum * count / delta_count)
        d.append(avg_price if d[6] >= 0 else d[6])



crypto = sys.argv[1]
flag = 'BTC_%s' %(crypto.upper())

src = urllib2.urlopen('https://poloniex.com/public?command=returnTicker')
dt  = src.read()
src.close()

dct = json.loads(dt)
price = float(dct[flag]['last'])

src = urllib2.urlopen('https://poloniex.com/public?command=returnOrderBook&currencyPair=%s&depth=100000' %flag)
dt  = src.read()
src.close()

dct = json.loads(dt)

bids = get_raw('bids', price, dct['bids'])
asks = get_raw('asks', price, dct['asks'])
remove_fate(bids)
remove_fate(asks)
mark_robot(bids)
mark_robot(asks)
add_count(price, bids)
add_count(price, asks)

bids.reverse()
real_list = bids + asks

range = 0.1
while range <= 10:
    hdlr = open('/tmp/%s%s' %(crypto, int(range*100 + 0.1)), 'w')
    for x in real_list:
        if x[0] <= price * (1 - range) or x[0] >= price * (1 + range):
            continue
        hdlr.write('\t'.join(str(y) for y in x) + '\n')
    hdlr.close()
    range += 0.1
