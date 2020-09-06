stock_price = "1000" #different ways to print out
yesterdays_price = "5000"

print("-----------String Formatting------------")
print("Today's price for google stock is: " + stock_price)
print("Today's price for google stock is:", stock_price)
print("Today's price for google stock is: {}".format(stock_price))
print(f"Today's price for google stock is: {stock_price}") #string interpilation, best way!
print(f"Todays Price: {stock_price}, Yesterdays Price: {yesterdays_price}")

print("------------Special Characters---------------")
print("my name is bub \
    i like tacos \
    Do you like tacos? ")  #multiline srings? 
print("This is a random jank thing \nto demonstrat stuff you knoe.") #\n moves the rest to the next line
print("here is some more \tjank for us to use this \tis the tab method you know. we use the \\t")
