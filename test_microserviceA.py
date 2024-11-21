import os

# Write a request to request.txt
def send_request_to_microservice():
    with open('request.txt', 'w') as request_file:
        request_file.write("check_overspending")
    print("Request sent to microservice.")

# Run the microservice - process the request
def run_microservice():
    print("Running the microservice...")
    os.system('python3 overspend_alert.py')

# Read the response from response.txt
def receive_response_from_microservice():
    print("Reading response from microservice...")
    with open('response.txt', 'r') as response_file:
        response = response_file.read()
    return response

# Main function handling the request and response
if __name__ == "__main__":
    # Send request
    send_request_to_microservice()

    # Run microservice
    run_microservice()

    # Receive response
    response = receive_response_from_microservice()
    print("\nMicroservice Response:")
    print(response)


