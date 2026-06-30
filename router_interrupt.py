# ====================================
# THE NETWORK ROUTER PACKET PROCESSOR
# ====================================

def trigger_reboot_sequence():
    print("THE ROUTER IS CLEARING ITS CACHE AND RESTARTING")

def trigger_thermal_shutdown():
    print("WARNING! TEMPERATURES CROSSED 90°C")
    print("THE FANS ARE SPINNING AT 100%")

while True:
    print("System Status: Processing network packets safely... [0% Packet Drop]")
   
    interrupt_signal = input("Enter the value of the signal: ")
   
    if interrupt_signal == "1":
        trigger_reboot_sequence()
   
    elif interrupt_signal == "2":
        trigger_thermal_shutdown()
  
    elif interrupt_signal == "":
        print("No interrupts. Forwarding next packet load...")
  
    else:
        print("Invalid Input. Please restart the loop")
