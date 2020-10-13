## Escape_characters_as_normal_text.py  -----> Video 9
## Exercise-1 ---> Video 10
## Exercise-1 Solution ---> Video 11
## Raw Strings ----> Video 12
# print(r"line A /n Line B")

## How to print Emoji ----> Video 13
# print("\U0001F602")
# print("\U0001F603")
# print("\U0001F604")
# print("\U0001F605")
# print("\U0001F606")
# print("\U0001F607")
# print("\U0001F608")
# print("\U0001F609")
# print("\U0001F610")

## Python as a Calculator ---> Video 14
# print(2+3+4) #Addition
# print(5-2) #Subtraction
# print(10/3) #Float division
# print(4/2)
# print(2/4)
# print(10//3) #Integer Division
# print(2/4)
# print(15%2) # Modulo
# print(2**3) #Exponent
# print(2**0.5)# Find Under root
# print(round(2**0.5, 4)) # use for round 4numbers 


## Variables, Rules, Conbentions Why Python is called Dynamic Programming Language -->Video 15


# number1 = 2
# print(number1)
# number1 = 4
# print(number1)
# ## string, number
# name = "Siddhartha"
# print(name)
# name = 123
# print(name)

# ## Rule 1
# # 1number = 4
# # print(1number)
# ## start with lettet and (_) ....> first letter
# _name = "Siddhartha"
# print(_name)
# user_one_name = "Name" ##----> This  is also known as snake case writing

## Summary ---> Video 16
## Print function
## Escape Sequence
## Escape Sequence as normal text
## Python as calculator
## naming rules for variables
## Convention for variable string


### String Concatenation ---> Video 17

##  Strings 
## Collection of characters inside single quotes or double quotes

# first_name = "Siddhartha"
# last_name = " Singh"
# full_name = first_name + last_name
# print(full_name)

# print(first_name + "3")
# print(first_name * 3)

### User Input ----> Video 18

# #user input
## Input Function
# name = input("Enter your name : ")
# print("Hello " + name)

## String 
# age = input("What is your age ? : ")
# print("Your age is " + age)

### int()function ----> 19

# number_one = int(input("Enter first number"))
# number_two = int(input("Enter your second number"))
# total = number_one + number_two
# print("total is " + str(total))

#### More about variables ----> 20

# name, age = "Siddhartha", 19
# print("Hello " + name + "Your age is->" + str(age))

# x=y=z=1
# print(x+y+z)

### More than one input in one line ---> 21

# name, age = input("Enter your name and age : ").split()
# print(name)
# print(age)

#### String Formatting ---> 22
# name = "Siddhartha "
# age = 19
## Formating in 2.0

# print("Hello "+name + "Your age is "+ str(age))

## formating in 3.0

# print("Hello {}Your age is {} ".format(name, age))
# print("Hello {}Your age is {} ".format(name, age+5))
## formating in 3.6

# print(f"Hello {name}Your age is {age}")
# print(f"Hello {name}Your age is {age+2}")

####Exercise ----> Video 23 , 24

## Ask user to input 3 numbers and you have to print average of three numbers using string formatting.

# a,b,c = input("Please enter theree numbers comma seprated : ").split(",")
# total = (int(a)+int(b)+int(c))/3
# print(f"number a is {a},number b is {b}, number c is {c}")
# print(f"Avrage of a, b & c is :- {(int(a)+int(b)+int(c))/3}")
# print(total)

#### String Indexing ---> Video 25

# String Indexing 
# language = "Python"
# # Position (Index number)
# # p - 0
# # y - 1
# # t - 2
# # h - 3
# # o - 4
# # n - 5
# print(language[-6: ])

#### String Slicing ---> Video 26

# Slicing / selecting sub sequences

# lan = "Python"
# print(lan[4])
## Syntax - [start argument : stop argument]
# print(lan[0:6])

###### Step Argument ---> Video 27
## Slicing/ Slecting sub sequences
# lan = "Python"
## Synatx - [Start argument : stop argument -1 : step argument]
# print(lan[::-1])

##### Exercise 2--> video 28-29
## Q-> Ask user name and print back user name in reverse order.

# user_name = input("Enter your name : ")
# print(f"{user_name[::-1]}")


###### String Method part 1 ---> Video 30
## Sring method part one 
# name = "SiddHarTha SiNgh"
# ##1. len()function
# print(len(name))

# ##2. lower()method
# print(name.lower())

# ##3. upper()method
# print(name.upper())

# ##4. title()method
# print(name.title())

# ##5. count()method

# print(name.count("H"))

##### Exercise 3----> Video 31-32
## Take two cooma seprated inputs from users
## 1.) user`s name
## 2.) a single character 

## Output - 2print lines 
## 1.) User`s name length
## 2.) count the chracter that user input 

