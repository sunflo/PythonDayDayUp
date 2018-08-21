def cal_sum(*x):
    result = 0
    for i in x:
        result = result + i
    return result


# print(cal_sum(2, 5))

def cal_sum_lazy(*x):
    def func():
        result = 0
        for i in x:
            result = result + i
        return result

    return func


# f = cal_sum_lazy(2, 4, 6)
# print(f())


# 装饰器


def log(func):
    def wra(*args, **kw):
        print('log=====>>>call %s():' % func.__name__)
        return func(*args, **kw)

    return wra


@log
def now(tv):
    print("hello 2018", tv)


now(123)
