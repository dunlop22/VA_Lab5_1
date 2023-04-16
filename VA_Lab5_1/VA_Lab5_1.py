import numpy as np
import matplotlib.pyplot as plt
import math
import getch

##Расчет значений функции в точках
def y_Count(x_):
    y_2 = []
    for i in range(len(x_)):
        x = x_[i]
        y_2.append(eval(func))
    return y_2

def left_pryamoug():
    rez = 0
    for i in range (len(y_) - 1):
        rez = rez + y_[i]
    rez = rez * h
    return rez

def middle_pryamoug():
    rez = 0
    for i in range (len(y1) - 1):
        rez = rez + y1[i]
    rez = rez * h
    return rez

def middle_pryamoug1():
    rez = 0
    for i in range (len(y_) - 1):
        rez = rez + ((y_[i] + y_[i +1]) / 2) 
    rez = rez * h
    return rez

def right_pryamoug():
    rez = 0
    for i in range (1, len(y_)):
        rez = rez + y_[i]
    rez = rez * h
    return rez


def trapezoid(y_2, h1):
    rez = (y_2[0] + y_2[len(y_2) - 1] ) / 2
    
    for i in range (1, (len(y_2) -1)):
        rez = rez + y_2[i]
    rez = rez * h1
    return rez

def simpson_(x_, y_, h):

    if len(x_) % 2 == 0: ##нечетное число отрезков, т.к. четное число значений
        ##изменить количество отрезков
        h_old = h
        h = (b - a) / (((b - a) / h_old) + 1)
        x_ = np.arange(a, b + h, h)
        print ("\nНовый шаг (т.к. число отрезков изначально нечетное): ", h)
        ##добавить до четного значения отрезков
        y_ = y_Count(x_)
    
    rez = y_[0] + y_[len(x_) - 1]

    for i in range (1, len(x_), 2): ##подсчет по нечетным 
        rez = rez + (y_[i] * 4)
    
    for i in range (2, len(x_) - 1, 2): ##подсчет по четным 
        rez = rez + (y_[i] * 2)

    rez = rez * h / 3
    return rez

print("Введите функцию: Y = ", end = '')
func = input();

print("\nВведите левую границу участка: ", end = '')
a = float(input())

print("\nВведите правую границу участка: ", end = '')
b = float(input())

print("\nВведите шаг: ", end = '')
h = float(input())

##равномерное распределение x с шагом h

x_ = np.arange(a, b + h, h)
x1 = x_ + h/2   ##значения X для метода средних прямоугольников

##расчет значений y по введенной функции
y_ = []
y_ = y_Count(x_)
y1 = y_Count(x1)    ##значения Y для метода средних прямоугольников

##метод левых прямоугольников
left = left_pryamoug()
print("Метод левых прямоугольников: ", left)

##метод средних прямоугольников
middle = middle_pryamoug()
print("Метод средних прямоугольников: ", middle)


##метод правых прямоугольников
right = right_pryamoug()
print("Метод правых прямоугольников: ", right)

##метод трапеции

trapezoi1d = trapezoid(y_, h)
print("Метод трапеций: ", trapezoi1d)

##метод Симпсона
simpson_znach = simpson_(x_, y_, h)
print("Метод Симпсона: ", simpson_znach)

