# ===========================
# "--- Virtual LED Blink Simulator ---"
# ===========================

import time

# Start with the virtual LED turned off
led_is_on = False

while True:
    if led_is_on:
        print("LED IS ON (🟢)")
    else:
        print("LED IS OFF (⚫)")
        
        # Toggle the boolean state
        led_is_on = not led_is_on
        
        # Wait for 1 second before repeating the loop
        time.sleep(1)
