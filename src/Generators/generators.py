def squares_list(n):
    return [x*x for x in range(n)]

def squares_gen(n):
    for x in range(n):
        yield x*x

print(squares_list(5))

for val in squares_gen(5):
    print(val)
