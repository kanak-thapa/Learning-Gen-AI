# types of compiler read convert to byte code then execute and then execute 
# and interpreter read execute read execute 

# python is interpreted lang
# who execute it python virtual machine 
"""
multi line comments
A - Z 65 - 90
a - z 97 - 122
we know what strings are but you must also know string
take more space than other data types like int, float etc
-- This happens because String stores every character with
their own Unicode
-- is a universal character encoding standard that
assigns a unique number (code point) to every character,
regardless of language
 Like “A” unicode is 65 
we can check them by using ord() function in python and
convert them back using chr() function.

-- Now the default data type of input is always string reason is
simple you can store anything in string.V
"""

# print("namaste kanak, we are learning python")
# name = "yash"
# age = 21

# print(name, age)
# print(ord('A'))
# print(chr(65))

# slicing 
# print(name[4:1:-1])

# input1 = str(input("enter name 1: "))

# print(f"hello my name is {input1}, nice to meet you")
# a = "Kanak"


# for i in range(6, 0, -1):#last one is not included
#     print(i)

# ans = 1

# for i in range(5, 0, -1):
#     ans = ans * i

# print(ans)

# num = 6
# sum = 0
# for i in range(1, num):
#     if(num%i==0):
#         sum = sum + i
# #1, 2, 3
# print(sum)

# if sum==num:
#     print(f"{num} this number is a perfect number")

#reversing a string

# string_name = "kanak"

# result = ""

# for i in range(len(string_name)-1, -1, -1):
#     result = result + string_name[i]

# print(result)

# if(result==string_name):
#     print("it is palindrome")

# str1 = "P@#yn26at^&i5ve"
# digit = 0
# character = 0
# symbol = 0

# for i in range(len(str1)):
#     if(str1[i].isdigit()):
#         digit+=1
#     elif(str1[i].isalpha()):
#         character+=1
#     else:
#         symbol+=1

# print(digit)
# print(character)
# print(symbol)

# a = 899
# ans = 0
# while(a>0):
#     num = a%10
#     ans = ans*10 + num
#     print(num)
#     a = a//10

# print(ans)


# import random
# print(random.randint(1, 100))

# name = ["kanak", "aditya", "ram", "pari"]
# print(random.choice(name))

# def  greet(name):#parameters, variables listed inside the function definition.
#     print(f"hello, {name}")
# name = "kanak"


# greet(name)#arguments, Arguments are the Values passed to a function when it is called

'''
positional arguments work-
default argument

'''

# def add(a, b):
#     return a + b

# print(add(3, 5)) # 3 is assigned to 'a', 5 to '

# def introduce(name, age):
#     print(f"I am {name} and I am {age} years old.")

# introduce(age=25, name="John")


# def greet (name="Guest"):
#     print(f"Hello, {name}!")

# greet ()
# greet("Bob")


# Uses default value "Guest"
# Uses "Bob"

# max = float('-inf')
# second = float('-inf')

# list = [22, 23, 25, -1, 3,  27, -2, 29]
# for i in list:
#     if max<i:
#         second = max
#         max = i
#     elif(i>second and i<max):
#         second = i

# print(second)
# print(max)


# sorted or not
    #   0  1  2  3
# list = [2, 1, 4, 5]
# notsorted = False
# for i in range(0, len(list)-1):
#     if(list[i]>list[i+1]):
#         print("not sorted")
#         notsorted = True
#         break
# if(notsorted):
#     print("list is not sorted")
# else:
#     print("list is sorted")

# t = (5, 2, 9, 1, 5, 6)

# index = t.index(9)
# print(index)
# count = t.count(5)
# print(count)

s = {1, 2, 3, 2}
print(s)

# s.add(4) # Adds an element to the set
# # Removes 2 (Raises an error if not found)
# s. remove (2)
# s.discard(5)
# popped_element = s.pop() # Removes a random element
# s.clear()

# Removes 5 (No error if not found)
# Removes all elements


A = {1, 2, 3}
B = {3, 4, 5}

union_set = A.union(B) # {1, 2, 3, 4, 5}
intersection_set = A.intersection(B) # {3}
difference_set = A.difference(B)
# {1, 2}
symmetric_diff = A.symmetric_difference(B)

# {1, 2, 4, 5}
