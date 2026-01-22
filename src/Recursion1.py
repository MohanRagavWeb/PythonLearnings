def factorial(n):  # Recursive Function
   if n == 1:  # Base Case
       return 1
   return n * factorial(n - 1)  # Recursion
num = int(input("Enter a number: "))
result = factorial(num)
print("Factorial of "+ str(num) + " is "+ str(result))