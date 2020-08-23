

def extraLongFactorials(n):
    if n == 1:
        return 1
    print(n)   
    return n*extraLongFactorials(n-1)

input = 25
factorial = extraLongFactorials(input)
print(factorial)