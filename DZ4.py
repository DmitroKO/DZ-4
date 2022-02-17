a = float(input('Ввидите первое число:'))
x = input("Выберите действие(+, -,*, /):")
b = float(input('Ввидите второе число:'))
if x == "+":
    c = a + b
    print("Результат:" + str(c))
elif x == "-":
    c = a - b
    print("Результат:" + str(c))
elif x == "*":
    c = a * b
    print("Результат:" + str(c))
elif x == "/":
    if b :
        c = a / b
        print("Результат:" + str(c))
    else:
        print("Деление на '0' не возможно!" )