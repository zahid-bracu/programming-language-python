numberOne = int(input("Please Enter Number One"))
numberTwo = int(input("Please Enter Number Two"))
operator = input("Please Enter operator")

def calculate(numberOne,numberTwo):
    if operator == "+":
        return numberOne+numberTwo
    elif operator == "-":
        return numberOne-numberTwo
    elif operator == "*":
        return numberOne*numberTwo
    elif operator == "/":
        return numberOne/numberTwo
result=calculate(numberOne,numberTwo)
print("The result is "+str(result))