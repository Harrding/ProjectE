"""
    This file contains the class of products which has price, id, and quantity
    as its variables. Also there will be an inventory class which contains
    multiple products and will be able to sum up the quantity of products.

    What I added in this program is that when the user enters an Id value that
    already exists inside of the current inventory, the prompt will request for
    them to re enter another value. The prompt will also print out the ID values
    that have already been used in the line above the new prompt. 
"""

class Product:
    def __init__(self, id, price, quantity):
        self.id = id
        self.price = price
        self.quantity = quantity
    def getQuantity(self):
        return self.quantity
    def getPrice (self):
        return self.price
    def getId(self):
        return self.id
    def __str__(self):
        return "Product " + id

class Inventory:
    def __init__(self, *products):
        if(len(products) > 0):
            self.inventoryProducts = products[0]
        else :
            self.inventoryProducts = []
    def countInventory(self):
        quantityProducts = 0
        for x in self.inventoryProducts:
            quantityProducts+= int(x.getQuantity())
        return quantityProducts
    def printInventory(self):
        print(self.inventoryProducts)
        for x in self.inventoryProducts:
            print(x)
    def addProduct(self, newProduct):
        self.inventoryProducts.append(newProduct)
    def checkId(self, idValue):
        for x in self.inventoryProducts:
            if(x.getId() == idValue):
                return False
        return True
    def printIds(self):
        for x in self.inventoryProducts:
            print(x.getId(), end = "  ")
            

numProducts = input("Enter the number of products you would like to enter : ")
currentInventory = Inventory()
for x in range(1, int(numProducts)+1):
    isRepeat = True
    while(isRepeat):
        id = input("Enter the id number for product " + str(x) + " : ")
        isRepeat = not currentInventory.checkId(id)
        if(isRepeat):
            print("You did not enter a valid ID number, because it is already in use. Please enter a different "
                  + "valid value to continue. The used ID numbers so far include : " )
            currentInventory.printIds()
            print()
    price = input("Enter the price for product " + str(x) + " : ")
    quantity = input("Enter the quantity for product " + str(x) + " : ")
    newProduct = Product(id, price, quantity)
    currentInventory.addProduct(newProduct)
print("The inventory space currently contains " + str(currentInventory.countInventory()) + " products")
    
