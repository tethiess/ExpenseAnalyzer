# Level 04 Assignment: Personal Expense Analyzer
# IS 303 - Hilton
# Author: Daniel Thiess
#
# Repeatedly asks the user for expenses until they enter 0, then classifies
# each expense and prints a summary.

expenses = []

# Collect expenses until the user enters 0
while True:
    entry = input("Enter an expense or 0 to finish: ")

    try:
        amount = float(entry.replace("$", "").replace(",", ""))
    except ValueError:
        print("Invalid input. Please enter a number.")
        continue

    if amount == 0:
        break
    if amount < 0:
        print("Expenses cannot be negative. Please try again.")
        continue

    expenses.append(amount)

# Classify each expense
small_count = 0
moderate_count = 0
large_count = 0

for expense in expenses:
    if expense < 25:
        small_count += 1
    elif expense <= 100:
        moderate_count += 1
    else:
        large_count += 1

# Print the summary
print()
print("Expense Summary")
print("---------------")

if len(expenses) == 0:
    print("No expenses were entered.")
else:
    total = sum(expenses)
    average = total / len(expenses)

    print(f"Number of expenses: {len(expenses)}")
    print(f"Total: ${total:,.2f}")
    print(f"Average: ${average:,.2f}")
    print(f"Smallest expense: ${min(expenses):,.2f}")
    print(f"Largest expense: ${max(expenses):,.2f}")
    print()
    print(f"Small expenses: {small_count}")
    print(f"Moderate expenses: {moderate_count}")
    print(f"Large expenses: {large_count}")
