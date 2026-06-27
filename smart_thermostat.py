# ======================================
# THE SMART THERMOSTAT THRESHOLD MONITOR
# ======================================

# Establish the user's input
temperature = int(input("Enter the current temperature: "))

# Establish the lower and upper limit variables
lower_limit = 60
upper_limit = 80

print(" ") # Print a space

if temperature >= lower_limit and temperature <= upper_limit:
    print("THE SYSTEM IS STABLE")
elif temperature < lower_limit:
    print("THE SYSTEM IS BELOW THE ESTABLISHED LOWER LIMIT")
    print("ALERT: ACTIVATING HEATER!")
elif temperature > upper_limit:
    print("THE SYSTEM IS ABOVE THE ESTABLISHED UPPER LIMIT")
    print("ALERT: ACTIVATING COOLING FAN!")

