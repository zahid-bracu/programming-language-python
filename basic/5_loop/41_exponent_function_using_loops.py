def exponentFunction(base,power):
    result=1
    for i in range(power):
        result=result*base
    return result

result = exponentFunction(2,2)
print(result)