# 循环输出
names = ["tom", "kobe", "micheal"]
for name in names:
    print(name)

# 求和
sums = 0
nums = [2, 4, 5, 6, 56, 17, 1, 3]
for i in nums:
    sums = sums + i
print(sums)

# range
print(list(range(10)))

# range 求和
sum1 = 0
# 生成一个0-101的序列，可通过list方法转为list
for i in range(101):
    sum1 = sum1 + i
print(sum1)

# continue break
for i in range(100):
    if (i >= 50):
        break
    if i % 2 == 0:
        continue
    print(i)
