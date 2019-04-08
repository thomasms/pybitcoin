from pybitcoin.util.utils import getdata


BASE_URL_API='https://cryptomate.co.uk/api/all/'
NAME = "cryptomate"

def currentprice(currency='USD'):
    data = getdata(str.format('{0}/{1}',
                              BASE_URL_API,
                              currency
                              )
                   )
    price = data['BTC']['price']
    return float(price)