# User_name, word = input("Enter your name and use comma speration to enter your chr. : ").split(",")
# print(f"Your name length is: {len(User_name)} \n Word count is: {User_name.count(word)}")


###### Strip Method and solve previous problem of spaces ----> Video 33

# name1 = "   Sidd   hartha   "
# name = "   Siddhartha   "
# dots = "................"
# ## lstrip() method
# print(name + dots)
# print(name.lstrip() + dots)

# ## rstrip() method
# print(name.rstrip() + dots)

# ## strip() method
# print(name.strip() + dots)

# ## Replace method
# print(name1 + dots)
# print(name1.replace(" ", "") + dots)

##### Replace And Find Method ---> Video 34
## replace()method
## find()method
# string = "She is beautiful and she is good dancer"
# print(string.replace(" ", "_"))
# print(string.replace("is", "was"))
# print(string.replace("is", "was", 1))
# ##FInd method
# is_pos1 = string.find("is")
# is_pos2 = string.find("is", is_pos1 +1)
# print(is_pos2)

##### Center Method With Program ----> Video 35
## Center method
# name = "Siddhartha"
## **Siddhartha**
# print(name.center(16,"*"))
# user_name = input("Enter your name : ")
# len_un = len(user_name)
# print(user_name.center(len(name)+8, "*"))


######## Strings Are Immutable ---> Video 36
## Strings ARE immutable
# string = "String"
# print(string[1])


#### More Assignment Operators ---> Video 37

# name = "Sidd"
# name += "hartha"
# print(name)
# age = 18
# age += 1
# print(age)

##### Chapter 2 Summery -----> Video 38
## Strings
# name = "Siddhartha "

## String indexing
# print(name[2])

## String slicing
# print(name[:3])
# print(name[::-1])
## take user input
# user_name = input("Enter your name : ")
# print(user_name)

## take two user inputs
# one, two = input("Enter your name : ").split(", ")
# print(f"Name one {one} two is {two}")
## len function
# print(len(name))

## lower, upper, title method
# print(name.lower())
# print(name.upper())
# print(name.title())

## find, replace, center method 
# print(name.find("d"))
# store1 = name.find("d")
# store2 = name.find("d", store1+1)
# print(store2)

# print(name.replace("S", "s"))

# print(name.center(len(name)+6, "*"))  


########## If Statement ----> Video 39
## Syntax 
## if condition
## #code # if condition is true the this code will execute
## #code
# age = int(input("Enter your age : "))
# if age >=14:
#     print("You are above 14")


####### Pass Statement ----> Video 40

## Pass 
# x = 18
# if x >18:
#     pass


###### Else Statement ---> Video 41

# age = int(input("Enter your age : "))
# if age >=14:
#     print("You are above 14")
# else:
#     print("You are not above 14")


##### Exercise ----> Video 42- 43
## Number guessing game
## Make a variable, like wining_number and assign any number to it.
## Ask user to guess a number.
## If user didn`t guessed correctly then:
   # If user guessed lower than actual number then print "Too late"
   # if user guessed higher than actual number then print "too high"
# import random
# winning_number = random.randint(1,100)
# guess_number = int(input("Enter a number between 1 to 100 : "))

# if winning_number == guess_number:
#     print("You WIN !!!!!!")
# else:
#     if winning_number > guess_number:
#         print("Too Low")
#     else:
#         print("Too high")

####### And, or operator ---> Video 44

## Check two conditions at same time
## and  , or

# name = "abc"
# age = 19
# if name == "abc" and age ==19:
#     print("True")
# else:
#     print("False")

# if name == "abc" or age ==29:
#     print("True")
# else:
#     print("False")

##### Exercise ----> 45- 46
## Ask user name and age
## If user name starts with ("a" or "A") and age is above 10 then
## print "You anc watch movie"
## Else print " Sorry, you cannot watch coco"

# user_name = input("Enetr you name : ")
# age = int(input("Enter your age : "))
# if age >= 10 and (user_name[0] == "a" or user_name[0] == "A"):
#     print("You can watch movie")
# else:
#     print("Sorry you cannot watch coco")    


###### if....elif...else  statement----> Video 47

## show ticket pricing
## 0 to 3(free)
## 4 to 10 (150)
## 11 to 60(250)
## above 60 (200)


# n = input("Enter your name : ")
# a = int(input("Enter your age : "))
# if a == 0:
#     print("You can`t watch")
# if 0< a <= 3:
#     print(f"Hi {n} your fee price is Free!!!")
# elif 4< a <= 10:
#     print(f"Hii {n}  your fee price is $150")
# elif 11< a<= 60:
#     print(f"Hii {n} your fee price is $250")
# elif a>= 60:
#     print(f"Hii {n} your fee price is $200")


##### In Keyword ---> Video 48
# name = "Siddhartha"
## In keyword
## If with in
# if "a" in name:
#     print("a is present in your name")
# else:
#     print("a is not present")


###### Check empty or not ---> Video 49

