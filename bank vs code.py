# Banking System using Functional Programming

# Function to create an account
def create_account(name, initial_balance=0):
    """
    Creates a new account with the given name and initial balance.
    """
    if initial_balance < 0:
        print("Error: Initial balance cannot be negative.")
        return None
    return {
        "name": name,
        "balance": initial_balance,
        "transactions": []
    }

# Function to deposit money
def deposit(account, amount):
    """
    Deposits the specified amount into the account.
    """
    if amount <= 0:
        print("Error: Deposit amount must be positive.")
        return account

    account["balance"] += amount
    account["transactions"].append(f"Deposit: ${amount:.2f}. New Balance: ${account['balance']:.2f}")
    print(f"Deposited ${amount:.2f}. New balance: ${account['balance']:.2f}")
    return account

# Function to withdraw money
def withdraw(account, amount):
    """
    Withdraws the specified amount from the account.
    """
    if amount <= 0:
        print("Error: Withdrawal amount must be positive.")
        return account

    if account["balance"] < amount:
        print("Error: Insufficient balance.")
        return account

    account["balance"] -= amount
    account["transactions"].append(f"Withdrawal: ${amount:.2f}. New Balance: ${account['balance']:.2f}")
    print(f"Withdrew ${amount:.2f}. New balance: ${account['balance']:.2f}")
    return account

# Function to check balance
def check_balance(account):
    """
    Displays the current balance of the account.
    """
    print(f"Current balance: ${account['balance']:.2f}")
    return account["balance"]

# Function to print transaction statement
def print_statement(account):
    """
    Prints a detailed transaction statement for the account.
    """
    print(f"\nTransaction Statement for {account['name']}:")
    if not account["transactions"]:
        print("No transactions available.")
    else:
        for transaction in account["transactions"]:
            print(transaction)

# Function to manage the account interactively
def manage_account():
    """
    Manages the account interactively through a menu-driven interface.
    """
    print("Welcome to the Banking System!")
    name = input("Enter your name to create an account: ")
    initial_balance = float(input("Enter the initial balance (default is $0): ") or 0)
    
    account = create_account(name, initial_balance)
    if not account:
        return  # Exit if account creation fails

    print(f"Account created for {account['name']} with an initial balance of ${account['balance']:.2f}.\n")

    while True:
        print("\nOptions:")
        print("1. Deposit Money")
        print("2. Withdraw Money")
        print("3. Check Balance")
        print("4. Print Transaction Statement")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            amount = float(input("Enter the amount to deposit: "))
            account = deposit(account, amount)
        elif choice == "2":
            amount = float(input("Enter the amount to withdraw: "))
            account = withdraw(account, amount)
        elif choice == "3":
            check_balance(account)
        elif choice == "4":
            print_statement(account)
        elif choice == "5":
            print("Thank you for using the Banking System. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    manage_account()