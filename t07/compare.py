def my_sum(*args):
    return sum(args)


# 加上非空及类型判断

def execute(func):
    def validate(*args):
        print("in")
        if len(args) == 0:
            return 0
        for x in args:
            if not isinstance(x, int):
                return 0
        return func(*args)

    return validate


# 装饰器，语法糖，等价于my_avg = execute(my_avg)
@execute
def my_avg(*args):
    return sum(args) / len(args)


print(my_avg(1, 2, 3, 4))
