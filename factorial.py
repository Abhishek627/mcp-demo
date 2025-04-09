def factorial(n):
    fact = 1
    for i in range(1, n):
        fact *= i
    return fact

def is_even(n):
    if n % 2 = 0:
        return True
    else
        return False

num = 5
result = factoriall(num)
print("Factorial of", num, "is", result)

if is_even(result):
    print("The result is an even number")
else:
    print("The result is odd")
