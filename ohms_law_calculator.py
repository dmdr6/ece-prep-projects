# =============================
# --- OHM'S LAW CALCULATOR ---
# =============================

# Functions (math only)
# Ohm's Law
def calculate_voltage(resistance, current):
    return resistance * current

def calculate_current(resistance, voltage):
    return voltage / resistance

def calculate_resistance(current, voltage):
    return voltage / current

# Print the menu for the user to see the options
print("Ohm's Law")
print("""
Select what you want to calculate:
      Type 'V' -> Voltage
      Type 'I' -> Current
      Type 'R' -> Resistance
""")

# Ask for user's input
ohms_option_selected = int("Enter V, I, or R: ").lower()

# Create conditions
if ohms_option_selected == "v":
    resistance = float(input("Enter Resistance (Ω): "))
    current = float(input("Enter Current (A): "))

    voltage = calculate_voltage(resistance, current)

    print(f"Voltage: {voltage:.3f} V")

elif ohms_option_selected == "i":
    resistance = float(input("Enter Resistance (Ω): "))
    voltage = float(input("Enter Voltage (V): "))

    current = calculate_current(resistance, voltage)

    print(f"Current: {current:.6e} A")

elif ohms_option_selected == "r":
    current = float(input("Enter Current (A): "))
    voltage = float(input("Enter Voltage (V): "))

    resistance = calculate_resistance(current, voltage)

    print(f"Resistance: {resistance:.3f} Ω")

else:
    print("Invalid option. Try again.")

