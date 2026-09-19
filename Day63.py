print("Intent Prediction")
training_data = {
    "hello": "Greeting",
    "hi": "Greeting",
    "bye": "Goodbye",
    "track my order": "Order Tracking",
    "where is my order": "Order Tracking",
    "cancel my order": "Order Cancellation",
    "refund my money": "Refund",
    "what is my balance": "Balance Enquiry",
    "i forgot my password": "Password Reset"
}
user = input("You: ").lower()
found = False
for text, intent in training_data.items():
    if text in user:
        print("Predicted Intent:", intent)
        found = True
        break
if not found:
    print("Intent not recognized.")
