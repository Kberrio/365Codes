class CRUD:
    def __init__(self):
        self.data = {}

    def create(self, key, value):
        self.data[key] = value
        print(f"Created entry: {key}: {value}")

    def read(self, key):
        if key in self.data:
            print(f"Value for {key}: {self.data[key]}")
        else:
            print(f"No entry found for {key}")

    def update(self, key, value):
        if key in self.data:
            self.data[key] = value
            print(f"Updated entry: {key}: {value}")
        else:
            print(f"No entry found for {key}")

    def delete(self, key):
        if key in self.data:
            del self.data[key]
            print(f"Deleted entry for {key}")
        else:
            print(f"No entry found for {key}")


def main():
    crud = CRUD()
    
    while True:
        print("\n1. Create\n2. Read\n3. Update\n4. Delete\n5. Exit")
        choice = input("Enter your choice: ")
        
        if choice == '1':
            key = input("Enter key: ")
            value = input("Enter value: ")
            crud.create(key, value)
        elif choice == '2':
            key = input("Enter key to read: ")
            crud.read(key)
        elif choice == '3':
            key = input("Enter key to update: ")
            value = input("Enter new value: ")
            crud.update(key, value)
        elif choice == '4':
            key = input("Enter key to delete: ")
            crud.delete(key)
        elif choice == '5':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")


if __name__ == "__main__":
    main()
