# ""Inventory System:"" Create a dictionary of products with quantities. Write functions to:
inventory = {}

"""Add a product with its quantity to the inventory."""

def add_product(product, quantity):
    
    if product in inventory:
        inventory[product] += quantity #Used for adding the quantity if the product already exists
    else:
        inventory[product] = quantity


        """Remove a product from the inventory."""
def remove_product(product):
    if product in inventory:
        del inventory[product]          # Used for deleting the product from the inventory
        print(f"{product} has has been removed successfully.")
    else:
        print(f"{product} not found in inventory")

def update_quantity(product, quantity):
    """Update the quantity of a product in the inventory."""
    if product in inventory:
        inventory[product] = quantity
    else:
        print(f"{product} not found in inventory") 

def display_inventory(inventory):
    for product, quantity in inventory.items():
        print(f"{product} : {quantity}")

def search_product(product):
    if product in inventory:
        print(f"{product} : {inventory[product]}") 
    else:
        print(f"{product} not found in inventory")

while True:
    print("\nInventory Product Manu:")
    print("1. Add Product")
    print("2. Search Product")
    print("3. Update Product Quantity")
    print("4. Delete Product")
    print("5. Display All Poducts")
    print("6. Exit")

    choice = input("Enter your choice (1-6): ")

    if choice == '1':
        product = input("Enter Product name to add:")
        quantity = int(input("Enter a quantity You want to add:"))
        add_product(product, quantity)

        
    elif choice == '2':
        product = input("Enter Product name to search:")
        search_product(product)

    elif choice == '3':
        product = input("Enter Product name you want to update: ") 
        quantity = int(input("Enter new quantity:"))   
        update_quantity(product, quantity)

    elif choice == '4':
        product = input("Enter product you want to remove: ")
        remove_product(product)

    elif choice == '5':
        display_inventory(inventory)

    elif choice == '6':
        print("Exiting Inventory. Goodbye!")
        break

    else:
        print("Invalid choice. Please try again.")










        