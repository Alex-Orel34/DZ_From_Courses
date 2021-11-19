class car:
    def __init__(self, marka, model, date, speed):
        self.__marka = marka
        self.__model = model
        self.__date = date
        self.__speed = speed

    @property
    def marka(self):
        return self.__speed

    @marka.setter
    def marka(self, speed):
        self.__speed = speed

    @property
    def model(self):
        return self.__model

    @model.setter
    def model(self, model):
        self.__model = model

    @property
    def date(self):
        return self.__date

    @date.setter
    def date(self, date):
        self.__date = date

    @property
    def speed(self):
        return self.__speed

    @speed.setter
    def speed(self, speed):
        self.__speed = speed

    def increase_speed_up(self):
        self.speed += 5

    def increase_speed_down(self):
        self.speed -= 5

    def stop(self):
        self.speed = 0

    def print_speed(self):
        print(self.speed)

    def turn_around(self):
        self.speed = -self.speed

    def print(self):
        print(self.__marka)
        print(self.__model)
        print(self.__date)
        print(self.__speed)


car = car('BMW', 'M5', '22.08.2002', 90)
car.print()
car.increase_speed_up()
car.print()
car.increase_speed_down()
car.print()
car.turn_around()
car.print()
car.stop()
car.print()