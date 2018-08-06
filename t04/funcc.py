from t04.funcClazz import *

#
# print(my_abs(-123))
#
# print(move(12, 23, 2, 90))
#
# x, y = move(12, 23, 2, 90)
# print(x)
# print(y)
#
# print(calc(1, 2, 3, 4, 5))
#
# num = [1, 2, 3, 4, 5]
# print(calc(*num))
#
# #
# person("jack", 23)
# extra = {"city": "suzhou", "job": "engineer"}
# person("micheal", 23, **extra, zipcode=12344)

# 这里有点凌乱，既然限制输入的参数名，那何苦多次一举设置为可变参数呢？
person1("flo", 26, city="suzhou", job="en")

# 递归
print(fact(20))

s = "abcded"
print(s[-2:-1])

print(list(range(1, 11)))
print([x * x for x in range(1, 11)])
