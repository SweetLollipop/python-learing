print("请猜出我心里想的数字，您共有3次机会。")
num = 10
if int(input("请输入第一次猜想的数字：")) == num:
    print("您猜对啦，答案是10。")
elif int(input("不对，再猜一次：")) == num:
    print("您猜对啦，答案是10。")
elif int(input("不对，再猜一次：")) == num:
    print("您猜对啦，答案是10。")
else:
    print("Sorry,全部猜错啦，我想的是10。")
