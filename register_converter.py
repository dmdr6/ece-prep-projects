# ==============================================
# THE HEXADECIMAL-TO-DECIMAL REGISTER CONVERTER
# ==============================================

# User Menu

print("""Please, select one of the following options:
      Option 1: Convert Standard Decimal Number ---> Hexadecimal
      Option 2: Convert Hexadecimal ---> Standard Decimal Number
""")

user_option = input("Enter an option (1 or 2): ")

print(" ") # Spacing line

if user_option == "1":
    decimal_number = int(input("Enter an integer: "))
    print(f"Hardware Register Address: {hex(decimal_number)}")

elif user_option == "2":
    hexadecimal_number = input("Enter a hexadecimal number (e.g., 0x1A): ")
    print(f"Standard Decimal Number: {int(hexadecimal_number, 16)}")

else:
    print("Invalid choice. Please restart the script and type 1 or 2.")