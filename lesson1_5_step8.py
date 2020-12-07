class MoneyBox:
    def __init__(self, capacity=0):
        self.capacity = capacity
        self.count = 0

    def can_add(self, v):
        return v <= self.capacity

    def add(self, v):
        if self.can_add(v):
            self.count += v
            self.capacity -= v
            print(f'limit: {self.capacity}, in box: {self.count}')


x = MoneyBox(10)
print(x.can_add(5))
x.add(5)
print(x.can_add(7))
x.add(7)