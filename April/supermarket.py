def create_shopping_list():
    shopping_list = {}

    while True:
        item = input("Enter item to add to the shopping list (type 'done' to finish): ").lower()
        if item == 'done':
            break

        quantity = input(f"Enter the quantity of {item}: ")
        shopping_list[item] = quantity

    return shopping_list

def print_shopping_list(shopping_list):
    print("\nYour shopping list:")
    for item, quantity in shopping_list.items():
        print(f"{item.capitalize()}: {quantity}")

if __name__ == "__main__":
    shopping_list = create_shopping_list()
    print_shopping_list(shopping_list)