#Task


#Code a Python program that will read from the text file inventory.txt and perform the following on the data, to prepare for presentation to your 
#managers:

# Inside this file, create a class named Shoes with the following attributes:
#● country,
#● code,
#● product,
#● cost, and
#● quantity.

#Inside this class define the following methods:
#▪ get_cost - Returns the cost of the shoes.
#▪ get_quantity -Returns the quantity of the shoes.
#▪ __str__ - This method returns a string representation of a class.

#Outside this class create a variable with an empty list. This variable will be used to store a list of shoes objects 
#Then you must define the following functions outside the class:
 
#▪ read_shoes_data - This function will open the file inventory.txt and read the data from this file, then create a shoes object with this data and append
#this object into the shoes list. One line in this file represents data to create one object of shoes. You must use the try-except in this function for 
#error handling. Remember to skip the first line using your code.
#▪ capture_shoes - This function will allow a user to capture data about a shoe and use this data to create a shoe object and append this object inside 
#the shoe list.
#▪ view_all - This function will iterate over the shoes list and print the details of the shoes returned from the __str__ function. Optional: you can 
#organise your data in a table format by using Python’s tabulate module.
#▪ re_stock - This function will find the shoe object with the lowest quantity, which is the shoes that need to be re-stocked. Ask the user if they 
#want to add this quantity of shoes and then update it. This quantity should be updated on the file for this shoe.
#▪ seach_shoe - This function will search for a shoe from the list using the shoe code and return this object so that it will be printed.
#▪ value_per_item - This function will calculate the total value for each item . Please keep the formula for value in mind; value = cost * quantity. 
#Print this information on the console for all the shoes.
#▪ highest_qty - Write code to determine the product with the highest quantity and print this shoe as being for sale.
#o Now in your main create a menu that executes each function above. This menu should be inside the while loop. 



#defining the class "Shoe"
class Shoe:

    
    #initialising the attributes of an object in this class
    def __init__(self, country, code, product, cost, quantity):
        self.country = country 
        self.code = code 
        self.product = product 
        self.cost = cost 
        self.quantity = quantity 
      
    
      #defining methods for the class 
    def get_cost(self):
        print(f"The cost of {self.product} is {self.cost} per unit")

    def get_quantity(self):
        print(f"There are {self.quantity} of {self.product} in stock")
    def __str__(self):
        print(f"{self.product}: {self.country},{self.code},R{self.cost}, {self.quantity} in stock")
        '''
        Add a code to returns a string representation of a class.
        '''


#=============Shoe list===========
'''
The list will be used to store a list of objects of shoes.
'''
shoe_list = []

#==========Functions outside the class==============

#this function adds all the shoes in the .txt file as Shoe objects to the empty shoe_list
def read_shoes_data():
    with open("inventory.txt","r+") as inventory:
        shoes = ""
        for lines in inventory:
            shoes+=lines
        empty = []
        empty = shoes.split("\n")
        for elements in empty:
            objecto = []
            objecto = elements.split(",")
            
            #a try- except block is used to skip over the first line, because a value error will be displayed because there is nothing 
            #that can be turned into an integer in the first line so a valueerror will occur
            try:
                objecto[2] = Shoe(objecto[0],objecto[1],objecto[2],objecto[3],objecto[4])
                skipfirstline = int(objecto[4])
                shoe_list.append(objecto[2])
            except ValueError:
                pass

#this function creates a new shoe object and adds it to  shoe_list 
def capture_shoes():
    print("To store a shoe in the catalougue please answer the following questions")
    product = input("What is the shoe product's name: ")
    codigo = input("What is the product code: ")
    country = input("Which centre is the product stored at: ")
    cost = input("What is the cost of one unit of the product: ")
    quantity = input("How many units are there: ")
    
    with open("inventory.txt","a+") as inventory:
        inventory.write(f"""
{country},{codigo},{product},{cost},{quantity}""")
        
    product = Shoe(country,codigo,product,cost,quantity)
    shoe_list.append(product)
    
    


