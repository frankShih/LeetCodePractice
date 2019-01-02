import array 

'''
Typecode	Value
b	        Represents signed integer of size 1 byte/td>
B	        Represents unsigned integer of size 1 byte
c          	Represents character of size 1 byte
i       	Represents signed integer of size 2 bytes
I       	Represents unsigned integer of size 2 bytes
f       	Represents floating point of size 4 bytes
d       	Represents floating point of size 8 bytes

＃so weird, can't use
array1 = array('i', [10,20,30,40,50])

for x in array1:
    print(x)

array1.insert(1,60)
array1.remove(40)
print(array1)
print (array1.index(40))

'''

# 2d array
a=[[0]*5 for i in range(5)]
# print(a)


