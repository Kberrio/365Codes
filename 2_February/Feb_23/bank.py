class BankAccount:
    def __init__(self, account_number, holder_name, balance=0):
        self.account_number = account_number
        self.holder_name = holder_name
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited {amount} into account {self.account_number}.")
        else:
            print("Invalid deposit amount.")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew {amount} from account {self.account_number}.")
        else:
            print("Insufficient funds.")

    def get_balance(self):
        return self.balance

    def __str__(self):
        return f"Account Number: {self.account_number}, Holder Name: {self.holder_name}, Balance: {self.balance}"


class Bank:
    def __init__(self):
        self.accounts = {}

    def add_account(self, account):
        if account.account_number not in self.accounts:
            self.accounts[account.account_number] = account
            print("Account added successfully.")
        else:
            print("Account number already exists.")

    def remove_account(self, account_number):
        if account_number in self.accounts:
            del self.accounts[account_number]
            print("Account removed successfully.")
        else:
            print("Account not found.")

    def get_account_balance(self, account_number):
        if account_number in self.accounts:
            return self.accounts[account_number].get_balance()
        else:
            print("Account not found.")
            return None

    def transfer(self, from_account_number, to_account_number, amount):
        if from_account_number in self.accounts and to_account_number in self.accounts:
            if self.accounts[from_account_number].get_balance() >= amount:
                self.accounts[from_account_number].withdraw(amount)
                self.accounts[to_account_number].deposit(amount)
                print("Transfer successful.")
            else:
                print("Insufficient funds for transfer.")
        else:
            print("One or both accounts not found.")


# Example usage:
if __name__ == "__main__":
    bank = Bank()

    account1 = BankAccount("001", "Alice", 1000)
    account2 = BankAccount("002", "Bob", 500)

    bank.add_account(account1)
    bank.add_account(account2)

    print("Alice's balance:", bank.get_account_balance("001"))
    print("Bob's balance:", bank.get_account_balance("002"))

    bank.transfer("001", "002", 300)

    print("Alice's balance after transfer:", bank.get_account_balance("001"))
    print("Bob's balance after transfer:", bank.get_account_balance("002"))