## check empty or not
## important
# name = ""
# if name: ## true if string is not empty
#     print("String is not empty")
# else:
#     print("String is empty")


###### While Loop ------> Video 50

## loops 
## While loop, for loop

# print("hello world") #10 times
# i = 1
# while i<=10:
#     print(f"hello world {i}")
#     i += 1
    
######## Programing with while loop ----> Video 51
## Sum : 1 to n(or any number)
# total = 0
# i = 1
# while i <= 30:
#     total += i
#     i += 1
#     print(total)



###### Exercise ---->  Video 52-53

## Sum of n natural numbers.
## ask user for a natural number(n)

## Print total from 1 to n.

# n = int(input("Enter a number: "))
# total = 0
# i = 1
# while i<= n:
#     total += i
#     i +=1
#     print(total)


###### Exercise ----> 54-55
## Ask user to input a number containing more than one digit 
## Example - 1256
## calculate 1+2+5+6 and print

## Algorithm - (method to solve problem in human language)
## ask input in string, i.e., don`t chage string to int
## Example "1256"
## pick string character one by one and change to int 
## int(example[0]) + int(example[1])... go to len(example)

# user = input("Enter any four numbers : ")
# print(f"Input is : {user}\nLength of input is: {len(user)}\nTotal sum of input is :  {int(user[0])+int(user[1])+int(user[2])+int(user[3])}")

## use while loop

# total = 0
# i = 0
# while i < len(user):
#     total += int(user[i])
#     i += 1
# print(total) 


###### Exercise --- > 56-57

# user = input("Enter your name : ")
# temp_var = ""
# i = 0 
# while i< len(user):
#     if user[i] not in temp_var:
#         temp_var += user[i]
#         print(f"{user[i]} : {user.count(user[i])}")
#     i += 1


###### Infinite Loop----> Video  58

# i =0
# while i<= 10:
#     print("Hello world")
#     i += 1

###### For loop ----> Video 59

## For loop with range fun

# for i in range(11):
#     print(f"Hello World : {i}")
    


#### For Loop example ----> Video 60

## sum form 1 to 10
# s_num = int(input("Enetr starting number : "))
# e_num = int(input("Enetr End number : "))
# total = 0
# for i in range(s_num, e_num+1):
#     total += i
#     print(total)
# print(f"Total sum = {total}")

########### Example ----> Video 61

## Ask user a number like 1256
### Calculate sum of diits ----> 1+2+5+6
# total = 0
# num = input("Enter numbers : ")

# for i in range(0, len(num)):
#     total += int(num[i])
    
# print(total)



######## Example ----> Video 62

## Ask user name and count each character
## "Siddhartha Singh"

# name = input("Enter your name : ")
# temp = ""
# for i in range(0, len(name)):
#     if name[i] not in temp:
#         print(f"{name[i]}: {name.count(name[i])}")
#         temp += name[i]


###### Break and Continue ----> Video 63

## 1 to 10 print
## Break
# for i in range(1, 11):
#     if i == 5:
#         break
#     print(i)
    
## Continue
## print 1 to 10, but not 5
## 1234678910
# for i in range(1,11):
#     if i == 5:
#         continue
#     print(i)

###### Exercise ----> Video 64-65

### Modify number guessing game

# import random
# win_num = random.randint(1,100)
# num = int(input("Enter a number b/w 1 to 100 : "))
# guess = 1
# game_over = False
# while not game_over:
#     if num == win_num:
#         print(f"You win , And you guessed this num in {guess} times")
#         game_over = True
#     else:
#         if num < win_num:
#             print("too low")
#             guess += 1
#             num = int(input("Guess again : "))
#         else:
#             print("Too high")
#             guess +=1
#             num = int(input("Guess again : "))

######### DRY Principle ----> Video 66

### DRY- Don`t repeat yourself
# import random
# win_num = random.randint(1,100)
# num = int(input("Enter a number b/w 1 to 100 : "))
# guess = 1
# game_over = False
# while not game_over:
#     if num == win_num:
#         print(f"You win , And you guessed this num in {guess} times")
#         game_over = True
#     else:
#         if num < win_num:
#             print("too low")
#         else:
#             print("Too high")
#         guess +=1
#         num = int(input("Guess again : "))


##### Step Argument in range function ----> Video 67

# for i in range(10,0,-1):
#     print(i)


##### For loop and strings ----> Video 68

# name = "Siddhartha"
# for i in range(len(name)):
#     print(f"{name[i]}, {name.count(name)}")
    
# for i in name:
#     print(i)

# num = input("Enter a num : ")
# total = 0
# for i in num:
#     total += int(i)
# print(total)


###### Chapter 3 Summary ---- Video 69

## if statement
## and or oprater
## While loop 
## For loop
## brak keyword
## continue keyword


###### Function intro---> 70

## function

