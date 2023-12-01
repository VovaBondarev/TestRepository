class Transport:
    def __init__(self, count_wheel, speed, count_place, view):
        self.count_wheel = count_wheel
        self.speed = speed
        self.count_place = count_place
        self.view = view

    def get_a(self):
        return a.count_wheel, a.speed, a.count_place, a.view

    def set_a(self):
        r

class Automobile(Transport):
    def __init__(self, count_wheel, speed, count_place, view):
        super().__init__(count_wheel, speed, count_place, view)


class Bike(Transport):
    def __init__(self, count_wheel, speed, count_place, view):
        super().__init__(count_wheel, speed, count_place, view)


a = Transport(0, 1000, 50,"Самолёт")
b = Automobile(4, 60, 5, "Автомобиль")
c = Bike(2, 20, 1, "Велосипед")
print(f"{a.view} имеет {a.count_wheel} колёс, скорость {a.speed} км/ч, {a.count_place} мест")
print(f"{b.view} имеет {b.count_wheel} колёс, скорость {b.speed} км/ч, {b.count_place} мест")
print(f"{c.view} имеет {c.count_wheel} колёс, скорость {c.speed} км/ч, {c.count_place} мест")
