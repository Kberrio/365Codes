class ChecklistApp:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append({"task": item, "completed": False})
        print(f"Added: {item}")

    def mark_complete(self, index):
        if 0 <= index < len(self.items):
            self.items[index]["completed"] = True
            print(f"Marked as complete: {self.items[index]['task']}")
        else:
            print("Invalid item index")

    def display_list(self):
        if not self.items:
            print("Your checklist is empty")
        else:
            for i, item in enumerate(self.items):
                status = "✓" if item["completed"] else " "
                print(f"{i}. [{status}] {item['task']}")

def main():
    app = ChecklistApp()
    
    while True:
        print("\nChecklist App")
        print("1. Add item")
        print("2. Mark item as complete")
        print("3. Display checklist")
        print("4. Quit")
        
        choice = input("Enter your choice (1-4): ")
        
        if choice == "1":
            item = input("Enter the task: ")
            app.add_item(item)
        elif choice == "2":
            index = int(input("Enter the item number to mark as complete: "))
            app.mark_complete(index)
        elif choice == "3":
            app.display_list()
        elif choice == "4":
            print("Thank you for using the Checklist App. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()