# name = "Siddhartha"
# print(len(name))
# a= 2
# b= 3
# def add_two(a,b):
#     return a+b 
# print(add_two(a,b))

## Int sum
# def add_two(a,b):
#     return a+b
# a = int(input("Enter first num : "))
# b = int(input("Enter second num : "))
# print(add_two(a,b))


## str sum
# def add_two(a,b):
#     return a+b
# a = input("Enter first name : ")
# b = input("Enter last name : ")
# print(add_two(a,b))

##### Print vs Return ----> Video 71

## print vs return

# def add_three(a,b,c):
#     return a+b+c

# print(add_three(5,5,5))
    

# def add_three(a,b,c):
#     print(a+b+c)

# add_three(5,5,5)


####### Functions Practice -----> Video 72

## Function practice
# def last_char(name):
#     return name[-1]
# print(last_char("Siddhartha"))



#
# def odd_even(num):
#     if num%2 == 0:
#         return "Even num"
#     else:
#         return "Odd"
# print(odd_even(9))


# def odd_even(num):
#     if num%2 == 0:
#         return "Even num"

#     return "Odd"
# print(odd_even(10))

# def is_even(num):
#     if num % 2 == 0:
#         return True
#     return False
# print(is_even(9))

# def is_even(num):
#     return num%2 == 0
# print(is_even(10))

###### Exercise ---> Video 73-74
# a = int(input("Enter first num : "))
# b = int(input("Enter last num : "))
# def grt_num(a,b):
#     if a>b:
#         return(f"grt num is {a}")
#     return(f"grt num is {b}")
# print(grt_num(a,b))


##### Define greatest ---> Video 75

# a = int(input("Enter first num: "))
# b = int(input("Enter secand num : "))
# c = int(input("Enter last num : "))

# def grt_num(a,b,c):
#     if a>b and c:
#         return (f"Grt num is {a}")
#     elif b>c and a:
#         return (f"Grt num is {b}")
#     return (f"Grt num is {c}")
# print(grt_num(a,b,c))


###### Function Inside function----> Video 76

# def grt_num(a,b):
#     if a>b:
#         return(f"grt num is {a}")
#     return(f"grt num is {b}")


##### Exercise ----> Video 77-78

## Define is_palindrome function that take one word in string as input 
## and return True if it is palindrome else return False

## palindrome - word that reads same backwords as forwards

## Example
## is_palidrome("madam")---> True
## is_palidrome("naman")---> True
## is_palidrome("horse")---> False

### logic(algorithm)
## step 1-> reverse the string 
## step 2-> compare reverse string with original string

# def is_palidrome(word):
#     reverse_word = word[::-1]
#     if word == reverse_word:
#         return True
#     return False

# print(is_palidrome("naman"))


# def is_palidrome(word):
#     if word == word[::-1]:
#         return True
#     return False
# print(is_palidrome("naman"))

#### Define Fibonacci ---> Video 79

# num = int(input("Enter a num: "))
# def fibonacci_seq(n):
#     a = 0
#     b = 1
#     if n == 1:
#         print(a)
#     elif n==2:
#         print(a,b)
#     else:
#         print(a,b, end =" ")
#         for i in range(n-2):
#             c = a + b
#             a = b
#             b = c
#             print(b, end = " ") 
# print(fibonacci_seq(num))



###### Default Parameters ----> Video 80

## default parameters

# def user_info(first_name, last_name, age):
#     print(f"Your first name is {first_name}")
#     print(f"Your last name is {last_name}")
#     print(f"Your age is {age}")
    
# print(user_info("Siddhartha", "Singh", 19))


##### Scope of variable inside and outside functions -----> Video 81
## Scope

# x = 5
# def func():
#    # global x
#    x = 7
#    return x

# print(func())
# print(x)


##### Intro to list ----> Video 82

## data structures
## list ----> this chapter
## orderd collection of items

## you can store anything in list int, flaot, string

# numbers = [1,2,3,4]
# print(numbers)
# print(numbers[2])

# words = ["word1", "word2","word3"]
# print(words)
# print(words[:2])

# mixed = [1,2,3,4,"five","six",2.3,None]
# print(mixed)

# mixed[1] = "two"
# print(mixed)

# mixed[1:] = "two"
# print(mixed)
 
# mixed[1:] = ["two","three","four"]
# print(mixed)


####### Add data to list-----> Video 83

## How to add items to our list
## most comman thing that you can do with your list and most important 

# fruits = ["grapes","apple"]
# fruits.append("mango")
# print(fruits)

# fruits = []
# fruits.append("mango")
# fruits.append("grapes")
# fruits.append("apple")
# print(fruits)


#### More methods to add data ----> Video 84

## some more methods to add data in our list 
## insert method
## how to join(concatenate) two list
## extend method
## diffrent between append and extend method

# fruits = ["mango","orange"]
# fruits.insert(1, "apple")
# print(fruits)

