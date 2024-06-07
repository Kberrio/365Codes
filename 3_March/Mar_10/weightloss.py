def calculate_weight(activity_factor):
    base_weight = 70  # Base weight in kilograms
    weight_change = 0.2  # Weight change factor in kilograms per activity level

    # Calculate weight change based on activity factor
    weight_change_amount = weight_change * activity_factor

    # Calculate new weight
    new_weight = base_weight + weight_change_amount
    return new_weight

def main():
    print("Welcome to the Weight Calculator!")
    activity_input = input("Please rate your activity level today from 1 to 10 (1 being sedentary, 10 being highly active): ")
    try:
        activity_factor = float(activity_input)
        if 1 <= activity_factor <= 10:
            new_weight = calculate_weight(activity_factor)
            print("Your estimated weight today is:", new_weight, "kg")
        else:
            print("Invalid input. Activity level must be between 1 and 10.")
    except ValueError:
        print("Invalid input. Please enter a number.")

if __name__ == "__main__":
    main()