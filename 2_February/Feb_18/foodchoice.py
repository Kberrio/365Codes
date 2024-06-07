def suggest_food():
    print("Welcome to the Food Suggestion Program!")
    print("Let's find the perfect meal for you.")

    # Ask questions to determine food suggestion
    preference = input("Do you prefer a light meal or a hearty meal? (light/hearty): ").lower()
    cuisine = input("What cuisine do you fancy? (e.g., Italian, Mexican, Indian): ").lower()
    time = input("Are you looking for something quick or are you willing to spend time cooking? (quick/cooking): ").lower()

    # Based on answers, suggest a food item
    if preference == 'light':
        if cuisine == 'italian':
            suggestion = "Caprese salad with a side of bruschetta"
        elif cuisine == 'mexican':
            suggestion = "Vegetable fajita wraps"
        elif cuisine == 'indian':
            suggestion = "Vegetable curry with basmati rice"
        else:
            suggestion = "A mixed green salad with vinaigrette dressing"
    elif preference == 'hearty':
        if cuisine == 'italian':
            suggestion = "Spaghetti carbonara"
        elif cuisine == 'mexican':
            suggestion = "Chicken enchiladas with rice and beans"
        elif cuisine == 'indian':
            suggestion = "Chicken tikka masala with naan bread"
        else:
            suggestion = "Grilled steak with roasted vegetables"
    else:
        suggestion = "Sorry, we couldn't suggest a meal based on your preferences."

    # Display the suggestion
    print("\nWe suggest you try:", suggestion)

# Call the function to run the program
suggest_food()
