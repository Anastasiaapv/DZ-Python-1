# Задача 8: Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.
# Пример:
# - A (3,6); B (2,1) -> 5,09

x1 = float(input('Введите X1: '))
y1 = float(input('Введите Y1: '))
x2 = float(input('Введите X2: '))
y2 = float(input('Введите Y2: '))
a = ((x2-x1)**2+(y2-y1)**2)**(0.5)
print(a)

