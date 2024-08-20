 Cafe Management System in Python

Welcome to the **Cafe Management System**! This is a beginner-friendly project built in Python to manage basic operations in a cafe, such as taking orders, calculating the bill, and displaying the menu.

## Features

- **View Menu:** Displays the available items in the cafe along with their prices.
- **Take Order:** Allows customers to place their orders.
- **Calculate Bill:** Calculates the total price of the order and applies any discounts if available.
- **Exit System:** Option to exit the system when the user is finished.

## Requirements

You just need Python installed on your system to run this project. You can download it from [Python's official website](https://www.python.org/downloads/).

## How to Run the Project

1. Download or clone the repository to your local machine.
2. Open the terminal or command prompt in the project folder.
3. Run the program using the following command:

## Python Concepts Used

This project uses basic Python programming concepts, making it great for beginners! Here’s what is covered:

- **Variables:** Used to store the menu items, prices, and orders.
- **Functions:** Structured the code using functions to make it easy to manage different operations (e.g., viewing the menu, taking orders, calculating the bill).
- **Loops:** Used `while` loops to keep the system running until the user chooses to exit.
- **Conditionals:** `if` and `else` statements help make decisions in the code, like checking if an item exists on the menu or if the customer has finished ordering.
- **Lists:** Store multiple items such as orders and menu options.
- **Dictionaries:** Map menu items to their prices for easier lookup.



Here’s a small example of how the menu might be displayed in this system:

```python
menu = {
    "Coffee": 3.0,
    "Tea": 2.5,
    "Sandwich": 5.0,
    "Cake": 4.0
}

def display_menu():
    print("Menu:")
    for item, price in menu.items():
        print(f"{item}: ${price}")

