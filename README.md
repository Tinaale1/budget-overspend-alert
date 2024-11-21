## Budget Overspend Alert Microservice A

### Communication Contract

This microservice helps you track your spending by analyzing your transactions against your budget. It communicates via text files: **request.txt** to send data and response.txt to receive alerts.

Request Data: This provides your budget and transactions in request.txt (JSON format).

Receive Alerts: This reads the overspend alerts from response.txt.

### A. How to Programmatically REQUEST Data from the Microservice

To use this microservice, follow these steps to send data:

1. Create a file named request.txt in the same directory as the microservice.
2. Write your request data in JSON format inside request.txt. The JSON should include:
    -A dictionary with your budget categories and limits.
    -A list of transactions to analyze.

**Example Request Call:**

```json
{
    "budget": {
        "Food": 100.0,
        "Housing": 500.0,
        "Transportation": 150.0,
        "Entertainment": 50.0,
        "Miscellaneous": 30.0
    },
    "transactions": [
        {
            "date": "2024-11-01",
            "amount": 120.0,
            "category": "Food",
            "payment_method": "credit card",
            "notes": "grocery shopping"
        },
        {
            "date": "2024-11-05",
            "amount": 40.0,
            "category": "Entertainment",
            "payment_method": "cash",
            "notes": "movie night"
        }
    ]
}
```
3. **Run the Microservice:**

In your terminal, go to the directory that has overspend_alert.py.
Run the microservice using: ```python3 overspend_alert.py```

### B. How to Programmatically RECEIVE Data from the Microservice

After the microservice processes the request, it writes the result in a file called response.txt.

**Example Receive Call:**
Here's an example of how to programmatically read data from response.txt:
```
with open('response.txt', 'r') as file:
    response = file.read()

print("Microservice Response:\n", response)
```
**Example Output Call from response.txt:**
```
Alert: You've overspent in Food by $20.0!
Warning: You're close to overspending in Miscellaneous. Only $5.0 left!
```
### D. UML sequence diagram
![UML Sequence Diagram](images/Screen%20Shot%202024-11-17%20at%201.04.50%20PM.png)
