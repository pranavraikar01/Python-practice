# #-----lists------
# food=["Pizza","burger","shwarma"]
# # print(food)
# # print(food[0])
# # food[1]="vadapav"      #we can change the elements of list
# # print(food[1])
# food.append("icecream")
# food.remove("Pizza")
# food.pop()                      #removes last element of list
# food.insert(1,"cake")            #inserts at certain position of list
# food.sort()                      #sorts the list
# for i in food:   
#     print(i)
# food.clear()                      #deletes the list


# #-----2Dlists------
# drinks=["cofee","soda","tea"]
# dinner=["chapati","rice","daal"]
# lunch=["bhaji","bhakri","fish"]
# food=[drinks,dinner,lunch]
# food[0][0]="solkadhi"
# print(food)


# #-----tupples----    it is collection of data which is ordered and is unchangeble and unlike list we can store duplicate data in tupple
# student=("Pranav",20,"male","Pranav")
# print(student.count("Pranav"))          #counts how many times pranav is repeated
# print(student.index("Pranav"))          #gives the index position of pranav if repeated then it gives index of word which comes first
# for i in student:
#     print(i)
# if "Pranav" in student:                 #checks whether pranav is there in the tupple or not
#     print("hello pranav")