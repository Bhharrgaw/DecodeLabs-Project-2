print("Expense Tracker")

total = 0

while True:
    amount = input("Enter expense (or type 'quit' to finish): ")

    if amount.lower() == "quit":
        break

    try:
        amount = int(amount)
        total = total + amount
        print("Total so far =", total)
    except:
        print("Please enter a valid number.")

print("\nTotal Expense =", total)
print("Thank you!")