# fruits1 = ["apple","grapes"]
# fruit = fruits + fruits1
# print(fruit)

# print("Extend Method")
# fruits.extend(fruits1)
# print(fruits)
# print(fruits1)


# print("Append method")
# fruits.append(fruits1)
# print(fruits)

####### Delete data from list -----> Video 85

## common method to delete data from list

# fruits = ['Orange','apple','pear','banana','kiwi']

## pop method
# fruits.pop(1)
# print(fruits)

## del 
# del fruits[1]

## remove

# fruits.remove('banana')

# print(fruits)

##### In keyword with list ------> Video 86

# fruits = ['orange','apple','pear','banana','kiwi']

# if 'apple' in fruits:
#    print("apple is present")
# else:
#    print("not present")
   

###### Some more list methods ---->Video 87


# fruits = ['orange','apple','pear','banana','kiwi','apple']
## count

# print(fruits.count('apple'))
# print(fruits.count('orange'))

## sort method

# fruits.sort() 
# print(fruits)

## use num
# num = [9,10,6,5,3,1]
# num.sort()
# print(num)

## sorted function

# num = [9,10,6,5,3,1]
# print(sorted(num))

## reverse

## clear
# num.clear()
# print(num)

## copy

# num_copy = num.copy()
# print(num_copy)
# print(num)


###### "is" vs "==" comparison 

## ==, is

# fruits1 = ['orange','apple','pear']
# fruits2 = ['banana','kiwi','apple','banana']
# fruits3 = ['orange','apple','pear']

# print(fruits1 == fruits2)
# print(fruits1 == fruits3)

# print(fruits1 is fruits3)


######### Join and split methods -------> Video 89

## split method
## convert string to list

# user_info = "Siddhartha,19".split(",")
# print(user_info)


# name,age = "Siddhartha,19".split(",")
# print(name,age)
# print(name)
# print(age)

## join method
## convert list to string

# user_info = ["Siddharta","19"]
# print(",".join(user_info))



########### List vs Array -------> Video 90

## list vs array

## c, c++, java
## array int, string
## list - store any data / flexible
## python array module - fix data type
## numpy array - binding with c libraries
## javascript array = python list / flexible


########## List vs string ------> Video 91

## List vs strings

## strings are immutable
## lists are mutable

# s = "string"
# t = s.title()
# print(t)
# print(s)


# l = ["word1","word2","word3"]
# l.pop()
# l.append("word4")
# l.insert(1, "word5")### insert method
# print(l)



######## Looping in list ------> Video 92


# fruits = ["orange","apple","pear","banana","kiwi"]

## for loop
# for fruit in fruits:
#    print(fruit)
   
   
## While loop

# i = 0
# while i<len(fruits):
#    print(fruits[i])
#    i +=1


###### List inside list ------> Video 93


## list inside list
# matrix = [[1,2,3],[4,5,6],[7,8,9]]

# print(matrix[0])
# for i in matrix:
#        print(i)



# for sublist in matrix:
#    for i in sublist:
#       print(i)
      
      
# print(matrix[1][1])

## type fun

# s = "string"
# print(type(s))

# print(type(matrix))


########## More about list ------> Video 94

## generate lists with range function

# number = list(range(1,11))
# print(number)
# for i in number:
#        print(i)

## somthing more about pop method

# poped_item = number.pop()
# print(poped_item)
# print(number)

## index method

# print(number.index(1))

## pass list to a function

# def negative_list(l):
#       negative = []
#       for i in l:
#          negative.append(-i)
#       return negative
# print(negative_list(number))


####### Exercise ------> Video 95-96

## define a function which will take list contaning numbers as input
## and return list containing square of every element

## example
## numbers = [1,2,3,4]
## square_list(number) -----> return -----> [1,4,9,16]


# numbers = list(range(1,11))
# def square_list(l):
#    square = []
#    for i in l:
#       square.append(i**2)
#    return square
# print(square_list(numbers))

######## Exercise ----> Video 97-98

## define a function which will take list as a argument and this function
## will return a reversed list

## Example 
## [1,2,3,4] ----> [4,3,2,1]
## ["word1", "word2"] ---> ["word2", "word1"]

## Note you simply do this with reverse method or [::-1]
## but try to do this with the help of append and return method

# def reverse_list(l):
#    l.reverse()
#    return l

# def reverse_list(l):
#       return l[::-1]

# def reverse_list(l):
#    r_list = []
#    for i in range(len(l)):
#       popped_item = l.pop()
#       r_list.append(popped_item)
#    return r_list 

# numbers = [1,2,3,4]
# print(reverse_list(numbers))



########## Exercise -----> Video 99-100

## define a function that take a list of words as argument and 
## return list with reverse of every element in that list

## example 
## ["abc","tuv","xyz"] ----> ["cba","vut","zyx"]

