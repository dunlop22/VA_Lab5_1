import numpy as np
import matplotlib.pyplot as plt
import math
import getch

##Расчет значений функции в точках
def y_Count(x_):
    y_ = []
    for i in range(len(x_)):
        x = x_[i]
        y_.append(eval(func))
    return y_

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


def trapezoid(y_, h):
    rez = (y_[0] + y_[len(y_) - 1] ) / 2
    
    for i in range (1, (len(y_) -1)):
        rez = rez + y_[i]
    rez = rez * h
    return rez

def simpson_(x_, y_):
    if len(x_) % 2 == 0: ##нечетное число отрезков, т.к. четное число значений
        ##добавить до четного значения отрезков
        x_ = np.append(x_, x_[len(x_) - 1] + h)
        y_ = y_Count(x_)
    
    rez = y_[0] + y_[len(x_) - 1]

    for i in range (1, len(x_), 2): ##подсчет по нечетным 
        rez = rez + (y_[i] * 4)
    
    for i in range (2, len(x_) - 1, 2): ##подсчет по четным 
        rez = rez + (y_[i] * 2)

    rez = rez * h / 3
    return rez


def Rung(x_, h):
    h_n = h
    k = 1
    n = len(y_) - 1
    ready = False
    while not ready:
        ready = True
        for i in range(n * k - 1):
            x_1 = [x_[0] + h_n * i, x_[0] + h_n * i + h_n]
            y_1 = y_Count(x_1)
            
    print(h_n, "<-new h")
    return h_n

print("Введите функцию: Y = ", end = '')
func = input();

print("\nВведите левую границу участка: ", end = '')
a = float(input())

print("\nВведите правую границу участка: ", end = '')
b = float(input())

print("\nВведите шаг: ", end = '')
h = float(input())

print("\nВведите допустимую погрешность: ", end = '')
e = float(input())

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

trapezoid = trapezoid(y_, h)
print("Метод трапеций: ", trapezoid)

##метод Симпсона
simpson_znach = simpson_(x_, y_)
print("Метод Симпсона: ", simpson_znach)


##метод Рунге
h_new = h
k = 1
n = len(x_ - 1)
ready = False

while not ready:
    ready = True
    for i in range(n * k - 1):
        x_1 = [x_[0] + h_new * i, x_[0] + h_new * i + h_new]
        y_1 = y_Count(x_1)
        if abs(trapezoid(y_1, h_new / 2) - trapezoid(y_1, h_new)) > eps * h_new / (y_[len(x_) - 1] - y_[0]):
            h_new /= 2
            k += 1
            ready = False
            break

print("Автоматический шаг (метод Рунге: ", h_new)


trapezoid_auto = trapezoid(y_, h_new)
print("Метод трапеций: ", trapezoid_auto)