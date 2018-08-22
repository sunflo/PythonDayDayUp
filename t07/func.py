passline = 60


## 作用域LEGB
# L：local 函数内部作用域
# E:enclosing 函数内部与内嵌函数之间   
# G:全局作用域
# B:build-in 内置作用域



##闭包

def func(val):
    print('%x' % id(val))
    if val >= passline:
        print("pass")
    else:
        print("failed")

    def in_func():
        print(val)

    in_func()
    return in_func


f = func(89)
f()

print(f.__closure__)