# def reverse_elements(l):
#    element =[]
#    for i in l:
#       element.append(i[::-1])
#    return element

# word = ["abc","tuv","xyz"]
# print(reverse_elements(word))


#######  Exercise -----> Video 101-102

## filter odd even
## define a function 
## input 
## list ---> [1,2,3,4,5,6,7]
## output ----> [[1,3,5,7],[2,4,6]]

# def odd_even(l):
#    odd_nums = []
#    even_nums = []
#    for i in l:
#       if i % 2 == 0:
#          even_nums.append(i)
#       else:
#          odd_nums.append(i)
#    output = [odd_nums, even_nums]
#    return output

# num = [1,2,3,4,5,6,7]
# print(odd_even(num))



###### Exercise -----> Video 103-104

## Common element finder function 
## define a function which take 2 list as a input and return a list
## Which contains common elements of both list


## Example
## input----> [1,2,5,8],[1,2,7,6]
## output---> [1,2]

# def common_finder(l1,l2):
#    output = []
#    for i in l1:
#       if i in l2:
#          output.append(i)
#    return output

# print(common_finder([1,2,5,8],[1,2,7,6]))


###### Min and max function ------> Video 105

## min and max functions

# numbers = [6,60,2]

# print(min(numbers))
# print(max(numbers))

# def gratest_dif(l):
#    return max(l) - min(l)

# print(gratest_dif(numbers))


########## Exercise ------> Video 106-107

## function 
## [1,2,3,[1,2],[3,4]], input
## 2
## type()


# def sublist_count(l):
#    count = 0
#    for i in l:
#       if type(i) == list:
#          count += 1
#    return count 
# print(sublist_count([1,2,3,[1,2],[3,4]]))

##### Chapter Summary -----> 108



##### Intro to tuples -----> Video 109

## Tuples data structure
## Tuples can store any data type
## most important tuples are immutable, once tuples is created you can`t update
## data inside tuples


# example = ("one","two","three")
## no append, no insert, no pop, no remove
## days = ("monday", "tuesday")

## tuples are faster than list


### methods use in tuples
## count, index
## len function
## slicing

# print(example[:2])
# print(type(example))


######## More about tuples ------> Video 110

## looping in tuples 
## tuples with one element
## tuples without parenthesis
## tuple unpacking 
## list inside tuple
## some function that you can use with tuples

# mixed = (1,2,3,4,5,6,7.0)

## for loop and tuples

# for i in mixed:
#    print(i)

## Note - You can use while loop too



## Tuples with one element

# nums = (1,)
# words = ("word1",)
# print(type(nums))
# print(type(words))


## Tuple without parenthesis
# guitars = "yamaha","baton rouge","taylor"
# print(type(guitars))

## Tuples unpacking

# guitarists = ("Maneli Jamal","Eddie Van Der Meer","Andrew Foy")
# guitarist1,guitarist2,guitarist3 = (guitarists)
# print(guitarists)

## List inside tuples

# fav = ("Southern magnolia",["Tokyo Ghoul theme", "Landscape"])
# fav[1].pop()
# fav[1].append("We made it")
# print(fav)

### min(),max,sum --- We use these functions in tuples

# print(min(mixed))
# print(max(mixed))
# print(sum(mixed))



######## Function Returning two values ------> Video 111

## Function returning two values
# def func(int1,int2):
#    add = int1 + int2
#    multiply = int1*int2
#    return [add,multiply]

# print(func(2,3))

# add,multiply = func(2,3)
# print(add)
# print(multiply)

####### Tuples 4th Class ---------> Video 112

## Somthing more about tuples, list, str

# nums = tuple(range(1,11))

# nums = list((1,2,3,4,5,6,7,8,9,10))## Use list 
# nums = str((1,2,3,4,5,6,7,8,9,10))

# print(nums)
# print(type(nums))


######## Tuple Summary -----> Video 113

## Tuples 
## Tuples are immutable 
## Tuples are orderd collection of data 
## Tuples ca store any data 
## You cannot change (add or delete) Values from tuples once it created
## But can add, delete data from list which is present inside tuples


# mixed = (1,2,3,4,5,"Six")

## no append, no pop, no insert , no remove 
## Only count and index

## Functions 
## min(), max(), len(), sum()

# mixed2 = (1,2,3,4,5,[6,7,8])
# mixed2[5].pop()
# print(mixed2)


########## Intro to Dictionaries -------> Video 114

## Dictionaries Intro
## Q - Why we use dictionaries?
## A- Because of limitations of list , list are not enough to represent real data

## Example
# user = ["Siddhartha",24,["coco","kimi no na wa"],["awaking","fairy tale"]]
## This list coutains user name, age, fav movies, fav tunes
## You can do this but this is not a good way to do this.



## Q - What are dictionaries
## A - Unorderd collections of data in key : Value pair.


## How to create Dictionaries
# user = {"name" : "Siddhartha","age" : 19}
# print(user)
# print(type(user))


