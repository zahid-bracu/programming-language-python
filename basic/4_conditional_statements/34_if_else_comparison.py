def maxNumber(numOne,numTwo,numThree):
    if numOne>numTwo and numOne>numThree:
        print(str(numOne)+" is greater")
    elif numTwo>numOne and numTwo>numThree:
        print(str(numTwo)+" is greater")
    elif numThree>numOne and numThree>numTwo:
        print(str(numThree)+" is greater")
    elif numOne==numTwo and numTwo==numThree:
        print("All are equal")

maxNumber(11,11,11)