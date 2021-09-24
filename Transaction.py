import uuid
import time


class Transaction:

    def __init__(self, senderpublickey, recieverpublickey, amount, type):
        self.senderpublickey = senderpublickey
        self.recieverpublickey = recieverpublickey
        self.amount = amount
        self.type = type
        self.id = uuid.uuid1().hex
        self.timestamp = time.time()
        self.signature = ''

    def toJson(self):
        return self.__dict__
