op = {'+': [], '-': [], '*': [], '/': []}
while True:
    try:
        a = int(input("Введите первое число: "))
        b = int(input("Введите второе число: "))
        sign = input("Введите оператор (+, -, *, /): ")
    except ValueError:
        print("*** Введите десятичное число!")
        continue

    if (sign == "/" and b == 0):
        print("*** На ноль делить нельзя.")
        continue

    functions = {
        '+': a + b,
        '-': a - b,
        '*': a * b,
        '/': a / b if b != 0 else None
    }

    if sign not in functions: #проверка отсутствия оператора в словаре
        print("*** Неверно введен оператор.")
        continue

    textmath = f"{a} {sign} {b} = {functions[sign]}" #текст с решением
    op[sign].append(textmath)

    print(textmath)
    print(f"История решений")
    for o,r in op.items():
        print(o,r)

    answer = input("Хотите выполнить еще одну операцию? (1/0): ")
    if answer.lower() != "1":
        break
