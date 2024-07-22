# age=19
# name="pranav"
# attractive=True
# print(type(name))
# print("pranav"+age) #We cannot concatenate a string directly with a different data type like int it will throw typeerror
# print("pranav"+str(age)) #Thus to concatenate a string directly with a different data type like int we will have to do type casting


####Multiple assignment=allows us to assign multiple variables at the same time in one line of code
# name,age,handsaome="pranav",20,True
# print(name,handsaome,age)
# pranav=harsh=lay=shailesh=True ## Assigns all of them true together in one line of code

# ##Walrus operator
# # print(name="Pranav") ## This will throw error TypeError: 'name' is an invalid keyword argument for print() 
# ##But we can achieve above functionality using the :
# print(name:="Pranav")  ##Here we assigned values to variables as part of a larger expression


# name="pranav"
# print(len(name)) ###Gives the length of the string
# print(name.find("p")) ##Retruns the index of the letter passed as parameter, present in the string
# # print(name.capitalize())
# print(name.upper())
# print(name.lower())
# print(name.isdigit())
# print(name.isalpha())
# print(name.count("a")) ##Counts the number of occurences of the given string
# print(name.replace("r","a"))
# print(name*3)  ##Concatenate the string with its copy the number of times multiplication is done





##Type casting = is used to convert the data type of a value to another data type
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
# #string_name[start:stop:step]    here start is inclusive,end is exclusive and step is used for skipping in between characters of string if we not write step then no characters will be skipped
# name="Pranav Sandeep Raikar"
# first_name=name[0:6]  
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
# slice=slice(7,-4) ##slice is an object 
# print(slice)
# print(website2[slice])


# #*****conditional statements*************
# age=int(input("How old are you?:"))
# if age==100:
#     print("You are very old")
# elif age>=18:
#     print("you are an adult")
# elif age==0:
#     print("you havent born yet")
# else:
#     print("You ARE A CHILD")


# #*****logical operators*************
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


# #---while loop-----
# name=""
# while len(name)==0:
#     name=input("enter your name:")
# print("hello "+name)


# #---for loop-----
# for i in range(10):   #here 10 is exclusive
#     print(i)
# for i in range(50,100):   #here 50 is inclusive and 100 is exclusive
#     print(i)
# for i in range(30,100,2):   #here 2 is the increment
#     print(i)
# for i in "Pranav Raikar":     #here for loop is used on string
#     print(i)
# for i in range(1, 8): #Output:1,2,3,4,5,6,7
#    print(i)
#    i += 2 ##This will not at all affect the execution or incrementation in for loop because In a for loop in Python, the iteration variable is controlled by the loop itself, and changes to the iteration variable within the loop body do not affect the sequence of values that the loop iterates over.


# import time
# for seconds in range(10,0,-1):
#     print(seconds)
#     time.sleep(1)    #here for loop executes every iteration after one second
# print("happy new year")



# #---neasted for loop-----            it can be used for drawing patterns
# # Read the number of rows from the user
# rows = int(input("how many number of rows are there: "))

# # Read the number of columns from the user
# columns = int(input("how many columns: "))

# # Read the symbol to use from the user
# symbol = input("enter a symbol to use: ")

# # Outer loop iterates over each row
# for i in range(rows):
#     # Inner loop iterates over each column in the current row
#     for j in range(columns):
#         # Print the symbol without moving to a new line
#         print(symbol, end="")
#     # After the inner loop, print a newline to move to the next row
#     print()



# #----loop control statements------
#      #--break--
# while True:
#     name=input("enter your name: ")
#     if name!="":
#         break
# print("while loop is broken")

#         #--continue--
# phone_number="123-456-789"
# for i in phone_number:
#     if i=="-":
#         continue
#     print(i,end="")   #writes all digits in same line here

#          #--pass--
# for i in range(1,21):
#     if i==13:
#         pass                    #pass skips the content given in that if condition
#     else:print(" "+ str(i),end="")    



