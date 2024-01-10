from array import *


# 1. create an array and traverse
print("Step 1")
my_array = array("i", [1, 2, 3, 4, 5])

for i in my_array:
    print(i)


# 2. Access individual elements through indexes
print("Step 2")
new_array = my_array[2]
print(new_array)


# 3. Append any value to the array using append() method
print("Step 3")
my_array.append(6)
print(my_array)


# 4. Insert the value into the array using insert() method
print("Step 4")
my_array.insert(0, 0)
print(my_array)


# 5. Extent python arrays using extend() method
print("Step 5")
extending_array = array("i", [6, 7, 8])
my_array.extend(extending_array)
print(my_array)


# 6. Add items from list into the array using fromlist() method
print("Step 6")
new_list = [9, 10]
my_array.fromlist(new_list)
print(my_array)


# 7. Romove any array element using remove() method
print("Step 7")
my_array.remove(3)
print(my_array)


# 8. Remove last element from the array using pop() method
print("Step 8")
my_array.pop()
print(my_array)


# 9. Fetch any element through its index using index() method
print("Step 9")
find_array = my_array.index(2)
print(find_array)


# 10. Reverse a python array using reverse() method
print("Step 10")
my_array.reverse()
print(my_array)


# 11. Get array buffer information through buffer_info() method
print("Step 11")
print(my_array.buffer_info())


# 12. Check for number of occurrences of an element using count() method
print("Step 12")
my_array.append(8) #second time
my_array.append(8) #third time
count = my_array.count(8)
print(count) #total 3 times is the occurrence of 8


# 13. Convert array to string using tostring() method
print("Step 13")
toString = my_array.tostring()
print(toString)


# 16. Convert array to a python list with same elements using fromlist() method 
print("Step 14")
inst = array('i')
inst.fromstring(toString)
print(inst)
 

# 15. Convert array to a python list with same elements using tolist() method  
print("Step 15")
toList = my_array.tolist()
print(toList)


# 16. Slice elements from a array
print("Step 16")
slicedArray = my_array[1:4]
print(slicedArray)
