
"""
>>> from simple import *
>>> rd.seed(0)
>>> gendic()
[{'id': 0, 'edad': 50}, {'id': 1, 'edad': 98}, {'id': 2, 'edad': 54}, {'id': 3, 'edad': 6}, {'id': 4, 'edad': 34}, {'id': 5, 'edad': 66}, {'id': 6, 'edad': 63}, {'id': 7, 'edad': 52}, {'id': 8, 'edad': 39}, {'id': 9, 'edad': 62}]
>>> sortdic([{'id': 0, 'edad': 50}, {'id': 1, 'edad': 98}, {'id': 2, 'edad': 54}, {'id': 3, 'edad': 6}, {'id': 4, 'edad': 34}, {'id': 5, 'edad': 66}, {'id': 6, 'edad': 63}, {'id': 7, 'edad': 52}, {'id': 8, 'edad': 39}, {'id': 9, 'edad': 62}])
El id de la persona mas joven es: 3
El id de la persona mas vieja es: 1
[{'id': 1, 'edad': 98}, {'id': 5, 'edad': 66}, {'id': 6, 'edad': 63}, {'id': 9, 'edad': 62}, {'id': 2, 'edad': 54}, {'id': 7, 'edad': 52}, {'id': 0, 'edad': 50}, {'id': 8, 'edad': 39}, {'id': 4, 'edad': 34}, {'id': 3, 'edad': 6}]
"""