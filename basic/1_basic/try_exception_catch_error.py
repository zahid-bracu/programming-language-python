try:
    result=10/0
    idNumber=int(input("Enter your Roll"))
    print(idNumber)
except ZeroDivisionError as error:
    print(error)
except ValueError as error:
    print(error)
except:
    print("Other Error")