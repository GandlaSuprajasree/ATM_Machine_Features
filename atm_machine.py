from data import ACCOUNTS
from atm_logic import check_balance, deposit, withdraw, transaction_history

def menu():
    """Step 1: Prepare while loop for menu options."""
    while True:
        print("\n===== ATM Machine =====")
        print("1. Check Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Transaction History")
        print("5. Exit")
        
        choice = input("Enter your choice: ")

        if choice == '5':
            # Step 6: Break loop when user chooses Exit.
            print("Thank you for using the ATM. Goodbye!")
            break

        name = input("Enter your name: ")
        try:
            pin = int(input("Enter your PIN: "))
        except ValueError:
            print("Invalid PIN. Please enter a valid number.")
            continue

        if choice == '1':
            check_balance(ACCOUNTS, name, pin)
        elif choice == '2':
            try:
                amount = float(input("Enter amount to deposit: "))
                deposit(ACCOUNTS, name, pin, amount)
            except ValueError:
                print("Invalid amount. Please enter a number.")
        elif choice == '3':
            try:
                amount = float(input("Enter amount to withdraw: "))
                withdraw(ACCOUNTS, name, pin, amount)
            except ValueError:
                print("Invalid amount. Please enter a number.")
        elif choice == '4':
            transaction_history(ACCOUNTS, name, pin)
        else:
            print("Invalid choice. Please select an option from 1 to 5.")

# Run the menu function when the script is executed directly.
if __name__ == "__main__":
    menu()


