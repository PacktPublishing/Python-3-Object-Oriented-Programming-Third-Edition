import datetime
from collections import namedtuple


# tuples
def middle(stock, date):
    symbol, current, high, low = stock
    return (((high + low) / 2), date)


mid_value, date = middle(
    ("FB", 177.46, 178.67, 175.79), datetime.date(2014, 10, 31)
)

# namedtuple
Stock = namedtuple("Stock", ["symbol", "current", "high", "low"])
stock = Stock("FB", 177.46, high=178.67, low=175.79)
