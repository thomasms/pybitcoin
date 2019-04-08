from pybitcoin.util.utils import getdata


BASE_URL_API='https://bitbay.net/API/Public/'
NAME = "bitbay"

def currentprice(currency='USD'):
    data = getdata(str.format('{0}/BTC/{1}/ticker.json',
                              BASE_URL_API,
                              currency
                              )
                   )
    price = data['last']
    return float(price)
