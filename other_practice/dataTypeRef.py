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
    return l[:]

my_list = [1, 2, 3]
new_list = copy_list(my_list)
print(new_list)
print(my_list == new_list)
print(my_list is new_list)
