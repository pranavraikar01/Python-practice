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
# #                       Avaialable is only available from inside the region it is created it can be global or local
# name="Pranav"                   #global variable
# def display_name():        
#     name="Raikar"          #local variable note:if local variable is not there in function then the function uses the global variable 
# #                           python follows LEGB=LOCAL,ENCLOSING,GLOBAL,BUILT-IN variables i.e if local not there then function checks for enclosing
# #                           function and so on
#     print(name)
# display_name()
# print(name)

