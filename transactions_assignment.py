# Transactions assignment
# SDDA - 28 February 2024
# By: Quinlan Caiger

from datetime import datetime


# Task 1
class Bank1:
    def __init__(
        self, accno, name, balance, numtransactions=None, transactions=None
    ):  # what def value to give to transactions? None doesn't work?
        self.accno = accno
        self.name = name
        self.balance = balance
        if numtransactions is None:
            self.numtransactions = 0
        else:
            self.numtransactions = numtransactions
        if transactions is None:
            self.transactions = []
        else:
            self.transactions = transactions

    # Task 2
    def display_balance(self):
        return f"Your balance is: R{self.balance:,}"

    # Task 3
    def withdraw(self, withdrawal):
        if withdrawal > self.balance:
            return f"Insufficient funds (R{self.balance:,}) to make this withdrawal (R{withdrawal:,})"
        else:
            self.balance -= withdrawal
            # Get today's date
            now = datetime.now()
            format = "%d %b"
            nicedate = now.strftime(format)
            self.numtransactions += 1
            self.statement(self.numtransactions, nicedate, "withdraw", withdrawal)
            return f"Success. {self.display_balance()}"

    # Task 4
    def deposit(self, depositamount):
        if depositamount < 0:
            return f"Invalid deposit amount of R{depositamount:,}"
        else:
            self.balance += depositamount
            # Get today's date
            now = datetime.now()
            format = "%d %b"
            nicedate = now.strftime(format)
            self.numtransactions += 1
            self.statement(self.numtransactions, nicedate, "deposit", depositamount)
            return f"Success. {self.display_balance()}"

    # add deposits and withdrawals to the statement as they happen
    # Statement function assignment
    def statement(self, idnum, date, transtype, amount):
        self.transactions.append(
            {"id": idnum, "Date": date, "Type": transtype, "Amount": amount}
        )
        # f"Hi {self.name}, here is your list of transactions:\n" for nice function later
        return self.transactions

    def print_transactions(self):
        return (
            f"Hello {self.name}, below are all your transactions:\n {self.transactions}"
        )


# create 3 accounts
gemma = Bank1(123, "Gemma Porrill", 15_000)
dhara = Bank1(124, "Dhara Kara", 50_001)
caleb = Bank1(125, "Caleb Potts", 100_000)

# print(gemma.balance, dhara.balance, caleb.balance)
# Task 2
print(gemma.display_balance())
# Task 3
# caleb.display_balance()
print(caleb.withdraw(2000))
print(caleb.display_balance())
print(caleb.withdraw(99000))
print(caleb.display_balance())
print(gemma.deposit(-1))
print(gemma.display_balance())
# Task 4
# dhara.deposit(10_000) -> Success. your balance is R60,001
print(dhara.deposit(10_000))
print(dhara.display_balance())


# List of Dicitonaries
# Assignment - Transactions
# Example output:
#    id   Date       Type     Amount
# 1.  1  29 Feb   withdraw       2000
# 2.  2  1 Mar    deposit        6000
# 3.  3  3 Mar    deposit        7000
print(gemma.deposit(10_000))
print(caleb.withdraw(1000))
print(dhara.deposit(15000))
print(dhara.print_transactions())
print(caleb.print_transactions())
print(gemma.print_transactions())
