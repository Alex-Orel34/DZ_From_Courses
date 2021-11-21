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

    def print(self):
        print(self.__marka)
        print(self.__model)
        print(self.__date)
        print(self.__speed)

    def stop(self):
        self.speed = 0

    def turn_around(self):
        self.speed = -self.speed


class sport_car(car):
    def increase_speed_up(self):
        self.speed += 10

    def increase_speed_down(self):
        self.speed -= 10


class truck(car):
    def check(self):
        if self.speed > 60:
            print(f'Attention! Your speed is {self.speed}, we recommend you 60.')

    def increase_speed_down(self, k):
        self.speed -= k

    def increase_speed_up(self):
        if self.speed > 60:
            print('reduce the speed to 60!')
            k = self.speed - 60
            self.increase_speed_down(k)
        else:
            self.speed += 5


class electro_car(car):
    def __init__(self, marka, model, date, speed, battery):
        self.__marka = marka
        self.__model = model
        self.__date = date
        self.__speed = speed
        self.__battery = battery

    @property
    def battery(self):
        return self.__battery

    @battery.setter
    def battery(self, battery):
        self.__battery = battery

    def level_of_battery(self):
        print(self.__battery)
        if self.__battery < 50:
            self.__speed = 40

    def print(self):
        print(self.__marka)
        print(self.__model)
        print(self.__date)
        print(self.__speed)
        print(self.__battery)

    def Power(self):
        self.__battery = 100


def main():
    car_test = sport_car('Bmw', 'M5', '22.08.2010', 70)
    car_test.print()
    print('------------------------------')
    car_test.increase_speed_up()
    car_test.print()
    print('------------------------------')
    car1 = truck('Belaz', "m105", "31.06.2006", 75)
    car1.print()
    car1.check()
    car1.increase_speed_up()
    print('------------------------------')
    car1.print()
    print('------------------------------')
    car2 = electro_car('Tesla', 'modulX', '23.05.2015', 80, 45)
    car2.print()
    print('------------------------------')
    car2.level_of_battery()
    print('------------------------------')
    car2.print()
    print('------------------------------')
    car2.Power()
    car2.print()


if __name__ == '__main__':
    main()
