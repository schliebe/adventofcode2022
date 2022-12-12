class Monkey:
    def __init__(self, id, operation_callback, test_callback):
        self.id = id
        self.operation = operation_callback
        self.test = test_callback
        self.monkey_true = self
        self.monkey_false = self
        self.items = []
        self.inspections = 0

    def set_monkeys(self, monkey_true, monkey_false):
        self.monkey_true = monkey_true
        self.monkey_false = monkey_false

    def set_items(self, items):
        self.items = items

    def catch_item(self, item):
        self.items.append(item)

    def run_turn(self):
        while len(self.items) > 0:
            item = self.items.pop(0)
            self.inspections += 1
            item = self.operation(item)
            # Day 11 - Part 1 (use the following line)
            # item = item // 3
            # Day 11 - Part 2 (use the following line)
            item = item % 9699690  # Multiplied value of all possible dividers
            if self.test(item):
                self.monkey_true.catch_item(item)
            else:
                self.monkey_false.catch_item(item)


m0 = Monkey(0, lambda x: x * 19, lambda x: x % 17 == 0)
m1 = Monkey(1, lambda x: x + 2, lambda x: x % 19 == 0)
m2 = Monkey(2, lambda x: x + 7, lambda x: x % 7 == 0)
m3 = Monkey(3, lambda x: x + 1, lambda x: x % 11 == 0)
m4 = Monkey(4, lambda x: x * 5, lambda x: x % 13 == 0)
m5 = Monkey(5, lambda x: x + 5, lambda x: x % 3 == 0)
m6 = Monkey(6, lambda x: x * x, lambda x: x % 5 == 0)
m7 = Monkey(7, lambda x: x + 3, lambda x: x % 2 == 0)
m0.set_monkeys(m2, m7)
m1.set_monkeys(m7, m0)
m2.set_monkeys(m4, m3)
m3.set_monkeys(m6, m4)
m4.set_monkeys(m6, m5)
m5.set_monkeys(m1, m0)
m6.set_monkeys(m5, m1)
m7.set_monkeys(m2, m3)
m0.set_items([83, 97, 95, 67])
m1.set_items([71, 70, 79, 88, 56, 70])
m2.set_items([98, 51, 51, 63, 80, 85, 84, 95])
m3.set_items([77, 90, 82, 80, 79])
m4.set_items([68])
m5.set_items([60, 94])
m6.set_items([81, 51, 85])
m7.set_items([98, 81, 63, 65, 84, 71, 84])

order = [m0, m1, m2, m3, m4, m5, m6, m7]

for i in range(10000):
    for monkey in order:
        monkey.run_turn()

inspections = [x.inspections for x in order]
inspections.sort(reverse=True)
print(inspections[0] * inspections[1])
