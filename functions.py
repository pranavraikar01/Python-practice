# #-------Functions----  it is a block of code which is executed only when it is called
# def hello(first_name,last_name):
#     print("hello " + first_name +" "+ last_name)
#     print("have a nice day")
# hello("Pranav","Raikar")    #function called
# first_name="Pranav"
# last_name="Raikar"
# hello(first_name,last_name)      #function can also be called by giving variables created earlier as a argument


# #------Function with return statement-----
# def add(a,b):
#     return a+b
# print(add(3,5))


# #---keyword arguments----  
# #usually when we pass arguments to a function call we are supposed to pass the arguments in same order as of function definition
# #when we use keyword arguments there is no need to do so for that we have to give the function arguments of function definition as keywords while calling the function
# def hello(first,middle,last):
#     print("hello " +first+ " "+middle+" "+last)
# hello(last="Raikar",first="Pranav",middle="Sandeep")


# #---Nested function calls---      function calls inside other functioon calls,innermost function call is resolved first,returned value is used as argument for outer one 
# print(round(abs(float(input("enter a integer: ")))))



# #----variable scope---  The region taht a variable is recognized
# #                       variable is only available from inside the region it is created it can be global or local
# name="Pranav"                   #global variable
# def display_name():        
#     name="Raikar"          #local variable note:if local variable is not there in function then the function uses the global variable 
# #                           python follows LEGB=LOCAL,ENCLOSING,GLOBAL,BUILT-IN variables i.e if local not there then function checks for enclosing
# #                           function and so on
#     print(name)
# display_name()
# print(name)



# #----args--- parameter that will pack all arguments into a tupple  useful so that a function can accept a varrying amount of arguments
# def add(*data):             #name can be any thing but when we send tupple as argument  * sign is compulsory
#     sum=0
#     data=list[data]    #type casting because we want to change specific value in tupple but tupple does not allow indexing
#     data[0]=0           #thus data at 0 position is changed from 1 to 0
#     for i in data:
#         sum=sum+i
#     return sum
# print(add(1,2,3,4,5,6))     #here data is a tupple thus we can send any number of data to the function with the use of tupples since tupples are iterable in a function



# #-----**kwargs---- parameters that will pack all arguments in a "dictionary" useful so that a function can accept a varrying amount of keyword argument
# def hello(**kwargs):
#     print("hello "+kwargs['first'])
#     print("hello",end=" ")
#     for key,value in kwargs.items():
#         print(value,end=" ")
# hello(title="Master",first="Pranav",middle="Sandeep",last="Raikar")



# #-----str.format()---     optional method that gives users more control when displaying output
# animal="cow"
# planet="earth"
# print("the {} walks on the {}".format(animal,planet))                              #{}is called as foramt field
# print("the {1} walks on the {0}".format(animal,planet))                            #positional argument here position of data comming inside{} is specified in the code
# print("the {animal} walks on the {planet}".format(animal="Dog",planet="Moon"))           #keyword argument
# text="The {} walks on the {}"
# print(text.format(animal,planet))                                           #different way of using .format
# name="pranav"
# print("hello my name is{:<10},nice to meet you".format(name))          #adds space where {} is used it can be after data from {} or also before data from{} as shown below
# print("hello my name is{:>10},nice to meet you".format(name))    
# print("hello my name is{:^10},nice to meet you".format(name))             #we can also show the data from {} in the centre of space where {} is present
# number=1000
# print("the number  is: {:.2f}".format(number))                          #prints value of pi upto two decimal
# print("the number is {:b}".format(number))             #prints the binary equivalent of given number same can be done for ortho ,hexadecimal as shown below
# print("the number is {:o}".format(number))               #prints the number in orthogonal system
# print("the number is {:X}".format(number))                  #prints the number in hexadecimal system
# print("the number is {:E}".format(number))                #prints the number in scientific notation



# #-----random numbers----    
# import random
# x=random.randint(1,6)                   #creates a random number between 1 and 6
# print(x)
# y=random.random()                       #creates random floating point number
# print(y)
# mylist=['rock','paper','pen']
# z=random.choice(mylist)                    #creates random from the list
# print(z)
# cards=[1,2,3,4,5,"j","k","l","m"]

# random.shuffle(cards)                   #shuffles the members of the list
# print(cards)
