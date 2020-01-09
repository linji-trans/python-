
num1 = int(input("请输入一个正整数: "))
num2 = int(input("请再输入一个正整数: "))
num3 = num1 * num2
while True:
    a = num1 // num2
    if a == 0:
        b = num2 % num1
        if b == 0:
            print("最大公约数：", num1)
            print("最小公倍数: ", int(num3 / num1))
            break
        else:
            num2 = num1
            num1 = b
    else:
        b = num1 % num2
        if b == 0:
            print ("最大公约数：", num2)
            print("最小公倍数: ", int(num3 / num2))
            break
        else:
            num1 = num2
            num2 = b


































