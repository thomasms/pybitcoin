from util.utils import getdata


BASE_URL_API='https://blockchain.info/ticker'


def currentprice(currency='USD'):
    price = getdata(BASE_URL_API)[currency]['last']
    return float(price)


def currentprice15m(currency='USD'):
    price = getdata(BASE_URL_API)[currency]['15m']
    return float(price)


def currentbuyselldiff(currency='USD'):
    data = getdata(BASE_URL_API)
    price = data[currency]['buy'] - data[currency]['sell']
    return float(price)

