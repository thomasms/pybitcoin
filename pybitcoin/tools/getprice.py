import pybitcoin.exchanges.coindesk as cd
import pybitcoin.exchanges.blockchain as bc

currency='GBP'

exchanges = [cd, bc]

for e in exchanges:
    print("Exchange: {0} - Price {1} ({2})".
          format(e, e.currentprice(currency=currency), currency))
