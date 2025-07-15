balance = 1000

def show_menu():
    print("\n--- ATM Menu ---")
    print("1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")

while True:
    show_menu()
    try:
        choice = int(input("Enter choice: "))
        if choice == 1:
            print(f"Current Balance: ₹{balance}")
        elif choice == 2:
            amount = float(input("Enter amount to deposit: ₹"))
            if amount <= 0:
                raise ValueError("Amount must be positive.")
            balance += amount
            print(f"₹{amount} deposited. New balance: ₹{balance}")
        elif choice == 3:
            amount = float(input("Enter amount to withdraw: ₹"))
            if amount <= 0:
                raise ValueError("Amount must be positive.")
            if amount > balance:
                raise ValueError("Insufficient balance.")
            balance -= amount
            print(f"₹{amount} withdrawn. New balance: ₹{balance}")
        elif choice == 4:
            print("Thank you for using the ATM.")
            break
        else:
            print("Invalid option. Try again.")
    except ValueError as e:
        print("Error:", e)