import time


print("This is Python 2")

name = input("To start off, What your name?? \n" )





if name == "sockey":
    print("Not today sockey \n")
    exit()
else:
    print("Hello " + name , ", Thank you! for joining on with python ")
    
price = 3
menu = "cake , rice , chips \n water, milk , chciken wings "
soda = "Coko , sprit ,  dr.papaer "


time.sleep( .5 )
print(".. \r")
time.sleep(.6)
print("... \r")
time.sleep(.5)
print(name, "Here is the menu \n " ,menu)
time.sleep(1)

input("Call me over when you are ready to oder sir " +  name + "\n" )


like = input("I heard that your are ready to oder " + name + " So what would you like to have today, ")
many = input("How many " + like + " would you like?")
total = price * int(many)
time.sleep(.9)
print("Great, Your total is $" + str(total) )
time.sleep(.8)
print("Sounds good" , many , like,"will be ready in a moment")













