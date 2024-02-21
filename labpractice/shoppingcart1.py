amount_owed = float(input("Enter the amount owed: $"))
entered_amount = float(input("Enter the customer's entered amount: $"))

# Check if entered amount is greater than or equal to the amount owed
if entered_amount >= amount_owed:
    # Calculate the change owed
    change_due = entered_amount - amount_owed
    print(f"Change owed: ${change_due:.2f}")

    # Compute the number of $5 bills
    num_5_bills = int(change_due // 5)
    change_due -= num_5_bills * 5

    # Compute the number of $1 bills
    num_1_bills = int(change_due // 1)
    change_due -= num_1_bills * 1

    # Compute the number of quarters
    num_quarters = int(change_due // 0.25)
    change_due -= num_quarters * 0.25

    # Compute the number of dimes
    num_dimes = int(change_due // 0.1)
    change_due -= num_dimes * 0.1

    # Compute the number of nickels
    num_nickels = int(change_due // 0.05)
    change_due -= num_nickels * 0.05

    # Compute the number of pennies
    num_pennies = int(change_due * 100)

    # Display the amount of change to be disbursed
    print(f"Change to be disbursed: ${entered_amount - amount_owed:.2f}")
    print(f"$5 bills: {num_5_bills}")
    print(f"$1 bills: {num_1_bills}")
    print(f"Quarters: {num_quarters}")
    print(f"Dimes: {num_dimes}")
    print(f"Nickels: {num_nickels}")
    print(f"Pennies: {num_pennies}")
else:
    print("Insufficient funds. Please enter more money.")