## Use Second method to create dictionary
# user1 = dict(name = "Siddhartha", age = 19)
# print(user1)

## How to access data from dictionary
## Note - There is no indexing because of unordered collection of data.

# print(user["name"])
# print(user["age"])


## Which type of data a dictionary can store?
## Anything
## Numbers, strings, list, dictionary

# user_info = {
#    "name" : "Siddharta",
#    "age" : 24,
#    "fav_movies" : ["coco","kimi no na wa"],
#    "fav_tune" : ["awaking","fairy tale"],  
    
# }

# print(user_info)
# print(user_info["fav_movies"])

## How to add data in empty dictionary

# user_info2 = {}
# user_info2["name"] = "siddhartha"
# user_info2["age"] = 19
# print(user_info2)


###### Looping & in keyword -----> Video 115
## In keyword and iterations in dictionary

# user_info = {
#    "name" : "Siddhartha",
#    "age" : 24,
#    "fav_movies" : ["coco","kimi no na wa"],
#    "fav_tune" : ["awaking","fairy tale"],  
    
# }

## Check if key exist in dictionary
# if "name" in user_info:
#    print("Present")

## Check if value exist in dictionary
# if "Siddhartha" in user_info.values():
#    print("Present")

# if 24 in user_info.values():
#    print("Present")
# else:
#    print("Not P.")

## Looping in dictionary

# for i in user_info.values():
#    print(i)

### Values method
# user_info_values = user_info.values()
# print(user_info_values)
# print(type(user_info_values))

### Keys method
# user_info_keys = user_info.keys()
# print(user_info_keys)
# print(type(user_info_keys))


# for i in user_info:
#    print(user_info[i])

#### items method

# user_items = user_info.items()
# print(user_items)
# print(type(user_items))

###
# for key, value in user_info.items():
#    print(f"Key is {key} and value is {value}")
   
# for i, j in user_info.items():
#    print(f"Key is {i} and value is {j}")


########## Add & delete data from dictionaries ----> Video 116

## add & delete data
# user_info = {
#    "name" : "Siddhartha",
#    "age" : 24,
#    "fav_movies" : ["coco","kimi no na wa"],
#    "fav_tune" : ["awaking","fairy tale"],  
    
# }

## How to add data
# user_info["fav_songs"] = ["s1","s2"]
# print(user_info)

## Pop Method 
# pop_item = user_info.pop("fav_tune")
# print(f"Pop item is{pop_item}")
# print(user_info)

## Popitem method

# pop_item = user_info.popitem()
# print(pop_item)
# print(user_info)


############ update() method----> Video 117

# user_info = {
#    "name" : "Siddhartha",
#    "age" : 24,
#    "fav_movies" : ["coco","kimi no na wa"],
#    "fav_tune" : ["awaking","fairy tale"],  
    
# }

# more_info = {"state" : 'UttarPradesh', "Hobbies" : ["coding","reading","guitar"]}

# user_info.update(more_info)
# print(user_info)


########## Fromkeys,get,clear,copy method ------> Video 118

## Fromkeys
## d = {"name" : "unknown", "age" : "unknown"}

# d = dict.fromkeys(["name","age","height"],"unknown")
# print(d)

## Get method 

# d = {"name":"Siddhartha", "age":19}
# print(d.get("name"))

# if "name" in d:
#    print("Prsent")
# else:
#    print("Not Present")
   
# if d.get("name"):
#    print("Present")
# else:
#    print("Not present")

## Clear method
# d.clear()
# print(d)

## Copy method
# d1 = d.copy()
# print(d1)


############ More about get() method -----> Video 119

## more about get, two same keys in dictionaries
# user = {"Name" : "Siddhartha","Age":19}
# print(user.get("Names", "not found ! "))


# user_1 = {"Name" : "Siddhartha","Age":19, "Age":20} ### update
# print(user_1)

####### Exercise ----> Video 120-121

## Exercise 
## Define a function that takes a number(n)
## return a dictionary containing cube of numbers from 1 to n

## Example
## cube_finde(3)
## {1:1, 2:8, 3:27}

## Cube finder

# def cube_finder(n):
#    cubes = {}
#    for i in range(1, n+1):
#       cubes[i] = i**3
#    return cubes

# print(cube_finder(10))


##### Word Counter Dictionary -----> Video 122

## Word count
## Siddhartha
# d= {"S" : 1, "i": 1, "h" : 2, "a" : 2, "h":2, "a": 2}
# print(d)

# def word_counter(s):
#    count = {}
#    for char in s:
#       count[char] = s.count(char)
#    return count

# print(word_counter("Siddhartha"))



########### Word Counter Dictionary ------> Video 122,123
#########  Eercise Solution ------> 123,124

# users = {
#    "name" : "Siddhartha",
#    "age" : 24,
#    "fav_movies" : ["coco","avanger"],
#    "fav_songs" : ["song1","song2"]
   
