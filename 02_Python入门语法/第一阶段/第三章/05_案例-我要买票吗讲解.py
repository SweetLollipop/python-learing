"""
演示Python中
if else的组合判断语句
练习案例：我要买票吗
"""
print("欢迎来到黑马动物园。")
height = int(input("请输入你的升高（cm）："))
if height >= 120:
    print("您的身高超出120cm，游玩需要购票10元。")
else:
    print("您的身高未超出120cm，可以免费游玩。")
print("祝您游玩愉快。")