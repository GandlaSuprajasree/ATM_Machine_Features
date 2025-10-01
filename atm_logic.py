def authenticate_user(accounts, name, pin):
    """Authenticates the user and returns the account dictionary if successful."""
    for account in accounts:
        if account["name"].lower() == name.lower() and account["pin"] == pin:
            return account
    return None

def check_balance(accounts, name, pin):
    """Step 2: Show balance if name & PIN match."""
    account = authenticate_user(accounts, name, pin)
    if account:
        print(f"Current Balance for {name}: ₹{account['balance']:.2f}")
    else:
        print("Invalid name or PIN")

def deposit(accounts, name, pin, amount):
    """Step 3: Add money & record transaction."""
    account = authenticate_user(accounts, name, pin)
    if account:
        if amount > 0:
            account["balance"] += amount
            account["transactions"].append(f"Deposited ₹{amount:.2f}")
            print(f"Deposited ₹{amount:.2f} successfully. New balance: ₹{account['balance']:.2f}")
        else:
            print("Invalid deposit amount. Amount must be positive.")
    else:
        print("Invalid name or PIN.")

def withdraw(accounts, name, pin, amount):
    """Step 4: Withdraw money if sufficient balance & record transaction."""
    account = authenticate_user(accounts, name, pin)
    if account:
        if amount > 0:
            if account["balance"] >= amount:
                account["balance"] -= amount
                account["transactions"].append(f"Withdrew ₹{amount:.2f}")
                print(f"Withdrew ₹{amount:.2f} successfully. New balance: ₹{account['balance']:.2f}")
            else:
                print("Insufficient balance.")
        else:
            print("Invalid withdrawal amount. Amount must be positive.")
    else:
        print("Invalid name or PIN.")

def transaction_history(accounts, name, pin):
    """Step 5: Show all deposits/withdrawals."""
    account = authenticate_user(accounts, name, pin)
    if account:
        print(f"Transaction History for {name}:")
        if account["transactions"]:
            for transaction in account["transactions"]:
                print(f"- {transaction}")
        else:
            print("No transactions to display.")
    else:
        print("Invalid name or PIN.")
