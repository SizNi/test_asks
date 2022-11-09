# возврат нового счетчика, создаваемого внутри класса
class Counter:
    def __init__(self, value=0):
        self.value = value

    def inc(self, delta=1):
        return Counter(max(self.value + delta, 0))

    def dec(self, delta=1):
        return self.inc(-delta)

# возврат значения изменяющегося счетчика в классе


class Counter_1:
    value = 0

    def inc(self, delta=1):
        self.value = max(self.value + delta, 0)

    def dec(self, delta=1):
        self.inc(-delta)

c = Counter()
c.inc().value
c.dec().value
c.inc().inc(5).value
c.inc().inc(5).dec(2).value


