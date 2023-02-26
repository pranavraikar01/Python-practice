# #----file detection---
# import os
# path="C:\\Users\\Pranav\\Desktop\\pranav.txt"    #NOTE:Even if there are single back slash in original path edit it and add double where they are,also the file must exist
# if os.path.exists(path):
#     print("the location exists")
#     if os.path.isfile(path):
#         print("It is a file")
#     elif os.path.isdir(path):
#         print("It is a directory")
# else:
#     print("The location doesnt exist")




# #----reading a file----
# with open('pranav.txt') as file:            #if the file is not in our project folder then write its path with double backslash wherever single there are single backslash
#     print(file.read())                      #since we used 'with' while opening file it automatically closes the file if we dont write with then we have to close file manually
# #note the above code doesn't has any exception handling which is practically incorrect
# try:
#     with open('pranav.txt') as file:           #if file is not found then it throws an exception
#         print(file.read())
# except FileNotFoundError:
#     print("That file is not found")



# #-----writing in file---
# text="\n hello I am editing this file \n"
# with open('pranav.txt','w') as file:                   #'w' is written in code for writing in file but this overwrites the earlier content
#     file.write(text)
# with open('pranav.txt','a') as file:                   #'a' is written in code for appending content in file thus it doesnt overite the earlier content it appends it
#     file.write(text)



#---copy a file----
