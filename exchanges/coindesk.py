from util.utils import getdata


BASE_URL_API='https://api.coindesk.com/v1/bpi'


def currentprice(currency='USD'):
    data = getdata(str.format('{0}/currentprice/{1}.json',
                              BASE_URL_API,
                              currency
                              )
                   )
    price = data['bpi'][currency]['rate_float']
    return float(price)


def pastprice(date, currency='USD'):
    data = getdata(str.format('{0}/historical/close.json?currency={1}&start={2}&end={3}',
                              BASE_URL_API,
                              currency,
                              date,
                              date
                              )
                   )
    price = data['bpi'][date]
    return float(price)


