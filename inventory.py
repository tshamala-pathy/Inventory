# Define a class to represent shoe objects
class Shoe:
    def __init__(self, country, code, product, cost, quantity):
        # Initialize shoe attributes
        self.country = country
        self.code = code
        self.product = product
        self.cost = cost
        self.quantity = quantity

    def get_cost(self):
        return self.cost

    def get_quantity(self):
        return self.quantity

    def __str__(self):
        return f"Country: {self.country}, Code: {self.code}, Product: {self.product}, Cost: {self.cost}, Quantity: {self.quantity}"

# Create an empty list to store shoe objects
shoe_list = []

# Function to read shoe data from a file
def read_shoes_data():
    try:
        with open('inventory.txt', 'r') as file:
            next(file)  # Skip the first line
            for line in file:
                data = line.strip().split(',')
                if len(data) == 5:
                    country, code, product, cost, quantity = data
                    shoe = Shoe(country, code, product, float(cost), int(quantity))
                    shoe_list.append(shoe)
    except FileNotFoundError:
        print("File 'inventory.txt' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Function to capture shoe information from the user
def capture_shoes():
    country = input("Enter the country: ")
    code = input("Enter the code: ")
    product = input("Enter the product: ")
    cost = float(input("Enter the cost: "))
    quantity = int(input("Enter the quantity: "))
    shoe = Shoe(country, code, product, cost, quantity)
    shoe_list.append(shoe)
    print("Shoe added successfully!")

# Function to view all shoes in the inventory
def view_all():
    if not shoe_list:
        print("No shoes in the list.")
    else:
        print("List of Shoes:")
        for shoe in shoe_list:
            print(shoe)

# Function to re-stock shoes with additional quantity
def re_stock():
    if not shoe_list:
        print("No shoes in the list.")
        return

    lowest_quantity_shoe = min(shoe_list, key=lambda x: x.get_quantity())
    print(f"Lowest quantity shoe: {lowest_quantity_shoe}")
    try:
        additional_quantity = int(input("Enter the quantity to add: "))
        if additional_quantity > 0:
            lowest_quantity_shoe.quantity += additional_quantity
            print(f"Quantity updated successfully! New quantity: {lowest_quantity_shoe.get_quantity()}")
        else:
            print("Quantity should be a positive number.")
    except ValueError:
        print("Invalid input for quantity.")

# Function to search for a shoe by its code
def search_shoe():
    code_to_search = input("Enter the code of the shoe to search: ")
    for shoe in shoe_list:
        if shoe.code == code_to_search:
            print(f"Shoe found: {shoe}")
            return
    print(f"No shoe found with code '{code_to_search}'.")

# Function to calculate and display the value per item for each shoe
def value_per_item():
    for shoe in shoe_list:
        value = shoe.cost * shoe.quantity
        print(f"Product: {shoe.product}, Value per item: {value}")

# Function to find the shoe with the highest quantity for sale
def highest_qty():
    if not shoe_list:
        print("No shoes in the list.")
        return

    highest_quantity_shoe = max(shoe_list, key=lambda x: x.get_quantity())
    print(f"Highest quantity shoe for sale: {highest_quantity_shoe}")

# Main Menu
while True:
    print("\n===== Shoe Inventory Management =====")
    print("1. Read Shoes Data from File")
    print("2. Capture Shoe")
    print("3. View All Shoes")
    print("4. Re-stock Shoes")
    print("5. Search Shoe")
    print("6. Calculate Value per Item")
    print("7. Find Highest Quantity Shoe")
    print("8. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        read_shoes_data()
    elif choice == "2":
        capture_shoes()
    elif choice == "3":
        view_all()
    elif choice == "4":
        re_stock()
    elif choice == "5":
        search_shoe()
    elif choice == "6":
        value_per_item()
    elif choice == "7":
        highest_qty()
    elif choice == "8":
        print("Exiting the program. Goodbye!")
        break
    else:
        print("Invalid choice. Please enter a valid option.")
        
