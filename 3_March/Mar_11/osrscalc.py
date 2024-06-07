import time

def get_experience():
    # Function to get current experience from the user
    return int(input("Enter your current experience: "))

def calculate_xp_per_hour(start_xp, end_xp, time_elapsed):
    # Calculate XP gained
    xp_gained = end_xp - start_xp
    # Calculate XP per hour
    xp_per_hour = (xp_gained / time_elapsed) * 3600  # Convert time to hours
    return xp_per_hour

def main():
    print("OSRS Experience Per Hour Calculator")
    print("===================================")
    
    start_time = time.time()
    start_xp = get_experience()
    
    while True:
        # Wait for some time (e.g., 1 hour)
        time.sleep(3600)  # 1 hour in seconds
        end_xp = get_experience()
        end_time = time.time()
        
        time_elapsed = end_time - start_time
        xp_per_hour = calculate_xp_per_hour(start_xp, end_xp, time_elapsed)
        
        print(f"You gained {end_xp - start_xp} experience in {time_elapsed / 3600:.2f} hours.")
        print(f"Your XP/hr: {xp_per_hour:.2f}")
        
        # Update start time and XP for the next iteration
        start_time = end_time
        start_xp = end_xp
        
        # Option to continue or exit
        choice = input("Do you want to continue? (yes/no): ").lower()
        if choice != 'yes':
            break

if __name__ == "__main__":
    main()
