import pybitcoin.exchanges.coindesk as cd
import pybitcoin.exchanges.blockchain as bc
import pybitcoin.exchanges.bitbay as bb
import pybitcoin.exchanges.cryptomate as cm

currency='USD'

exchanges = [cd, bc, bb, cm]

for e in exchanges:
    print("Exchange: {0} - Price {1} ({2})".
          format(e.NAME, e.currentprice(currency=currency), currency))
