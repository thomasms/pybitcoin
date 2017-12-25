import quandl
import matplotlib.pyplot as plt
import matplotlib.dates as md
import datetime as dt
import time

data_sets = [
    ('BCHARTS/LOCALBTCUSD', 'k'),
    ('BCHARTS/MTGOXUSD', 'g--'),
    ('BCHARTS/BITBOXUSD', 'r-')
]

def get_price(data, price_key='Open'):
    price = data[price_key].tolist()
    dates = [dt.datetime.fromtimestamp(ts.timestamp()) \
             for ts in data.index.tolist()]
    datenums = md.date2num(dates)

    return datenums, price


for d in data_sets:
    data = quandl.get(d[0]).dropna()
    dates, prices = get_price(data)
    plt.plot(dates, prices, d[1], label=d[0])

# plot formatting
plt.subplots_adjust(bottom=0.2)
plt.xticks(rotation=25)
ax = plt.gca()
xfmt = md.DateFormatter('%d-%m-%Y')
ax.xaxis.set_major_formatter(xfmt)
plt.legend()
plt.grid(True)
plt.yscale('log')
plt.show()
