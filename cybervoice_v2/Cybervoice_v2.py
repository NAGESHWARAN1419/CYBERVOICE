
def analyze_message(message):

    warning_words = [
        "otp",
        "urgent",
        "blocked",
        "verify",
        "password",
        "click here",
        "bank account"
    ]

    found_warnings = []

    for word in warning_words:
        if word in message.lower():
            found_warnings.append(word)

    return found_warnings


# Dictionary containing safety advice
advice = {
    "otp": "Never share your OTP with anyone.",
    "password": "Never share your password with anyone.",
    "click here": "Avoid clicking unknown links.",
    "bank account": "Verify through your bank's official channels.",
    "urgent": "Be careful of messages that pressure you to act immediately.",
    "blocked": "Contact the organization through its official channels.",
    "verify": "Do not enter personal information through untrusted links."
}


# Main program
print("================================")
print("          CYBERVOICE")
print("================================")

user_message = input("Enter a suspicious message: ")

print("--------------------------------")

detected_words = analyze_message(user_message)

if detected_words:

    print("Potential warning signs detected!")
    print("Detected words:", detected_words)
    print()
    print("SAFETY ADVICE:")

    for word in detected_words:
        if word in advice:
            print("-", advice[word])

else:
    print("No matching warning words found.")
    print("This does NOT mean the message is safe.")

print("--------------------------------")
print("Thank you for using CyberVoice!")
print("================================")
