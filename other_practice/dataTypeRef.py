a = 1
b = 2
print('1==2 ? ', id(a) == id(b), id(a), id(b))
c = 2
print('2==2 ? ', id(c) == id(b), id(c), id(b))

a = "strawberry"
b = "strawberry"
print(id(a) == id(b))
c = "Strawberry"
print(id(c) == id(b))


# You can also use “is” to check if two variables have same objectID


list1 = [1, 2, 3]
list2 = list1[:]    # copy
print(list1)
print(list2)
print(list1 is list2)
print('list1 list2 same object? ', id(list1) == id(list2))

# In Python, all data is stored in the form of an object.
# An object has three things: id, type, and value.

print(type(2))
print(type(-6.25))
print(type(2,))
print(type("hello"))
print(type('A'))
print(type('346.789'))
print(type([2, 3, 4]))
print(type({'category': 'produce', 'count': 200}))
print(type(print))
print(type(type))


'''
Python
Mutable objects:
list, dict, set
'''
my_list = ['cat', 'dog', 'bunny']
print(id(my_list[0]))   # address of element changed, but not the list
print('Address of my_list is: {}'.format(id(my_list)))
my_list[0] = 'sugar glider'
print(id(my_list[0]))

print('Address of my_list is: {}'.format(id(my_list)))

'''
Python
Immutable objects:
integer, float, string, tuple, bool, frozenset

Immutability may be used to ensure that an object remains constant
throughout your program. The values of mutable objects can be
changed at any time and place, whether you expect it or not.
'''

def assign_value(n, v):
    n = v

list1 = [1, 2, 3]
list2 = [4, 5, 6]
assign_value(list1, list2)
print(list1)    # like 'passed by pointer'

def copy_list(l):
    # return l[:]
    return list(l)

my_list = [1, 2, [3, 4]]
new_list = copy_list(my_list)
print(new_list)
print(my_list == new_list)
print(id(my_list) == id(new_list))
print(my_list is new_list)


import copy

'''
shallow copy creates object with the reference of original elements
shallow copy doesn't create copy of nested objects,
instead it just copies the reference of nested objects.
'''
old_list = [[1, 1, 1], [2, 2, 2], [3, 3, 3]]
new_list = copy.copy(old_list)
old_list.append([4, 4, 4])

print("Old list:", old_list)
print("New list:", new_list)

old_list[1][1] = 'AA'

print("Old list:", old_list)
print("New list:", new_list)


'''
A deep copy creates a new object and recursively adds the copies of
nested objects present in the original elements.
'''
new_list = copy.deepcopy(old_list)

old_list[1][0] = 'BB'

print("Old list:", old_list)
print("New list:", new_list)