 ATM Machine (Python Project)

 Project Overview
This is a simple ATM Machine simulation project implemented in Core Python  
It allows users to:
- Check balance  
- Deposit money  
- Withdraw money  
- View transaction history  

The project is designed in a modular structure with three files:
- data.py → Stores account data  
- atm_logic.py → Contains core ATM logic (functions for deposit, withdraw, balance check)  
- atm_machine.py → Provides the menu-driven interface for the ATM system  


Project Structure

ATM-Machine-Project/
- data.py          # Stores account details
- atm_logic.py     # ATM business logic (deposit, withdraw, etc.)
- atm_machine.py   # Main menu-driven interface
- README.md        # Project documentation

 Features
- Authentication -> using `name` and `PIN`  
- Check Balance -> Displays current account balance  
- Deposit Money -> Adds money to the account and records the transaction  
- Withdraw Money -> Deducts amount if sufficient balance exists  
- Transaction History -> Shows all deposits & withdrawals  
- Exit Option -> Ends the session  

How to Run
1. Clone or download the project files.    
2. Open a terminal in the project directory.  
3. Run the project using:
   python atm_machine.py

 Example Run
===== ATM Machine =====
1. Check Balance
2. Deposit Money
3. Withdraw Money
4. Transaction History
5. Exit
Enter your choice: 1
Enter your name: Ravi
Enter your PIN: 1234
Current Balance for Ravi: ₹5000.00

 Preloaded Accounts
The file data.py contains some predefined accounts:

| Name   | Balance | PIN  |
|--------|---------|------|
| Ravi   | 5000    | 1234 |
| Priya  | 7000    | 2345 |
| Suresh | 10000   | 3456 |
| Anita  | 3000    | 4567 |
| Kiran  | 8500    | 5678 |
| Meena  | 12000   | 6789 |
| Vamsi  | 4500    | 7890 |
| Rohit  | 6000    | 8901 |
| Sonia  | 9000    | 9012 |
| Neha   | 11000   | 1122 |


