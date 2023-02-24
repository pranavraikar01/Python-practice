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


##-----set----   it is a collection which is unordered and,unindexed.No duplicate values it is faster than a list
# utensils={"knife","spoon","fork"}
# dishes={"bowl","plate","cup"}

# utensils.add("napkin")                   #adds new value in the set
# utensils.remove("fork")                  #removes value from the set
# utensils.update(dishes)                  #adds one set into another
# dinner_table=utensils.union(dishes)       #adds one set into other   if we do intersection then what is common between both that is written 
# print(utensils.difference(dishes))          #prints what utensils has that dishes doesn't
# for i in utensils:              
#     print(i)                    #it prints in an unordered fashion
# for j in dinner_table:
#     print(j)



# #-----dictionary--- a changeble unordered caollection of uniwue key:value pairs it is fast becoause uses hashing 
# Capitals={'USA':'Washington dc',
#           'India':'new Delhi',
#           'China':'Bejing',
#           'Germany':'Berlin'}
# print(Capitals.get('India'))          #we have to give input as key then here in code then it will give the value of that keya as output
# print(Capitals.get('Russia'))          #since there is no key as Russia it gives None as output
# print(Capitals.keys())                  #prints all the keys
# print(Capitals.values())                #prints all the values
# Capitals.update({'USA':'CALIFORNIA'})        #changes the value of key
# Capitals.update({'Spain':'Paris'})            #adds new key value pair
# print(Capitals.items())                 #prints both keys and values
# Capitals.pop('China')                   #deletes some key value pair using key from dictioanry
# for key,value in Capitals.items():      #also prints both keys and values
#     print(key,value)
# Capitals.clear()                        #clears the dictionary



# #-----index operator [] =gives access to a sequenc's element(str,list,tupples)---
# name="pranav raikar"
# if(name[0].islower()):          
#     name=name.capitalize()          #checks name is in lower case if yes then it capitalizes it we can do it vice versa too
# print(name)
# first_name=name[:3].upper()         
# print(first_name)
# last_name=name[4:].lower()
# print(last_name)
# last_character=name[-1]
# print(last_character)

