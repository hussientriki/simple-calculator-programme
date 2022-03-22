while True:
    num = int(input("enter the first number : "))
    num1 = int(input("enter the second number : "))
    print("1)addition")
    print("2)subtraction")
    print("3)multiplication")
    print("4)devision")
    print("5)power")
    addition = 1
    subtraction = 2
    multiplication = 3
    division = 4
    power = 5
    sign = int(input("enter the sign : "))
    if sign == addition:
        print(num + num1)
    elif sign == subtraction:
        print(num - num1)
    elif sign == multiplication:
        print(num * num1)
    elif sign == division:
        print(num / num1)
    elif sign == power:
        print(num ** num1)
    desire = input("if you want to quit enter \"q\" or if you want to restart enter \"y\" : ")
    if desire == "y":
        continue
    break
