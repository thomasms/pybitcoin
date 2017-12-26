from util.utils import getresponse


def currentprice(currency='USD'):
    url = 'https://blockchain.info/ticker'
    data = getresponse(url)
    price = data[currency]['last']
    return float(price)

