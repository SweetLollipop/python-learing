"""
演示布尔类型的定影
以及比较运算符的应用
"""
# 定义变量存储布尔类型的数据
bool_1 = True
bool_2 = False
print(f"bool_1变量的内容是：{bool_1}，类型是：{type(bool_1)}")
print(f"bool_2变量的内容是：{bool_2}，类型是：{type(bool_2)}")

# 比较运算符的使用
# ==, !=, >, <, >=, <=
# 演示进行内容的相等比较
num1 = 10
num2 = 10
print(f"10 == 10的结果是：{num1 == num2}")
num3 = 10
num4 = 15
print(f"10 != 15的结果是：{num3 != num4}")
name1 = "itcast"
name2 = "itheima"
print(f"itcast == itheima 结果是：{name1 == name2}")

# 演示大于小于, 大于等于小于等于的比较运算
num5 = 10
num6 = 5
print(f"10 > 5的结果是：{num5 > num6}")
print(f"10 < 5的结果是：{num5 < num6}")
num7 = 10
num8 = 11
print(f"10 >= 11的结果是：{num7 >= num8}")
print(f"10 <= 11的结果是：{num7 <= num8}")
