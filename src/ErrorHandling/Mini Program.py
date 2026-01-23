try:
    num1 = int(input("Enter number: "))
    num2 = int(input("Enter another number: "))
    result = num1 / num2
except ZeroDivisionError:
    print("Cannot divide by zero")
except ValueError:
    print("Invalid input")
else:
    print("Result:", result)
finally:
    print("Program finished")
