class Transport:

    def __init__(self, color, power, wheel, classificator=0, passenger=0, cargo=0):
        self.color = color
        self.power = power
        self.wheel = wheel
        self.classificator = classificator
        self.passenger = passenger
        self.cargo = cargo

    def __str__(self):
        return f'Транспортное средство'


class Car(Transport):

    def __super__(self, color='white', power=100, wheel=4, classificator=0):
        self.color = color
        self.power = power
        self.wheel = wheel
        self.classificator = classificator

    def charcter(self):
        return f'Тип: {self.classificator}, Цвет авто: {self.color}, мощность: {self.power}, кол-во колес: {self.wheel}'

    def __str__(self):
        return 'Автомобиль'


trans = Transport('Blue', 140, 6, 5, 7, 1)
auto_1 = Car('auto', 1, 0, 3)
toyota = Car('gray', 120, 4, 3)


# print(f'Цвет авто: {auto_1.color}, мощность: {auto_1.power}, кол-во колес: {auto_1.wheel}, вместимость: {auto_1.passenger}')
# print(f'Тип: {toyota.classificator}, Цвет авто: {toyota.color}, мощность: {toyota.power}, кол-во колес: {toyota.wheel}')

print(auto_1)
print(trans)
print(auto_1.__super__())
print(toyota.__super__('gray', 120, 4, 3))
print(toyota.charcter())


