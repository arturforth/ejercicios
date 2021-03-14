import math


class RadioMenorACeroError(Exception):
    pass


class circulo:
    def __init__(self, radio):
        self.__radio = radio

        try:
            if self.__radio < 0:
                raise RadioMenorACeroError
        except RadioMenorACeroError:
            print('El radio del circulo no puede ser menor a cero')
            exit()

    @property
    def radio(self):
        return self.__radio

    @radio.setter
    def radio(self, radio):
        if radio >= 0:
            self.__radio = radio
        else:
            print('Error: El radio no puede ser menor a cero')

    def area(self):
        return math.pi*(self.__radio**2)

    def perimetro(self):
        return 2*math.pi*self.__radio

circulo1 = circulo(-7)
# print(circulo1)
circulo1.radio = -1
print('fin')