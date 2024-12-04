from enum import Enum
from typing import Optional, List, Dict, Union

class OrderSide(Enum):
    BUY = 'buy'
    SELL = 'sell'

class OrderType(Enum):
    MARKET = 'market'
    LIMIT = 'limit'

class OrderStatus(Enum):
    OPEN = "open"
    CLOSED = "closed"
    CANCELED = "canceled"
    EXPIRED = "expired"
    REJECTED = "rejected"
    UNKNOWN = "unknown"

class Order:
    def __init__(
        self,
        identifier: str,
        status: OrderStatus,
        order_type: OrderType,
        side: OrderSide,
        price: float,
        average: Optional[float],
        amount: float,
        filled: float,
        remaining: float,
        timestamp: int,
        datetime: Optional[str],
        last_trade_timestamp: Optional[int],
        symbol: str,
        time_in_force: Optional[str],
        trades: Optional[List[Dict[str, Union[str, float]]]] = None,
        fee: Optional[Dict[str, Union[str, float]]] = None,
        cost: Optional[float] = None,
        info: Optional[Dict[str, Union[str, float, dict]]] = None
    ):
        self.identifier = identifier
        self.status = status
        self.order_type = order_type
        self.side = side
        self.price = price
        self.average = average
        self.amount = amount
        self.filled = filled
        self.remaining = remaining
        self.timestamp = timestamp
        self.datetime = datetime
        self.last_trade_timestamp = last_trade_timestamp
        self.symbol = symbol
        self.time_in_force = time_in_force
        self.trades = trades
        self.fee = fee
        self.cost = cost
        self.info = info  # Original unparsed structure for debugging or auditing

    def is_filled(self) -> bool:
        return self.status == OrderStatus.CLOSED

    def is_canceled(self) -> bool:
        return self.status == OrderStatus.CANCELED

    def is_open(self) -> bool:
        return self.status == OrderStatus.OPEN

    def __str__(self) -> str:
        return (
            f"Order(id={self.identifier}, status={self.status}, "
            f"type={self.order_type}, side={self.side}, price={self.price}, average={self.average}, "
            f"amount={self.amount}, filled={self.filled}, remaining={self.remaining}, "
            f"timestamp={self.timestamp}, datetime={self.datetime}, symbol={self.symbol}, "
            f"time_in_force={self.time_in_force}, trades={self.trades}, fee={self.fee}, cost={self.cost})"
        )


    def __repr__(self) -> str:
        return self.__str__()