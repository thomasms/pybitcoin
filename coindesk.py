from utils import getresponse


def currentprice(currency='USD'):
    url = 'https://api.coindesk.com/v1/bpi/currentprice/{}.json'.format(currency)
    data = getresponse(url)
    price = data['bpi'][currency]['rate_float']
    return float(price)

print(currentprice())
