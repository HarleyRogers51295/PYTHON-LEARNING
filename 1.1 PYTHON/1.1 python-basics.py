
#printing out strings to the command console
print("------------PRINT------------")
print("YO I'm using quotes jank!")
print('YO "This term" is in double quotes')
print('yo here we use \'backslash\' dawg')

#variables
#the names are in snake case my_variable, python runs top down. Must make the meaning of the cvaribale first before you call the variable
print("------------VARIABLE------------")
my_message = "herro!"
print(my_message)

#sting concatenation
print("------------CONCATENATION------------")
string_1 = "Hello"
string_2 = "world"
print(string_1 + " " + string_2)
print("hello" + " " + "world!")
print("------------CON + ID'S------------")
both_messages = string_1 + " " + string_2
print(both_messages)
print(id(both_messages))
both_messages = string_2 + " " + string_1
print(both_messages)
print(id(both_messages))
#You will see different ids for both of these. They are the same variable but since it changes the ID changes

#Indexing
print("-----------INDEXING-----------")
name = "Interstellar"
print(name[0])
print(name[5])
#so on and so forth
print(name[-1])
print(name[-5])
#start from the back if you dont know the length of your string


#slicing
print("----------SLICING----------")
print(name)
print(name[0:5]) #when you have a stop index
print(name[5:]) #any point to the end
print(name[:]) #gives the whole sting
print(name[2:9:2]) #this step size, the third entry makes it skip some. in this case it skips one index. 1 is set by default
print(name[::-1]) #reverse a sting cool stuff!