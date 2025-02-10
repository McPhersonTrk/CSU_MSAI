import hashlib
import json
import os

# Define a class to handle ATM operations with PIN hashing and data handling
class ATM:
    # ATM program with hashed PIN storage, file-based data persistence, and enhanced security features.
    # Define a function to initialize the ATM system with secure PIN storage and persistent balance
    def __init__(self, account_file="account_data.json"):
        # Initializes the ATM system by loading account data from a file.
        self.state = "Start"  # Initial state
        self.pin_attempts = 0  # Counter for incorrect PIN attempts
        self.max_attempts = 3  # Maximum allowed PIN attempts
        self.account_file = account_file  # JSON file to store account data
        
        # Load account data or initialize default values
        if os.path.exists(self.account_file):
            with open(self.account_file, "r") as file:
                self.account_data = json.load(file)
        else:
            self.account_data = {
                "pin_hash": self.hash_pin("1234"),  # Default PIN is hashed
                "balance": 1000.0,
                "account_active": True
            }
            self.save_account_data()

    # Define a function to hash the PIN using SHA-256
    def hash_pin(self, pin):
        # Hashes the provided PIN using SHA-256.
        return hashlib.sha256(pin.encode()).hexdigest()

    # Define a function to save account data to a file
    def save_account_data(self):
        # Saves the current account data to a JSON file.
        with open(self.account_file, "w") as file:
            json.dump(self.account_data, file, indent=4)

    # Define a function to handle inserting a card into the ATM
    def insert_card(self):
        # Handles inserting a card into the ATM and checks if the account is active.
        if not self.account_data["account_active"]:
            print("State: Reject Customer - Account Inactive")
            return
        
        print("Card Inserted.")
        self.state = "PIN Entry"
        print("State: PIN Entry - Prompting User for PIN")
        self.enter_pin()

    # Define a function to handle PIN entry and validation
    def enter_pin(self):
        # Handles real PIN entry and validation with hashed storage.
        while self.pin_attempts < self.max_attempts:
            user_pin = input("Enter your PIN: ")
            if self.hash_pin(user_pin) == self.account_data["pin_hash"]:
                self.state = "Select Transaction"
                print("State: Select Transaction - Displaying Options")
                self.select_transaction()
                return
            else:
                self.pin_attempts += 1
                print(f"Incorrect PIN. Attempt {self.pin_attempts}/{self.max_attempts}")
        
        self.state = "Reject Customer"
        print("State: Reject Customer - Max PIN Attempts Reached")

    # Define a function to handle transaction selection and perform operations
    def select_transaction(self):
        #Handles transaction selection and performs account modifications securely.
        while True:
            print("Select Transaction:")
            print("1. Withdraw Money")
            print("2. Deposit Money")
            print("3. Check Balance")
            print("4. Exit")
            choice = input("Enter choice: ")
            
            if choice == "1":
                amount = float(input("Enter amount to withdraw: "))
                if amount > self.account_data["balance"]:
                    print("State: Reject Transaction - Insufficient Balance")
                else:
                    self.withdraw(amount)
            elif choice == "2":
                amount = float(input("Enter amount to deposit: "))
                self.deposit(amount)
            elif choice == "3":
                print(f"Your current balance is: ${self.account_data['balance']}")
            elif choice == "4":
                self.end_transaction()
                return
            else:
                print("Invalid choice. Please select a valid transaction.")

    # Define a function to handle withdrawing money from the ATM
    def withdraw(self, amount):
        # Handles withdrawing money from the ATM and updates account data.
        if amount > self.account_data["balance"]:
            print("State: Reject Transaction - Insufficient Balance")
            return
        self.account_data["balance"] -= amount
        self.save_account_data()
        print(f"Withdrawal Successful. New Balance: ${self.account_data['balance']}")
        self.print_receipt()

    # Define a function to handle depositing money into the ATM
    def deposit(self, amount):
        #Handles depositing money into the ATM and updates account data.
        self.account_data["balance"] += amount
        self.save_account_data()
        print(f"Deposit Successful. New Balance: ${self.account_data['balance']}")
        self.print_receipt()

    # Define a function to handle printing transaction receipts
    def print_receipt(self):
        # Handles printing a transaction receipt.
        print("State: Print Receipt - Generating Statement")
        print("Transaction Complete.")

    # Define a function to handle ending the transaction session
    def end_transaction(self):
        # Ends the ATM session securely.
        self.state = "End Transaction"
        print("State: End Transaction - Thank you for using our ATM.")

# Start Enhanced ATM Program
atm = ATM()
atm.insert_card()
