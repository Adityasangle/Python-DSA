import collections

# initializing deque
de = collections.deque([1, 2, 3,4,5,6])
print("deque: ", de)

# using append() to insert element at right end
# inserts 4 at the end of deque
de.append(4)

# printing modified deque
print("\nThe deque after appending at right is : ")
print(de)

# using appendleft() to insert element at left end
# inserts 6 at the beginning of deque
de.appendleft(6)

# printing modified deque
print("\nThe deque after appending at left is : ")
print(de)

print(de[4])
print(de.count(4))
de[3] = 100

# using index() to print the first occurrence of 4
print ("The number 4 first occurs at a position : ")
print (de.index(4))

# using extend() to add numbers to right end
# adds 4,5,6 to right end
de.extend([9,10,12])

# printing modified deque
print ("The deque after extending deque at end is : ")
print (de)

# using extendleft() to add numbers to left end
# adds 7,8,9 to left end
de.extendleft([70,80,90])

# printing modified deque
print ("The deque after extending deque at beginning is : ")
print (de)