import json
import sys
from datetime import datetime

user = None
maximum_budget = 100000

with open("data/user.json", "r") as file:
    user = json.load(file)


print(user["budget"])
print(user["credit"])

user_budget = user["budget"]+user["credit"]
print(user_budget)

if user_budget >= maximum_budget or user_budget <= 0:
    print("Desila se greska. Vas budzet je veci od dozvoljenog ili je premali.")
    sys.exit()

expense = 0

while expense <= 0 or expense > user_budget:
    expense = int(input("Molim vas unesite iznos troskova: "))


with open("logs/expense_log.txt", "a") as file:
    remaining_budget = user_budget-expense
    message = (f"\nAmount: {expense},"
               f" User: {user["id"]},"
               f" Budget: {user_budget},"
               f" Preostali budzet: {remaining_budget}, "
               f" Date: {datetime.now()}")
    file.write(message)