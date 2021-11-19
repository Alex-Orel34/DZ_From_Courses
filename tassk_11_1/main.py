class desk:
    Size = 0
    Color = None
    Height = 0

    def __init__(self, size, color, height):
        self.__Size = size
        self.__Color = color
        self.__Height = height

    @property
    def Size(self):
        return self.__Size

    @Size.setter
    def Size(self, size):
        self.__Size = size

    @property
    def Color(self):
        return self.__Color

    @Color.setter
    def Color(self, color):
        self.__Color = color

    @property
    def Height(self):
        return self.__Height

    @Height.setter
    def Height(self, height):
        self.__Height = height

    def cut(self):
        self.__Size -= 1


class carpet:
    Size = 0
    Color = None
    Material = None

    def __init__(self, size, color, material):
        self.__Size = size
        self.__Color = color
        self.__Material = material

    @property
    def Size(self):
        return self.__Size

    @Size.setter
    def Size(self, size):
        self.__Size = size

    @property
    def Color(self):
        return self.__Color

    @Color.setter
    def Color(self, color):
        self.__Color = color

    @property
    def Material(self):
        return self.__Material

    @Material.setter
    def Material(self, material):
        self.__Material = material

    def paint(self, color):
        self.__Color = color


class shop:
    Adress = None
    City = None
    Master = None

    def __init__(self, adress, city, master):
        self.__City = city
        self.__Master = master
        self.__Adress = adress

    @property
    def City(self):
        return self.__City

    @City.setter
    def City(self, city):
        self.__City = city

    @property
    def Master(self):
        return self.__Master

    @Master.setter
    def Master(self, master):
        self.__Master = master

    @property
    def Adress(self):
        return self.__Adress

    @Adress.setter
    def Adress(self, adress):
        self.__Adress = adress

    def new_master(self, master):
        self.__Master = master


class man:
    name = None
    height = 0
    weight = 0

    def __init__(self, name, height, weight):
        self.__name = name
        self.__weight = weight
        self.__height = height

    @property
    def Name(self):
        return self.__name

    @Name.setter
    def Name(self, name):
        self.__name = name

    @property
    def Height(self):
        return self.__height

    @Height.setter
    def Height(self, height):
        self.__height = height

    @property
    def Weight(self):
        return self.__weight

    @Weight.setter
    def Material(self, weight):
        self.__weight = weight

    def new_name(self, name):
        self.__name = name


class bed:
    size = 0
    color = None
    material = None

    def __init__(self, size, color, material):
        self.__size = size
        self.__color = color
        self.__material = material

    @property
    def Size(self):
        return self.__size

    @Size.setter
    def Size(self, size):
        self.__size = size

    @property
    def Color(self):
        return self.__color

    @Color.setter
    def Color(self, color):
        self.__color = color

    @property
    def Material(self):
        return self.__material

    @Material.setter
    def Material(self, material):
        self.__material = material

    def broke(self):
        print('Chruum')
