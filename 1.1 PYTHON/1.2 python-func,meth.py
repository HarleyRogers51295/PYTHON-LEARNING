import string

greeting = "hello"
user = "Harley"
message = "        What up foo!"
message_two = "what-Up-Dock?"
my_list = ['hello', 'darkness', 'my', 'old', 'friend']
print(greeting, user, message)

print("---------Built In Functions---------")
print(len(greeting)) #length of a string
print(type(greeting)) #type of object
print(type(5))
print(id(user)) #gives ID number, memory location

print("---------Built in Methods------------")
print(greeting)
print(greeting.capitalize())
#print(dir(user)) #this function displays all the methods available
print(greeting.upper()) #turns all to upper
print(user.lower()) #turns all to lower
print(user, message.strip().lower()) #strip takes away unwanted space, this is also a expample of chaining methods together
print(greeting.find('e')) #gives the index of the requested string
print(greeting.find('b')) #returns a -1 if the wanted char is not in the string
print(message.split()) #breaks up the string, turns it into list.
print(message_two.split('-')) #you can specify what you want to split on, needs the ' '
print(" ".join(my_list)) #joins together a list into a string. Must put what you want to join on. ex. " "

print(string.ascii_lowercase) #this prints out the alphabet. must have the import string at the top for it to work

