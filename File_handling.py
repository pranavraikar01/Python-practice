# #----file detection---
# import os
# path="C:\\Users\\Pranav\\Desktop\\python practice\\vesit.txt"    #NOTE:Even if there are single back slash in original path edit it and add double where they are,also the file must exist
# if os.path.exists(path):
#     print("the location exists")
#     if os.path.isfile(path):
#         print("It is a file")
#     elif os.path.isdir(path):
#         print("It is a directory")
# else:
#     print("The location doesnt exist")




# #----reading a file----
# with open('vesit.txt') as file:            #if the file is not in our project folder then write its path with double backslash wherever single there are single backslash
#     print(file.read())                      #since we used 'with' while opening file it automatically closes the file if we dont write with then we have to close file manually
# #note the above code doesn't has any exception handling which is practically incorrect
# try:
#     with open('vesit.txt') as file:           #if file is not found then it throws an exception
#         print(file.read())
# except FileNotFoundError:
#     print("That file is not found")



# #-----writing in file---
# text="\n hello I am  editing this file \n"
# # with open('vesit.txt','w') as file:                   #'w' is written in code for writing in file but this overwrites the earlier content
# #     file.write(text)
# with open('vesit.txt','a') as file:                   #'a' is written in code for appending content in file thus it doesnt overite the earlier content it appends it
#     file.write(text)



# #---copy a file----
# #copyfile() = copies conntents of file
# #copy() =copyfile() + prmission mode + destination can be a directory
# #copy2() = copy() + copies matadat(file's creation and modification times)
# import shutil           #in this module there are copyfile(),copy(),copy2() functions
# shutil.copyfile('vesit.txt','copy.txt')        #sorce,destination must be given as argument to function NOTE:destination file is automatically created wherever source is present




# #---move a file---- 
# import os
# source="copy.txt"
# destination="C:\\Users\\Pranav\\Desktop\\movedcopy.txt"     #destination where the file is to be moved
# try:
#     if os.path.exists(destination):
#         print("there already a file exists")
#     else:
#         os.replace(source,destination)
#         print(source +" i.e the file is moved")
# except FileNotFoundError:
#     print(source + "was not found")
# # NOTE:we can also do the same above process of moving file for a folder




# #---delete a file---        NOTE:whenever you run these code in future for files first check they are present or deleted during the early execution
# import os
# import shutil
# path='sample.txt'
# try:
#     os.remove(path)             #deletes a file
#     #os.rmdir(path)             #deletes a file or empty folder
#     #shutil.rmtree(path)        #delete files and or folders
# except FileNotFoundError:
#     print("file was not found")
# except PermissionError:
#     print("You do not have permission to delete the file")
# except OSError:
#     print("You can delete that only by shutil.remove method")
# else:
#     print(path +" was deleted")





# #-----module---    a file containing python code.May contain functions,classes,etc. 
# #                  used with modular programming,which is to seperate a program into parts 
# import modules as msg               #as msg here is just usde for giveing the the usage of module a specific name in this module
# msg.hello()
# msg.bye()
# #the above syntax can be also written:
# #from modules import hello,bye   #NOTE: Then we dont have to write msg.bye() we have to write only bye() while calling the function bye
# #if we are working on large program then we can use:  from modules import *
# #NOTE: for knowing the inbuilt modules of python we have in our system type :-  help("modules")
