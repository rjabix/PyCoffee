from datetime import datetime

#речі які підуть в бд: предмети, час замовлення, сума замовлення, прибуток
class Order:

    def __init__(self, total, orderTime, *argv):
        self.value: float = total
        self.orderTime: datetime = orderTime

        for item in argv:
