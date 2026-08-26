# College Enquiry Menu Chatbot

responses = {
    "1": "Course Fee: ₹15,000 per year.",
    "2": "Duration: 3 years.",
    "3": "Eligibility: Pass in Higher Secondary (Plus Two).",
    "4": "Location: Kochi, Kerala.",
    "5": "Contact: +91 9876543210.",
    "6": "Hostel Information: Separate hostel facilities are available for boys and girls.",
    "7": "Placement Information: Training and placement assistance is available."
}
while True:
    print("\n===== College Enquiry Chatbot =====")
    print("1. Course Fee")
    print("2. Duration")
    print("3. Eligibility")
    print("4. Location")
    print("5. Contact")
    print("6. Hostel Information")
    print("7. Placement Information")
    print("8. Exit")
    choice = input("Enter your choice (1-8): ")
    if choice == "8":
        print("Thank you for using the chatbot!")
        break
    elif choice in responses:
        print("\nBot:", responses[choice])
    else:
        print("\nInvalid choice! Please select a valid option.")
    again = input("\nWould you like to continue? (yes/no): ").lower()
    if again == "no":
        print("Thank you! Have a nice day.")
        break
