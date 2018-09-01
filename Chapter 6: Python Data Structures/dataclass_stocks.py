from dataclasses import make_dataclass, dataclass

# using make_dataclass
Stock = make_dataclass("Stock", ["symbol", "current", "high", "low"])
stock = Stock("FB", 177.46, high=178.67, low=175.79)


# compared to regular object
class StockRegClass:
    def __init__(self, name, current, high, low):
        self.name = name
        self.current = current
        self.high = high
        self.low = low


stock_reg_class = StockRegClass("FB", 177.46, high=178.67, low=175.79)


# using dataclass decorator
@dataclass
class StockDecorated:
    name: str
    current: float
    high: float
    low: float


stock_decorated = StockDecorated("FB", 177.46, high=178.67, low=175.79)


@dataclass
class StockDefaults:
    name: str
    current: float = 0.0
    high: float = 0.0
    low: float = 0.0


stock_defaults = StockDefaults("FB")


@dataclass(order=True)
class StockOrdered:
    name: str
    current: float = 0.0
    high: float = 0.0
    low: float = 0.0


stock_ordered1 = StockOrdered("FB", 177.46, high=178.67, low=175.79)
stock_ordered2 = StockOrdered("FB")
stock_ordered3 = StockOrdered("FB", 178.42, high=179.28, low=176.39)
