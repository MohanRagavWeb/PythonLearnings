def add_item(list_x):
    list_x += [3]

list_a = [1, 2]
add_item(list_a)
print(list_a)

"""
list_x refers to the same list object as list_a
+= modifies the list in-place (does NOT create a new list)
So the original list is updated
O/P: [1,2,3]
"""

def add_item(list_x):
    list_x = list_x + [3]

list_a = [1, 2]
add_item(list_a)
print(list_a)

"""
list_x + [3] creates a NEW list
list_x now points to a new object
list_a still points to the old unchanged list
O/P: [1,2]
"""


def add_item(list_x):
    list_x = list_x + [3]
    return list_x
list_a = [1,2]
b=add_item(list_a)
print(b)