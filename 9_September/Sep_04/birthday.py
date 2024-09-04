import datetime
import json
import os
from abc import ABC, abstractmethod

class Person:
    def __init__(self, name, birthday, email):
        self.name = name
        self.birthday = datetime.datetime.strptime(birthday, "%Y-%m-%d").date()
        self.email = email

    def __str__(self):
        return f"{self.name} (Born: {self.birthday}, Email: {self.email})"

class BirthdayDatabase:
    def __init__(self, filename="birthdays.json"):
        self.filename = filename
        self.people = []
        self.load_data()

    def add_person(self, person):
        self.people.append(person)
        self.save_data()

    def remove_person(self, name):
        self.people = [p for p in self.people if p.name != name]
        self.save_data()

    def get_upcoming_birthdays(self, days=7):
        today = datetime.date.today()
        upcoming = []
        for person in self.people:
            next_birthday = person.birthday.replace(year=today.year)
            if next_birthday < today:
                next_birthday = next_birthday.replace(year=today.year + 1)
            days_until = (next_birthday - today).days
            if days_until <= days:
                upcoming.append((person, days_until))
        return sorted(upcoming, key=lambda x: x[1])

    def load_data(self):
        if os.path.exists(self.filename):
            with open(self.filename, "r") as f:
                data = json.load(f)
                self.people = [Person(**p) for p in data]

    def save_data(self):
        data = [{"name": p.name, "birthday": p.birthday.strftime("%Y-%m-%d"), "email": p.email} for p in self.people]
        with open(self.filename, "w") as f:
            json.dump(data, f, indent=2)

class NotificationStrategy(ABC):
    @abstractmethod
    def send_notification(self, person, days_until):
        pass

class EmailNotification(NotificationStrategy):
    def send_notification(self, person, days_until):
        print(f"Sending email to {person.email}:")
        if days_until == 0:
            print(f"Happy Birthday, {person.name}!")
        else:
            print(f"Birthday reminder: {person.name}'s birthday is in {days_until} days.")

class SMSNotification(NotificationStrategy):
    def send_notification(self, person, days_until):
        print(f"Sending SMS to {person.name}:")
        if days_until == 0:
            print(f"Happy Birthday, {person.name}!")
        else:
            print(f"Birthday reminder: Your birthday is in {days_until} days.")

class BirthdayNotifier:
    def __init__(self, database, strategy):
        self.database = database
        self.strategy = strategy

    def send_notifications(self, days=7):
        upcoming = self.database.get_upcoming_birthdays(days)
        for person, days_until in upcoming:
            self.strategy.send_notification(person, days_until)

class BirthdayManager:
    def __init__(self):
        self.database = BirthdayDatabase()
        self.notifier = BirthdayNotifier(self.database, EmailNotification())

    def run(self):
        while True:
            print("\nBirthday Manager")
            print("1. Add a person")
            print("2. Remove a person")
            print("3. View all birthdays")
            print("4. View upcoming birthdays")
            print("5. Send notifications")
            print("6. Exit")
            
            choice = input("Enter your choice: ")
            
            if choice == "1":
                name = input("Enter name: ")
                birthday = input("Enter birthday (YYYY-MM-DD): ")
                email = input("Enter email: ")
                self.database.add_person(Person(name, birthday, email))
            elif choice == "2":
                name = input("Enter name to remove: ")
                self.database.remove_person(name)
            elif choice == "3":
                for person in self.database.people:
                    print(person)
            elif choice == "4":
                days = int(input("Enter number of days to look ahead: "))
                upcoming = self.database.get_upcoming_birthdays(days)
                for person, days_until in upcoming:
                    print(f"{person.name}: {days_until} days until birthday")
            elif choice == "5":
                self.notifier.send_notifications()
            elif choice == "6":
                break
            else:
                print("Invalid choice. Please try again.")

if __name__ == "__main__":
    manager = BirthdayManager()
    manager.run()