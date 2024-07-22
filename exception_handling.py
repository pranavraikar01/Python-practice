# #-----exception-----   events detected during execution that interrupt the flow of program are called execeptions and their handling is called as exception handling
# try:                                                            #in try block we write the code in which we feel exception may occur
#     numerator=int(input("enter a number to divide:"))
#     denominator=int(input("enter a number to divide by:"))
#     result=numerator/denominator
# #so while coding in real life always check first the possible exceptions by running the code without try then we can see the possible exceptions
# #thus accordingly write the specific exept blocks for the code
# except ZeroDivisionError as e:                                  #even if we dont write ' as e' it is okay its just a standard practice
#     print("You cant divide by zero")                            #this exception occurs when number is divided by zero
# except  ValueError as e:
#     print("Enter only numbers plz")                             #this exception occurs when number is divided by non int number
# except Exception:
#     print("Something went wrong")                             #even if we write this much and not specify the above exceptions it is okay but it is good to specify them as below
# # except Exception as e:
# #     print("exception:"+str(e))                             #even if we write this much and not specify the above exceptions it is okay but it is good to specify them
# else:
#     print(result)
# finally:
#     print("this will always excecut")                           #this always executes even if exception occurs or not