#this function uses a for loop and a method defined in the Shoe class to print every shoe obejct in shoe_list as a readable string
def view_all():
    for Shoe in shoe_list: 
        Shoe.__str__()

#this function changes the value of the shoe's stock by changing the corresponding attribute of the object
def re_stock():
    stock = []
    for Shoe in shoe_list:
        stock.append(int(Shoe.quantity))
    #this looks for the shoe which is least in stock 
    current_stock = min(stock)
    index = stock.index(min(stock))
    
    shoe = shoe_list[index]
    shoe.__str__()
    #this shoe is then printed to the user and they are asked if they wish to restock it.
    try:
        #after the user enters a number then it is added to the previous stock and then the updated shoe object is printed
        restock = int(input("If you wish to restock this item, enter the number of units it will be restocked with: "))
        shoe.quantity = str(current_stock + restock)
        shoe.__str__()
        
        #the updated shoe item is then replaced with the old shoe object in the .txt file
        with open("inventory.txt","r+") as f:
            inventory = f.read()
            
        inventory = inventory.replace(f"{shoe.product},{shoe.cost},{current_stock}",f"{shoe.product},{shoe.cost},{shoe.quantity}")
        
        with open("inventory.txt","w") as file:
            file.write(inventory)
        
            
    #if the user does not enter a number then they are returned to the menu 
    except ValueError:
        print("You will be returned to the menu now")
        pass
    
    
    
# this function displays a specific shoe object that the user chooses
def search_shoe():
    
    user_shoe = input("What is the product name or code of the shoe you are looking for: ").lower()
    
    for shoe in shoe_list: 
        try: 
            if user_shoe == (shoe.product).lower() or user_shoe == shoe.code:
                print("Here is the product:")
                shoe.__str__()
        
        #if the user enters something invalid then an error message is printed
        except:
            print("Error: Product not found")
        
            
    pass
   
#this function calculates how much money is expected to be made by multiplying the stock by the price per unit 
def value_per_item():
    
    for shoe in shoe_list:
        value = int(shoe.cost) * int(shoe.quantity)
        shoe.__str__() 
        
        #the calculated information is displayed underneat each shoe object 
        
        print(f"Total Value: R{value}" +"\n")
    '''
    This function will calculate the total value for each item.
    Please keep the formula for value in mind: value = cost * quantity.
    Print this information on the console for all the shoes.
    '''
    
    
#this function looks for the shoe with the highest quantity and prints a message saying it is for sale
def highest_qty():
    stock = []
    for Shoe in shoe_list:
        stock.append(int(Shoe.quantity))
    

    index = stock.index(max(stock))
    shoe = shoe_list[index]
    shoe.__str__()
    print("This shoe has the highest number in stock and is for sale")
    '''
    Write code to determine the product with the highest quantity and
    print this shoe as being for sale.
    '''

#callijng the function that adds all the shoes from inventory.txt to shoe_list 
read_shoes_data()
#==========Main Menu=============

#this while loop displays the menu to the user and calls the respective functions depending on what the user enters 
while True:
    
    
    menu = input("""
                 
Welcome to the Nike Inventory. Please select one of the following menu items:
    c - Add a new product to the inventory 
    va - View all the current products in the inventory
    re - Restock a product in the inventory 
    s - Search for a specific shoe 
    tv - Show the total value of each product 
    ms - Show the product that is most in stock at the moment
    e - exit
    
    """).lower()
    
    menu =  menu.replace(" ","")
    
    if menu == "c":
        capture_shoes()
    
    if menu == "va":
        view_all()
    
    if menu == "re":
        re_stock()
        
    if menu == "s":
        search_shoe()
    
    if menu == "tv":
        value_per_item()
        
    if menu == "ms":
        highest_qty()
    
    if menu == "e":
        print("Program Stopping...")
        break
    
    else:
        pass

    
    
    
    
    



