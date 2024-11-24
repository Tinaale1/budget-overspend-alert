# budget-overspend-alert:
# A microservice to check budget categories and alert when spending goes over or is close to the set budget.
import json

# Function to get budget data from budget.txt
def get_budget_data():
    with open('budget.txt', 'r') as budget_file:
        return json.load(budget_file)


# Function to get transaction data from transaction.txt
def get_transaction_data():
    with open('transaction.txt', 'r') as transaction_file:
        return json.load(transaction_file)


# Function to calculate spending by category
def calculate_spending_by_category(transactions):
    spending_by_category = {}   # Create an empty dictionary to store spending for each category
    for transaction in transactions:  # Loop through each transaction in the list of transactions
        category = transaction["category"]  # Get the category of the current transaction
        amount = transaction["amount"]  # Get the amount of money spent in the current transaction
        if category in spending_by_category:  # Check if the category already exists in our dictionary
            spending_by_category[category] += amount  # If it does, add the amount to the existing total for that category
        else:
            spending_by_category[category] = amount  # If it doesn't, create a new entry in the dictionary with this amount
    return spending_by_category # After the loop, return the dictionary with all spending totals by category

# Function to check for overspending and write alerts to response.txt
def check_overspending(budget_data, spending_by_category):
    with open('response.txt', 'w') as response_file:
        for category in budget_data:  # Loop through each category in the budget data
            budget_limit = budget_data[category]  # Get the budget limit for the current category
            if category in spending_by_category:  # Check if we have any spending recorded for this category
                amount_spent = spending_by_category[category]  # Get the total amount spent in this category
                overspend_amount = amount_spent - budget_limit  # Calculate how much we've overspent

                # Check if we're overspending
                if overspend_amount > 0:
                    write_alert(response_file, category, overspend_amount)  # Write an overspend alert

                # Check if we're not overspending but we're close... so less than $10 left in the budget
                elif amount_spent > budget_limit - 10:
                    remaining_amount = budget_limit - amount_spent  # Calculate how much is left before reaching the budget limit
                    write_alert(response_file, category, remaining_amount=remaining_amount)  # Write a warning about being close to overspending


def main():
    # Read the request from request.txt
    with open('request.txt', 'r') as request_file:
        request = request_file.read().strip()

    # If the request is "check_overspending", run the budget check
    if request == "check_overspending":
        budget_data = get_budget_data()  # Get budget information like how much you can spend on different categories

        # Get the transaction information like what you have spent money on
        transaction_data = get_transaction_data()

        # Calculate total spending in each category using the transaction data
        spending_by_category = calculate_spending_by_category(transaction_data)

        # Check if any category has overspending and write alerts to 'response.txt'
        check_overspending(budget_data, spending_by_category)


if __name__ == "__main__":
    main()

