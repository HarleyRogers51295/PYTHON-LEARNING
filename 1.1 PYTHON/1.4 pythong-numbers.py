import math
import random

print("-------------BASICS & MATH--------------")
#integer is a whole number ex. 4, 500, 67, 2........ no decimals
#float has a decimal point ex. 1.521346584 .....
#python auto changes these for you if you do 1 + 1.5 it will be 2.5.
#you can use +, -, /, *, %, **(to the power of!)
print(abs(-50)) #returns the positive of the number entered
print(abs(50))
print(10 + 5)
print(10 - 5)
print(10 * 5)
print(10 / 5)
print(10 % 5)
print(10 ** 5) 
print(math.pow(10, 5))
print(math.log2(100000000)) #this will come up in the algo area
print(random.randint(0, 1000)) #random number generator


print("--------------TYPE CASTING-------------")
result = "10" + "10"
print(result)
#type cast as such!
result = int("10") + int("10") ##typically used with variuables. look below.
print(result)
print(type("10"))

num_1 = "20"
num_2 = "14"
result = int(num_1) + int(num_2) # change to int
print(result)
print(type(result))

num_3 = 10
num_4 = 45
result_2 = num_3 + num_4
result_2= str(result_2) #chamge to string
print(result_2)
print(type(result_2))

####CANNOT CONVERT things that are not numbers to an int! ex, harley cannot be a number.#### 


print("--------------INPUT FROM USER-------------")

print("Welcome here! PLease enter yur numbers to be multiplied!")
print("-" * 30)
num_5 = input("Enter Your first number here: ")
num_6 = input("Enter Your second number here: ")
result_3 = int(num_5) * int(num_6)
print(result_3)