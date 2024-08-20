class Cafe:
    def __init__(self):
        self.name = ""
        self.date = ""
        self.mobile = ""
        self.menu = {
            "Coffee": 2.5,
            "Tea": 1.5,
            "Sandwich": 5.0,
            "Cake": 3.0
        }
        self.order = {}

    def person_detail(self):
        self.name = input("Name: ")
        self.date = input("Date (dd-mm-yyyy): ")
        self.mobile = input("Mobile: ")

    def take_order(self):
        print("\nMenu:")
        for item, price in self.menu.items():
            print(f"{item}: ${price}")

        while True:
            item = input("\nEnter the item you want to order (or type 'done' to finish): ").title()
            if item == "Done":
                break
            elif item in self.menu:
                try:
                    quantity = int(input(f"How many {item}(s) would you like to order? "))
                    if item in self.order:
                        self.order[item] += quantity
                    else:
                        self.order[item] = quantity
                except ValueError:
                    print("Please enter a valid number.")
            else:
                print("Sorry, that item is not on the menu.")

    def calculate_total(self):
        total = 0
        for item, quantity in self.order.items():
            total += self.menu[item] * quantity
        return total

    def save_receipt(self):
        total = self.calculate_total()
        with open(f"{self.name}_receipt.txt", "w") as file:
            file.write(f"Name: {self.name}\n")
            file.write(f"Date: {self.date}\n")
            file.write(f"Mobile: {self.mobile}\n\n")
            file.write("Order:\n")
            for item, quantity in self.order.items():
                file.write(f"{item} x{quantity}: ${self.menu[item] * quantity}\n")
            file.write(f"\nTotal: ${total:.2f}\n")

    def main(self):
        self.person_detail()
        self.take_order()
        self.save_receipt()
        print(f"\nOrder placed successfully! Your total is ${self.calculate_total():.2f}.")
        print(f"Receipt saved as {self.name}_receipt.txt")

if __name__ == "__main__":
    cafe = Cafe()
    cafe.main()
                
        
                
                

                