# }

# user = {}

# name = input("What is your name : ")
# age = input("What is your age : ")
# fav_movies = input("Your fav movies separated by comma ").split(",")
# fav_song = input("Your fav song separated by comma ").split(",")

# user["name"] = name
# user["age"] = age
# user["fav_movies"] = fav_movies
# user["fav_song"] = fav_song

# for i, j in user.items():## i = key, j = value.
#    print(f"{i} : {j}")
   

####### Summary -----> Video 125

## Summary dictionary
## What is dictionary
## unorderd collection of data

# d = {"name" : "Siddhartha", "age" : 24}

##or
# d1 = dict(name = "Siddhartha", age = 24)

##or

# d2 = {
#    "name" : "Siddhartha",
#    "age" : 24,
#    "fav_movies" : []
# }

## How to access data from dictionary
## You cannot do like
## d[0], because there is no order inside dictonary


## syntax
## print(dictname[keyname])
# print(d["name"])


## add data inside empty dict
# empty_dict = {}
# empty_dict["key1"] = "value1"
# empty_dict["key2"] = "value2"
# print(empty_dict)

## Check existance of value inside dict
## Use in keyword to check for keys
# if "name" in d:

## how to iterate over dictionary
## most common method

# for key , value in empty_dict.items():  
#       print(f"key is {key}, and value is {value}")

## to print all keys
# for i in empty_dict:
#    print(i)
   
##  to print all values
# for j in empty_dict.values():
#    print(j)

## most common dict methods

##get method 
## to access a key and check existance
## print(d.get("name"))

## Q - Why we use get
## A - to get rid of error
## example
# print(empty_dict["keys1"])
## use get
# print(empty_dict.get("keys1"))


### To delete item
## pop ---> take one argument which is keyname

# popped = empty_dict.pop("key1")
# print(popped)
# print(empty_dict)

########## Intro to sets -----> Video 126

## set data type
## unordered collection of unique items

# s = {1,2,3,2}
# print(s)
# print(type(s))

## list
# l = [1,1,2,3,4,5,5,5,6,7,7,8] 
## remove duplicate
# s2 = list(set(l)) ## use this also --> list(set(s2))
# print(s2)


## Add method 
# s.add(4)
# s.add(5)
# s.add(4) ## only one time add 4
# print(s) 

## remove method
# s.remove(3) ## if i use 3 --> 4 then show error.
# s.discard(4) ## no error
# print(s)

## clear method
# s.clear()
# print(s)

## copy method
# s1 = s.copy()
# print(s1)


####### More about sets ----> Video 127

## in keyword in sets and for loop

# s = {"a","b","c"}

## In keyword to check if items is present or not in set

# if "a" in s:
#    print("present")
# else:
#    print("present")
   
## for loop
# for item in s:
#    print(item)
   
### Set maths

# s1 = {1,2,3,4}
# s2 = {3,4,5,6}

## Union 

# union_set = s1 s2
# print(union_set)


## Intersection

# inter_set = s1&s2
# print(inter_set)



##### What is list comprehension ----> 128

## list comprehension
## with the help of list comprehension we can create of list in one line

## create a list of squares from 1 to 10

# square = []
# for i in range(1,11):
#       square.append(i**2)
# print(square)
##
# square2 = [i**2 for i in range(1,11)]
# print(square2)

### negative list
# negative = []
# for i in range(1,11):
#    negative.append(-i)
# print(negative)
##
# negative2 = [-i for i in range(1,11)]
# print(negative2)

##
# names = ["Sid","harshit","Mohit","Rohit"]
# new_list = [] ### take all the str`s 0th position in new_list
# for name in names:
#       new_list.append(name[0])
# print(new_list)
# ##
# new_list2 = [name[0] for name in names]
# print(new_list2)


###### Exercise ----> Video 129 -130

## Define a function that take list of strings
## list contaning reverse of every string

## Note - Use list Comprehension because we alredy did this exercise 
## using normal method

## Example 
## l = ["abc","tuv","xyz"]
## reverse_string(l) --> ["cba","vut","zyx"]

# def rev_str(l):
#    rev_s = []
#    for i in l:
#       rev_s.append(i[::-1])
#    return rev_s
# print(rev_str(["abc","tuv","xyz"]))


# def reverse_strings(l):
#    return [i[::-1] for i in l]
# print(reverse_strings(["abc","tuv","xyz"]))


##### List Comprehension with if statement ---> Video 131

# numbers = list(range(1,11))
# print(numbers)

## even nums
# nums = []
# for i in numbers:
#    if i%2 ==0:
#       nums.append(i)
# print(nums)


# ## 
# even_nums = [i for i in numbers if i%2 == 0]
# print(even_nums)

# odd_nums = [i for i in numbers if i%2 != 0]
# print(odd_nums)

#######  


