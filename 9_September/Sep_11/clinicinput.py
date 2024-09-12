class Patient:
    def __init__(self, name, age, gender, symptoms):
        self.name = name
        self.age = age
        self.gender = gender
        self.symptoms = symptoms

def get_patient_info():
    name = input("Enter patient name: ")
    age = int(input("Enter patient age: "))
    gender = input("Enter patient gender: ")
    symptoms = input("Enter patient symptoms: ")
    return Patient(name, age, gender, symptoms)

def main():
    patients = []
    while True:
        print("\n1. Add new patient")
        print("2. View all patients")
        print("3. Exit")
        choice = input("Enter your choice (1-3): ")

        if choice == '1':
            patient = get_patient_info()
            patients.append(patient)
            print("Patient added successfully!")
        elif choice == '2':
            if not patients:
                print("No patients in the system.")
            else:
                for i, patient in enumerate(patients, 1):
                    print(f"\nPatient {i}:")
                    print(f"Name: {patient.name}")
                    print(f"Age: {patient.age}")
                    print(f"Gender: {patient.gender}")
                    print(f"Symptoms: {patient.symptoms}")
        elif choice == '3':
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()