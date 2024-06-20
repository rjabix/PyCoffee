from abc import ABC, abstractmethod
from datetime import datetime
from typing import List


class AbstractOrder(ABC):

    @abstractmethod
    def __init__(self, order_id, order_date, ingredients: str):
        self.order_id: int = order_id
        self.order_date: datetime = order_date
        self.ingredients: str = ingredients

    @abstractmethod
    def get_info_text(self) -> tuple:
        ...

    @abstractmethod
    def get_waiting_time(self) -> int:
        ...

    def get_id(self) -> int:
        return self.order_id


# READY
class ReadyOrder(AbstractOrder):

    def __init__(self, order_id, order_date: datetime, order_ready_date: datetime, ingredients: str):
        super().__init__(order_id, order_date, ingredients)
        self.order_ready_date: datetime = order_ready_date

    def get_info_text(self) -> tuple:
        return "Ready", self.order_id, self.order_date, self.order_ready_date

    def get_waiting_time(self) -> int:
        return (self.order_ready_date - self.order_date).seconds


# NOT READY
class NotReadyOrder(AbstractOrder):

    def __init__(self, order_id, order_date, ingredients: str):
        super().__init__(order_id, order_date, ingredients)

    def get_info_text(self) -> tuple:
        return "Not ready", self.order_id, self.order_date

    def get_waiting_time(self) -> int:
        return (self.order_date - datetime.now()).seconds


# FUNCTIONS


orders_list: List[AbstractOrder] = []


def get_average_waiting_time(orders: List[AbstractOrder]) -> dict:
    ready_times = []
    not_ready_times = []

    for order in orders:

        if not isinstance(order, AbstractOrder):
            raise ValueError("Invalid order type")

        match order.get_info_text()[0]:
            case "Ready":
                ready_time = order.get_waiting_time()
                ready_times.append(ready_time)
            case "Not ready":
                not_ready_time = order.get_waiting_time()
                not_ready_times.append(not_ready_time)

    return {"Ready": sum(ready_times) / len(ready_times), "Not ready": sum(not_ready_times) / len(not_ready_times)}


def add_new_order(ingredients: str) -> None:
    order_id = len(orders_list) + 1
    order_date = datetime.now()
    orders_list.append(NotReadyOrder(order_id, order_date, ingredients))


def make_order_ready(index: int, time: datetime = datetime.now()) -> None:
    order = orders_list[index-1]
    orders_list[index-1] = ReadyOrder(order.order_id, order.order_date, time, order.ingredients)
    print(f"Order {orders_list[index-1].ingredients} is ready")
