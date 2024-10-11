#Sequence data types store multiple values in the same variable in an organized and efficient way.

#String is an immutable sequence of characters represented by quotes.
str1 = "Hello World"
print(str1[0])
# str[0] = "P" #An error will be generated because it is immutable.

str2 = """ 
        Multiline 
         String
"""

print(str2)

f = 'data'
s = 'structure'
print(f + s) #We use + to concatenate strings.
print('Data ' + 'structure') 

t = 'data-'
print(t * 3) #The '*' operator in Python is used to repeat a string a specified number of times.

#The range() function returns a sequence of numbers, starting from 0 by default, 
#and increments by 1 (by default), and stops before a specified number.
print(list(range(10))) #list() converts the sequence into a list
print(range(10))
print(list(range(0, 100+1, 10)))

#Lists are used to store multiple items in a single variable.
list01 = ['food', 'bus', 'apple', 'quuen']
print(list01)
print(list01[2]) #Acessing list elements

print(['food', 'bus', 'apple', 'quuen'] == ['bus', 'quuen', 'apple', 'food']) #Lists are ordered.

#Lists are dynamic, you can add or remove elements as needed.
list01 += ['guitar']
print(list01)
list01[2:3] = [] # Removes the element at index 2 by replacing the slice list01[2:3] with an empty list []
print(list01)
del list01[0] #Deleting an element from the list
print(list01)

list01 += [43, False, 2.900, range(10)] #The elements of the list can be of various data types.
print(list01)

list02 = ['data', 'structures', 'using', 'python', 'happy', 'learning']
print(list02[-2]) #Negative indices start counting from the end of the list.
print('Slicing ' , list02[1:4]) 
list02[1:4] = [1, 2, 3, 4]
print(list02)

#Operators and internal functions can be applied to lists.
print('data' in list02) # 'in' checks if an element exists in the list
print('man' in list02)  # 'not in' checks if an element does not exist in the list)

a = [1, 2, 3, 4]
b = [5, 6, 8, 7]
c = ['a', 'b', 'c']
concatenated_list = a + b # '+' is used for concatenation, combining two lists
print(concatenated_list)
print(a * 2 + b * 2) # '*' is used to repeat a list a certain number of times
print(len(concatenated_list)) # 'len()' returns the length (number of elements) of a list
print(min(c)) #'min()' returns the smallest element in a list
print(max(b)) # 'max()' returns the largest element in a list