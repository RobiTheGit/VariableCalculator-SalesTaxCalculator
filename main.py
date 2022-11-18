import varis #import varis.py
import sys #import the sys module

    
items = [] #make items a blank vairable
item= '' #make item a blank variable

varis.tax = varis.tax + 1 #for easy math
    
def calc(): #the calculating function, all of the ifs are the same except for the else and different numbers
    global item #make item a global variable
    global i #make i a global variable
    thing = input('What item would you like to buy? ') #ask for the item wanted to be bought
    quant = int(input(f'How much of {thing} would you like to buy? '))  #ask for the quantity of the last item
    if thing in varis.thinglist: #does thing equal the first tiem of the list
        if quant < 1000000: #test if quant is less than 1 million
            x = varis.thinglist.index(thing) #set x to the item
            i = float(varis.costlist[x]) #set i to the cost of the item
            price = round((i*varis.tax)*int(quant), 2) #calculate the price of the item with sales tax
            print('$',price) #print the price with sales tax
            print(varis.mesage2) #print a message I have in the varis.py code
            item = float(i)*float(quant) # set item to the price * quantity
            items.append(item) #append the non sales tax affected item into the items list
            recurse()        #loop
        else:
            print('1 million dollars!') #simple print statement for an easter egg
            price = 1000000 #set the price to $1,000,000
            items.append(price) #append the price onto the items list
            recurse() #loop
            
    else: #here is the difference
        if quant < 1000000: #test if quant is less than 1 million
            item = float(input("I don't have that on my list, what is the base price? ")) #ask for the basic price, can have decimals
            price = round((item*varis.tax)*int(quant), 2) #price is the round of the item price * tax all times the quantity
            it = float(item)*float(quant) #set the price of the item to the item price * quantity
            items.append(it) # append the price to the items list
            print('$',price) #print the price with sales tax applied
            print(varis.mesage2) #print a message i have in varis.py
            recurse() #loop

        else:
            print('1 million dollars!') #simple print statement for an easter egg
            price = 1000000.00 #set the price to $1,000,000
            items.append(price) #append the price onto the items list
            recurse()  #loop 
    
    
def init(): #the initialization function, doesn't do much
    print(varis.logo)
    print(f"The items are") # simple print statement
    for x in range(len(varis.thinglist)): # for the ammount of items in varis.thinglist...
        print(varis.thinglist[x]) #print the item 
    calc() #if so, calculate

def recurse(): #the loop function
    choice = input('Would you like to keep shopping(yes/no answer those only)? ') #ask if the user wants to keep going with this
    if choice == 'no': #see if the choice is no
        total = round((float(sum(items))*float(varis.tax)), 2)# calculate the total
        print('Your total is $',total) #print the total out
        sys.exit(0) #exit the program
    else:
        init() #run the init code
    
init()#run the init code
