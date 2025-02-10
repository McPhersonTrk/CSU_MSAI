class ATM:
    # Define a class to simulate ATM operations
    #ATM class that prints each step in order following the activity
    # diagram for an ATM system. The class includes methods to simulate ATM useage.

    # Define a function to initialize the ATM system
    def __init__(self):
        self.state = "Start"  # Initial state
        self.pin_attempts = 0  # Counter for incorrect PIN attempts
        self.max_attempts = 3  # Maximum allowed PIN attempts
        self.balance = 1000  # Example initial balance

    # Define a function to print each step in the ATM process
    def print_step(self, step):
        #Prints each step in the ATM transaction flow.
        print(f"Step: {step}")

    # Define a function to handle inserting a card into the ATM
    def insert_card(self):
        # Simulates inserting a card into the ATM.
        self.print_step("Card Inserted")
        self.state = "PIN Entry"
        self.print_step("State: PIN Entry - Prompting User for PIN")

    # Define a function to handle PIN entry and validation
    def enter_pin(self, correct):
        # Simulates PIN entry validation.
        self.print_step("Entering PIN...")
        if self.state != "PIN Entry":
            self.print_step("Error: Invalid State Transition")
            return
        self.print_step("State: Validate PIN - Checking PIN")
        if correct:
            self.state = "Select Transaction"
            self.print_step("State: Select Transaction - Displaying Options")
        else:
            self.pin_attempts += 1
            self.print_step(f"Incorrect PIN. Attempt {self.pin_attempts}/{self.max_attempts}")
            if self.pin_attempts >= self.max_attempts:
                self.state = "Reject Customer"
                self.print_step("State: Reject Customer - Max PIN Attempts Reached")
                return
            else:
                self.print_step("Prompting User for PIN Again")

    # Define a function to handle transaction selection
    def select_transaction(self, transaction_type, amount=0):
        #Simulates transaction selection and follows sequence from state diagram.
        self.print_step(f"Selecting Transaction: {transaction_type}")
        if transaction_type == "Withdraw" or transaction_type == "Transfer":
            self.state = "Check Balance"
            self.print_step("State: Check Balance - Fetching Account Balance")
            if amount > self.balance:
                self.state = "Reject Customer"
                self.print_step("State: Reject Customer - Insufficient Balance")
                return
            else:
                self.balance -= amount
                if transaction_type == "Withdraw":
                    self.state = "Withdraw Money"
                    self.print_step("State: Withdraw Money - Verifying Funds and Deducting Amount")
                else:
                    self.state = "Transfer Funds"
                    self.print_step("State: Transfer Funds - Verifying Accounts and Completing Transfer")
        elif transaction_type == "Deposit":
            self.state = "Deposit Money"
            self.print_step("State: Deposit Money - Accepting Funds and Updating Balance")
            self.balance += amount
        self.print_receipt()

    # Define a function to handle printing receipts
    def print_receipt(self):
        # Simulates printing a transaction receipt.
        self.print_step("State: Print Receipt - Generating Statement")
        self.end_transaction()

    # Define a function to handle ending the transaction session
    def end_transaction(self):
        # Ends the ATM session.
        self.state = "End Transaction"
        self.print_step("State: End Transaction - Session Complete")

# Simulate ATM Operations with step-by-step printing
atm = ATM()
atm.insert_card()
atm.enter_pin(False)  # First incorrect PIN attempt
atm.enter_pin(False)  # Second incorrect PIN attempt
atm.enter_pin(True)   # Third attempt - correct PIN
atm.select_transaction("Withdraw", 500)  # Withdraw $500
atm.select_transaction("Deposit", 200)   # Deposit $200
atm.select_transaction("Transfer", 300)  # Transfer $300