def increment(a):
    a += 1
    return a


a = int(input())
increment(a)
print(a)

"""(same answer)
Even though variable names are same, they are referring to two different objects.
Changing the value of the variable inside the function will not affect the variable outside.
"""