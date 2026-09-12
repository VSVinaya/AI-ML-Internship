print("Convert the sentence to lowercase")
text = "HELLO, I WANT TO BOOK A TICKET."
lowercase_text = text.lower()
print("Lowercase:", lowercase_text)

print("Tokenize the sentence")
text = "I love learning Artificial Intelligence."
tokens = text.split()
print("Tokens:", tokens)

print("Identify Intent and Entities")
text = "Book a flight to Chennai on Friday."
intent = "Flight Booking"
destination = "Chennai"
date = "Friday"
print("User:", text)
print("Intent:", intent)
print("Destination:", destination)
print("Date:", date)

print("Tokenize a sentence using split()")
sentence = input("Enter a sentence: ")
tokens = sentence.split()
print("Tokens:", tokens)
