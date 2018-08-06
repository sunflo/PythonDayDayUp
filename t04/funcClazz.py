import math


def my_abs(x):
    if not isinstance(x, (int, float)):
        raise TypeError("bad opreate type")
    if x >= 0:
        return x
    else:
        return -x


def funcnop():
    pass


def move(x, y, step, angle=0):
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx, ny


def calc(*num):
    sum1 = 0
    for x in num:
        sum1 = sum1 + x

    return sum1


def person(name, age, **extra):
    print(name)
    print(age)
    print(extra)


def person1(name, age, *, city, job):
    print(name, age, city, job)
