def factorial(n):
    fact = 1
    for i in range(1, n + 1):  # Include n in the range
        fact *= i
    return fact

def is_even(n):
    return n % 2 == 0  # Simplified logic

num = 5
result = factorial(num)  # Fixed typo in function call
print("Factorial of", num, "is", result)

if is_even(result):
    print("The result is an even number")
else:
    print("The result is odd")
