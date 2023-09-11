def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

# Input the number
number = int(input("Enter a number: "))

# Calculate the factorial using the recursive function
result = factorial(number)

# Print the result
print(f"The factorial of {number} is {result}")
