# PART 1:
# Define the ItemToPurchase class, which models an item with a name, price, and quantity
class ItemToPurchase:
    # Constructor: Initializes item attributes with default values
    # if no parameters are provided
    def __init__(self, item_name="none", item_price=0, item_quantity=0, item_description=""):
        # attributes
        self.item_name = item_name
        self.item_price = item_price
        self.item_quantity = item_quantity
        self.item_description = item_description  # Added item description

    # Method to print the cost of an individual item (qty * price).
    def print_item_cost(self):
        total_cost = self.item_price * self.item_quantity
        # Output and format the item name, quantity, price and total cost
        print(f'{self.item_name} {self.item_quantity} @ ${self.item_price:.2f} = ${total_cost:.2f}')

# PART 2:
    # Method to return the total cost of an item used for total cost calculations.
    # This method returns the total cost of an item by multiplying the item price by the item quantity.
    def get_total_cost(self):
        return self.item_price * self.item_quantity

# Define the ShoppingCart class for the user's shopping cart.
class ShoppingCart:
    # Parameter constructor initializes user and cart details.
    # Default values are set for the customer name and date.
    def __init__(self, cust_name='none', cur_date='January 1, 2020'):
        # Attributes
        self.cust_name = cust_name
        self.cur_date = cur_date
        self.cart_items = []

    # Method to add items to the cart.
    # This method takes an item object as a parameter.
    def add_item(self, item):
        self.cart_items.append(item)

    # Method to remove items from the cart.
    # This method takes an item name as a parameter.
    def remove_item(self, item_name):
        found = False
        for item in self.cart_items:
            if item.item_name == item_name:
                self.cart_items.remove(item)
                found = True
                break
        if not found:
            print('Item not found in cart. Nothing removed.')

    # Method to modify item quantity in the cart.
    # This method takes an item name and a quantity as parameters.
    def modify_item(self, item_modify):
        found = False
        for item in self.cart_items:
            if item.item_name == item_modify.item_name:
                found = True
                if item_modify.item_quantity != 0:
                    item.item_quantity = item_modify.item_quantity
                if item_modify.item_price != 0:
                    item.item_price = item_modify.item_price
                break
        if not found:
            print('Item not found in cart. Nothing modified.')

    # Method to return the total number of items in the cart.
    # This method iterates over the cart items and sums the quantity of each item.
    def get_qty_items_in_cart(self):
        qty_items = sum(item.item_quantity for item in self.cart_items)
        return qty_items

    # Method to return total cost of the cart.
    # This method iterates over the cart items and sums the total cost of each item.
    def get_total_cost_of_cart(self):
        total_cost = sum(item.item_price * item.item_quantity for item in self.cart_items)
        return total_cost

    # Method to print the total cost of the cart.
    # This method also calls the print_item_cost method to print the individual costs of each item.
    def print_total_cost(self):
        print(f'{self.cust_name}\'s Shopping Cart: {self.cur_date}')
        qty_items = self.get_qty_items_in_cart()
        print(f'Number of Items in Your Cart: {qty_items}\n')
        if qty_items == 0:
            print('Shopping Cart is Empty')
        else:
            for item in self.cart_items:
                item.print_item_cost()
            print(f'\nTotal: ${self.get_total_cost_of_cart():.2f}')

    # Method to print the descriptions of each item in the cart.
    # This method iterates over the cart items and calls the print_item_description method for each item.
    def print_description(self):
        print(f'{self.cust_name}\'s Shopping Cart - {self.cur_date}')
        print('\nItem Descriptions:')
        for item in self.cart_items:
            print(f'{item.item_name}: {item.item_description}')

# PART 3:
# Function to print the menu options for the user.
# This function takes a ShoppingCart object as a parameter.
def display_menu(cart):
    option = " "
    while option != "q":
        print('\nMENU')
        print('a - Add item to cart')
        print('r - Remove item from cart')
        print('c - Change item quantity')
        print('i - Output items\' descriptions')
        print('o - Output shopping cart')
        print('q - Quit')
        option = input('Choose an option:\n')

        # Option a: Add item to cart
        if option == "a":
            item_name = input('Enter the item name:\n')
            item_price = float(input('Enter the item price:\n'))
            item_quantity = int(input('Enter the item quantity:\n'))
            item_description = input('Enter the item description:\n')  # Get item description
            new_item = ItemToPurchase(item_name, item_price, item_quantity, item_description)
            cart.add_item(new_item)

        # Option r: Remove item from cart
        elif option == "r":
            item_name = input('Enter the name of the item to remove:\n')
            cart.remove_item(item_name)

        # Option c: Change item quantity
        elif option == "c":
            item_name = input('Enter the name of the item to modify:\n')
            item_price = float(input('Enter the new price:\n'))
            item_quantity = int(input('Enter the new quantity:\n'))
            new_item = ItemToPurchase(item_name, item_price, item_quantity)
            cart.modify_item(new_item)

        # Option i: Output items' descriptions
        elif option == "i":
            cart.print_description()

        # Option o: Output shopping cart
        elif option == "o":
            cart.print_total_cost()

        # Option q: Quit the program
        elif option == "q":
            break
        else:
            print('Invalid option')

# Part 7 In the main function, create a ShoppingCart object and call the display_menu function.
# This code will only run if the script is executed directly.
if __name__ == "__main__":
    # Prompt User for Name and Date
    cust_name = input('Enter your name:\n')
    cur_date = input('Enter the current date:\n')

    # Output name and date
    # Create a ShoppingCart object and call the display_menu function
    print(f'Customer Name: {cust_name}')
    print(f'Today\'s Date: {cur_date}')

    cart = ShoppingCart(cust_name, cur_date)
    display_menu(cart)
