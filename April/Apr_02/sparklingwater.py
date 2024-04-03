class SparklingWaterDispenser:
    def __init__(self, initial_water_level=100):
        self.water_level = initial_water_level

    def dispense(self, amount):
        if self.water_level >= amount:
            self.water_level -= amount
            print(f"Dispensing {amount}ml of sparkling water.")
        else:
            print("Not enough water. Please refill the dispenser.")

    def refill(self, amount):
        self.water_level += amount
        print(f"Refilled dispenser with {amount}ml of sparkling water. Current water level: {self.water_level}ml")


def main():
    dispenser = SparklingWaterDispenser()

    while True:
        print("\n1. Dispense sparkling water")
        print("2. Refill dispenser")
        print("3. Check water level")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            amount = int(input("Enter the amount of sparkling water to dispense (in ml): "))
            dispenser.dispense(amount)
        elif choice == '2':
            amount = int(input("Enter the amount of sparkling water to refill (in ml): "))
            dispenser.refill(amount)
        elif choice == '3':
            print(f"Current water level: {dispenser.water_level}ml")
        elif choice == '4':
            print("Exiting program. Thank you!")
            break
        else:
            print("Invalid choice. Please enter a valid option.")


if __name__ == "__main__":
    main()
