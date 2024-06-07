import pyautogui
import random
import time

def auto_clicker():
    try:
        while True:
            # Perform a click
            pyautogui.click()
            
            # Random interval between clicks
            interval = random.uniform(0.5, 1.5)  # Random interval between 0.5 and 1.5 seconds
            time.sleep(interval)
            
            # Jiggle the mouse briefly
            for _ in range(random.randint(1, 3)):  # Jiggle the mouse 1 to 3 times
                pyautogui.move(5, 5, duration=0.1)
                pyautogui.move(-5, -5, duration=0.1)
                pyautogui.move(-5, 5, duration=0.1)
                pyautogui.move(5, -5, duration=0.1)
            
            # Random interval between jiggles
            time.sleep(random.uniform(0.2, 0.5))
            
    except KeyboardInterrupt:
        print("\nAuto clicker stopped.")

if __name__ == "__main__":
    auto_clicker()
