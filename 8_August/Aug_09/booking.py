import datetime

class BookingSystem:
    def __init__(self):
        self.appointments = {}

    def book_appointment(self, date, time, name):
        appointment_datetime = datetime.datetime.strptime(f"{date} {time}", "%Y-%m-%d %H:%M")
        if appointment_datetime in self.appointments:
            return False
        self.appointments[appointment_datetime] = name
        return True

    def view_appointments(self):
        sorted_appointments = sorted(self.appointments.items())
        for datetime, name in sorted_appointments:
            print(f"{datetime.strftime('%Y-%m-%d %H:%M')}: {name}")

    def cancel_appointment(self, date, time):
        appointment_datetime = datetime.datetime.strptime(f"{date} {time}", "%Y-%m-%d %H:%M")
        if appointment_datetime in self.appointments:
            del self.appointments[appointment_datetime]
            return True
        return False

def main():
    booking_system = BookingSystem()

    while True:
        print("\n1. Book an appointment")
        print("2. View appointments")
        print("3. Cancel an appointment")
        print("4. Exit")
        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            date = input("Enter date (YYYY-MM-DD): ")
            time = input("Enter time (HH:MM): ")
            name = input("Enter your name: ")
            if booking_system.book_appointment(date, time, name):
                print("Appointment booked successfully!")
            else:
                print("Sorry, that time slot is already booked.")

        elif choice == '2':
            booking_system.view_appointments()

        elif choice == '3':
            date = input("Enter date (YYYY-MM-DD): ")
            time = input("Enter time (HH:MM): ")
            if booking_system.cancel_appointment(date, time):
                print("Appointment cancelled successfully!")
            else:
                print("No appointment found at that date and time.")

        elif choice == '4':
            print("Thank you for using the booking system. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()