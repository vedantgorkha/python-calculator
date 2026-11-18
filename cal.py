num1 = float(input("ENTER A NUMBER: "))
op = input("ENTER OPERATION (+, -, *, /): ")
num2 = float(input("ENTER SECOND NUMBER: "))

if op == "+":
    print(num1 + num2)

elif op == "-":
    print(num1 - num2)

elif op == "*":
    print(num1 * num2)

elif op == "/":
    if num2 == 0:
        print("CANNOT BE DIVIDED BY 0")
    else:
        print(num1 / num2)

else:
    print("INVALID OPERATION")
