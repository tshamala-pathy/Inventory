# Shoe Inventory Management Readme 🥿📦

## Introduction 📝

This Shoe Inventory Management program is designed to help users manage information about shoes, including their country of origin, product code, product name, cost, and quantity. The program provides various functionalities such as reading shoe data from a file, capturing new shoe information, viewing all shoes, re-stocking shoes, searching for a shoe by its code, calculating the value per item for each shoe, and finding the shoe with the highest quantity for sale.

## Files 📂

- **main.py**: The main Python script containing the Shoe class and the main program logic.
- **inventory.txt**: A sample file containing shoe data in CSV (Comma-Separated Values) format. Each line represents a shoe with fields in the order: country, code, product, cost, quantity.

## How to Use 🚀

1. **Run the Program:**
    - Execute the `main.py` script to start the Shoe Inventory Management program.

2. **Main Menu:**
    - The program will display a main menu with various options.
    - Choose an option by entering the corresponding number.

3. **Options:**
    1. **Read Shoes Data from File (Option 1):**
        - Reads shoe data from the 'inventory.txt' file and populates the shoe_list.

    2. **Capture Shoe (Option 2):**
        - Allows the user to manually input information for a new shoe and adds it to the inventory.

    3. **View All Shoes (Option 3):**
        - Displays information about all shoes in the inventory.

    4. **Re-stock Shoes (Option 4):**
        - Increases the quantity of the shoe with the lowest quantity by a user-specified amount.

    5. **Search Shoe (Option 5):**
        - Allows the user to search for a shoe by its code.

    6. **Calculate Value per Item (Option 6):**
        - Calculates and displays the value per item for each shoe based on its cost and quantity.

    7. **Find Highest Quantity Shoe (Option 7):**
        - Finds and displays information about the shoe with the highest quantity for sale.

    8. **Exit (Option 8):**
        - Exits the program.

## Error Handling 🛑

- The program includes error handling for file not found and general exceptions during file reading.
- It checks for valid input when capturing shoe information and re-stocking.

## Sample 'inventory.txt' File Format 📄

Country,Code,Product,Cost,Quantity
USA,001,Athletic Shoe,50.00,100
China,002,Leather Boot,80.00,50
Italy,003,Canvas Sneaker,30.00,75


Note: Make sure to maintain the CSV format with the specified order of fields.

## Notes 📌

- The program uses a class-based approach, where each shoe is represented by an instance of the Shoe class.
- The shoe_list is a list that holds instances of the Shoe class, forming the inventory.
- Feel free to customize the program to suit specific needs or extend its functionalities.

## Author ✍️

Tshamala Pathy

Feel free to reach out for any questions or improvements! 🌟
