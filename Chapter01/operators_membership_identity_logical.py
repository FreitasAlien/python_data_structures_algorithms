#Membership operators test for the membership of an object in a sequence, such as strings, lists, or tuples. 
mylist1 = [10, 20, 30, 40]
mylist2 = [100, 50, 60, 90, 20]

if mylist1[1] in mylist2: # 'in' checks if an element exists in the list
    print("elements are overlapping")
else: 
    print("elements are not overlapping")

mylist3 = [1, 5, 10, 50, 340, 34, 52, 23]
mylist4 = [1, 40, 53, 50, 2, 60, 340, 24]

for i in range(8):
    if mylist3[i] not in mylist4: # 'not in' checks if an element does not exist in the list)
        print("the element",  mylist3[i], "- does not appear in both lists")
    else:
        print("the element", mylist3[i], "- appears in both lists")
        
#Identity operators compare the memory locations of two objects.
firstList = []
secondList = []

if firstList == secondList: # '==' checks if the values of two operands are equal or not
    print("Both are equal") 
else:
    print("Both are not equal")

# '==' is different from 'is' because '==' compares the values of two objects, while 'is' compares the memory locations of two objects.
thirdList = firstList

if thirdList is firstList: # 'is' checks if the memory locations of two objects are the same
    print("Both variables are pointing to the same object")
else:
    print("Both variables are not pointing to the same object")

if firstList is not secondList:
    print("Both firstList and secondList are not the same object")
else:
    print("Both firstList and secondList are the same object")

#Logical operators are used to combine conditional statements.
a = 35
b = 135

if a > 0 and b > 0: # 'and' returns True if both statements are true
    print("Both numbers are positive")
else:
    print("At least one number is less than or equal to zero")

c = 32
d = -32

if c > 0 or d > 0: # 'or' returns True if one of the statements is true
    print("At least one number is positive")
else:
    print("Both numbers are less than or equal to zero")

a = 32
if not a: # 'not' returns True if the object is False
    print("The number is false")
else:
    print("The number is true")
