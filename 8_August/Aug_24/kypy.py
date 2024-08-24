from pynput.keyboard import Key, Controller, Listener, HotKey
import time

# Initialize the keyboard controller
keyboard = Controller()

# Function to type a predefined text
def type_text():
    text = "This is an automated typing script."
    for char in text:
        keyboard.press(char)
        keyboard.release(char)
        time.sleep(0.1)  # Adding delay to mimic human typing speed

# Function to simulate complex key combinations
def complex_key_combinations():
    # Press and release a series of keys
    with keyboard.pressed(Key.ctrl):
        with keyboard.pressed(Key.shift):
            keyboard.press('n')
            keyboard.release('n')
    
    time.sleep(0.5)
    
    # Simulate pressing "Ctrl + Alt + Delete"
    with keyboard.pressed(Key.ctrl):
        with keyboard.pressed(Key.alt):
            keyboard.press(Key.delete)
            keyboard.release(Key.delete)

# Callback function for hotkey events
def on_activate_h():
    print('<Ctrl>+<Alt>+H pressed! Triggering typing action.')
    type_text()

def on_activate_q():
    print('<Ctrl>+<Alt>+Q pressed! Exiting...')
    return False  # This will stop the listener

# Define hotkeys
hotkey_combinations = {
    frozenset([Key.ctrl, Key.alt, KeyCode(char='h')]): on_activate_h,
    frozenset([Key.ctrl, Key.alt, KeyCode(char='q')]): on_activate_q,
}

# Listener for hotkeys
def for_canonical(f):
    return lambda k: f(l.canonical(k))

def on_press(key):
    print(f'Key {key} pressed.')
    # Implement more complex behavior here if needed

def on_release(key):
    print(f'Key {key} released.')
    if key == Key.esc:
        # Stop listener
        return False

# Start listening for keyboard events
with Listener(on_press=on_press, on_release=on_release) as listener:
    with keyboard.pressed(Key.shift):
        keyboard.press('a')
        keyboard.release('a')

    # Adding some complex key press and release scenarios
    complex_key_combinations()
    
    # Hotkey Listener
    with Listener(on_press=for_canonical(hotkey_combinations.get)):
        listener.join()

print("Script completed.")
