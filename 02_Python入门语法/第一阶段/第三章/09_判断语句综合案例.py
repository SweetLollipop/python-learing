"""
演示判断语句的实战案例，中级猜数字
"""
# 1.构建一个随机的数字变量
import random
num = random.randint(1, 10)

guess_num = int(input("请输入你要猜测的数字："))

# 2.通过if判断语句进行数字的猜测
if guess_num == num:
    print("恭喜，第一次就猜中了")
else:
    if guess_num >num:
        print("你猜测的数据大了")
    else:
        print("你猜测的数据小了")

    guess_num = int(input("再次输入你要猜测的数字："))

    if guess_num == num:
        print("恭喜，第二次猜中了")
    else:
        if guess_num > num:
            print("你猜测的数据大了")
        else:
            print("你猜测的数据小了")

        guess_num = int(input("再次输入你要猜测的数字："))

        if guess_num == num:
            print("恭喜，第三次猜中了")
        else:
            print("三次机会用完了，没有猜中。")