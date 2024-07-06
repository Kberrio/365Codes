import pyautogui
import time
import random
import datetime

# Disable pyautogui's fail-safe feature
pyautogui.FAILSAFE = False

def get_click_position():
    print("Move your mouse to the center of the desired click area and press Enter.")
    input()
    return pyautogui.position()

def random_move():
    screen_width, screen_height = pyautogui.size()
    random_x = random.randint(0, screen_width)
    random_y = random.randint(0, screen_height)
    pyautogui.moveTo(random_x, random_y, duration=0.5)

def log_action(message):
    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"[{current_time}] {message}")

def get_random_point_in_area(center, radius):
    x = center[0] + random.uniform(-radius, radius)
    y = center[1] + random.uniform(-radius, radius)
    return (int(x), int(y))

def main():
    click_center = get_click_position()
    log_action(f"Click area center set to: {click_center}")

    start_time = time.time()
    click_count = 0
    
    try:
        while time.time() - start_time < 5 * 3600:  # Run for less than 5 hours
            click_count += 1
            
            # Get a random point within a small area around the center
            click_pos = get_random_point_in_area(click_center, 10)  # 10 pixel radius
            
            # Move to the click position slowly and perform a click
            pyautogui.moveTo(click_pos[0], click_pos[1], duration=1.0)
            pyautogui.click(duration=0.5)
            log_action(f"Click #{click_count} at {click_pos}")

            # Random interval between 15 and 19 minutes (900 to 1140 seconds)
            interval = random.randint(900, 1140)
            log_action(f"Waiting for {interval} seconds ({interval/60:.2f} minutes)")

            # Move the mouse to a random position
            random_move()

            # Wait for the interval
            time.sleep(interval)

            # Log the total running time
            elapsed_time = time.time() - start_time
            log_action(f"Total running time: {elapsed_time:.2f} seconds ({elapsed_time/3600:.2f} hours)")

        log_action("5 hours completed. Stopping execution.")

    except KeyboardInterrupt:
        log_action("Program terminated by user.")

    finally:
        total_time = time.time() - start_time
        log_action(f"Program ran for a total of {total_time:.2f} seconds ({total_time/3600:.2f} hours)")
        log_action(f"Performed {click_count} clicks")

if __name__ == "__main__":
    main()