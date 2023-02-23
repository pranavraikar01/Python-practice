# age=19
# name="pranav"
# attractive=True
# print(type(name))
# print("pranav"+str(age))


# name,age,handsaome="pranav",20,True
# print(name,handsaome,age)


# name="pranav"
# print(name.capitalize())


# x=1
# y=str(x)
# print(type(y))


# a="45"
# print(float(a))
# x=34
# print("the number is :"+ str(x))


# name=input("what is your name")
# print("hello"+name)
# a=int(input("enter  a number"))
# b=int(input("enter  a number"))
# print("Addition is:"+str(a+b))


# import math
# pi=3.14
# x,y,z=1,2,3
# print(round(pi))
# print(math.ceil(pi))  
# print(math.floor(pi))
# print(abs(pi))
# print(math.pow(pi,2))
# print(math.sqrt(pi))
# print(max(x,y,z))
# print(min(x,y,z))


# #---string slicing---
# #string_name[start:end:step]    here start is inclusive,end is exclusive and step is used for skipping in between characters of string if we not write step then no characters will be skipped
# name="Pranav Sandeep Raikar"
# first_name=name[0:7]  
# print(first_name)
# last_name=name[15:]
# print(last_name)
# funky_name=name[::2]
# print(funky_name)
# #the syntax used in funkyname is also allowed in which the start and end of original string is considered as start and end 
# reversed_name=name[::-1]
# print(reversed_name)
# #****slicing using slice function*********
# website1="https//google.com"
# website2="https//wikipidea.com"
# slice=slice(7,-4)
# print(website1[slice])
# print(website2[slice])


#*****conditional statements*************
# age=int(input("How old are you?:"))
# if age==100:
#     print("You are very old")
# elif age>=18:
#     print("you are an adult")
# elif age==0:
#     print("you havent born yet")
# else:
#     print("You ARE A CHILD")


#*****logical operators*************
# temp=int(input("what is the temperature outside:"))
# if temp >=0 and temp <=30:
#     print("the temperature is good today")
#     print("you can go outside")
# elif temp <0 or temp >30:
#     print("stay at home")
# if not(temp >=0 and temp <=30):
#     print("the temperature is good today")
#     print("you can go outside")
# elif not(temp <0 or temp >30):
#     print("stay at home")


#---while loop-----
# name=""
# while len(name)==0:
#     name=input("enter your name:")
# print("hello "+name)


#---for loop-----
# for i in range(10):   #here 10 is exclusive
#     print(i)
# for i in range(50,100):   #here 50 is inclusive and 100 is exclusive
#     print(i)
# for i in range(30,100,2):   #here 2 is the increment
#     print(i)
# for i in "Pranav Raikar":     #here for loop is used on string
#     print(i)

# import time
# for seconds in range(10,0,-1):
#     print(seconds)
#     time.sleep(1)    #here for loop executes every iteration after one second
# print("happy new year")


#---neasted for loop-----            it can be used for drawing patterns
# rows =int(input("how many number of rows are there: "))
# columns=int(input("how many columns: "))
# symbol=input("enter a symbol to use: ")
# for i in range(rows):
#     for j in range(columns):
#         print(symbol,end="")
#     print()


#--loop control statements------
while True:
    name=input("enter your name: ")
    if name!="":
        break
print("while loop is broken")