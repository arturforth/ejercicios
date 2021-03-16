"""
>>> from clases import *
>>> c1 = circulo(-5)
Traceback (most recent call last):
    ...
clases.RadioMenorACeroError: El radio del circulo no puede ser menor a cero
>>> circulo1 = circulo(7)
>>> circulo1.radio = -2
Error: El radio no puede ser menor a cero
>>> circulo1.area()
153.93804002589985
>>> circulo1.perimetro()
43.982297150257104
"""