
# =====================================================
# CYBERVOICE
# A Beginner-Friendly Cybersecurity Awareness Assistant
# Version 1.0
# =====================================================

# 1. Cybersecurity warning database

security_rules = {
    "otp": {
        "severity": "HIGH",
        "english": "Never share your OTP with anyone.",
        "tamil": "உங்கள் OTP-ஐ யாரிடமும் பகிர வேண்டாம்."
    },
    "password": {
        "severity": "HIGH",
        "english": "Never share your password. Use strong, unique passwords.",
        "tamil": "உங்கள் கடவுச்சொல்லை யாரிடமும் பகிர வேண்டாம்."
    },
    "pin": {
        "severity": "HIGH",
        "english": "Never share your banking PIN or UPI PIN.",
        "tamil": "உங்கள் வங்கி அல்லது UPI PIN-ஐ யாரிடமும் பகிர வேண்டாம்."
    },
    "click here": {
        "severity": "MEDIUM",
        "english": "Avoid clicking unexpected links. Check the website address first.",
        "tamil": "எதிர்பாராத இணைப்புகளை அழுத்த வேண்டாம். இணையதள முகவரியைச் சரிபார்க்கவும்."
    },
    "urgent": {
        "severity": "MEDIUM",
        "english": "Scammers may pressure you to act quickly. Take time to verify.",
        "tamil": "உடனே செயல்பட வேண்டும் என்று அழுத்தம் கொடுக்கும் செய்திகளை கவனமாகச் சரிபார்க்கவும்."
    },
    "blocked": {
        "severity": "MEDIUM",
        "english": "Do not trust account-blocking claims without verification. Contact your bank officially.",
        "tamil": "கணக்கு முடக்கப்பட்டதாக வரும் செய்திகளை உடனே நம்ப வேண்டாம். வங்கியை அதிகாரப்பூர்வமாகத் தொடர்புகொள்ளவும்."
    },
    "verify": {
        "severity": "MEDIUM",
        "english": "Verify requests through the official website or app. Do not use unknown links.",
        "tamil": "அதிகாரப்பூர்வ இணையதளம் அல்லது செயலி மூலம் மட்டும் சரிபார்க்கவும்."
    },
    "bank account": {
        "severity": "MEDIUM",
        "english": "Never provide banking details through suspicious messages or links.",
        "tamil": "சந்தேகமான செய்திகள் அல்லது இணைப்புகள் மூலம் வங்கி விவரங்களை வழங்க வேண்டாம்."
    },
    "prize": {
        "severity": "MEDIUM",
        "english": "Be careful with unexpected prize or lottery messages. Do not pay fees to claim prizes.",
        "tamil": "எதிர்பாராத பரிசு அல்லது லாட்டரி செய்திகளை கவனமாக அணுகவும். பரிசைப் பெற பணம் செலுத்த வேண்டாம்."
    },
    "won": {
        "severity": "LOW",
        "english": "Unexpected winning messages may be scams. Verify the sender independently.",
        "tamil": "எதிர்பாராத வெற்றி செய்திகள் மோசடியாக இருக்கலாம். அனுப்பியவரை தனியாகச் சரிபார்க்கவும்."
    },
    "link": {
        "severity": "LOW",
        "english": "Check links carefully before opening them.",
        "tamil": "இணைப்புகளைத் திறப்பதற்கு முன் கவனமாகச் சரிபார்க்கவும்."
    },
    "download": {
        "severity": "LOW",
        "english": "Download apps and files only from trusted sources.",
        "tamil": "நம்பகமான மூலங்களிலிருந்து மட்டும் செயலிகள் மற்றும் கோப்புகளைப் பதிவிறக்கவும்."
    }
}


# 2. General safety tips

safety_tips = [
    "Never share OTPs, passwords, PINs or banking credentials.",
    "Do not click unexpected links.",
    "Never install apps sent by unknown people.",
    "Verify bank messages using the official bank app or phone number.",
    "Do not send money because someone threatens or pressures you.",
    "Report suspected cybercrime through official channels."
]


# 3. Analyze the message

def analyze_message(message):

    found_warnings = []

    # Convert message to lowercase
    message = message.lower()

    # Check every warning keyword
    for word in security_rules:

        if word in message:
            found_warnings.append(word)

    return found_warnings


# 4. Calculate warning level

def get_severity(found_warnings):

    if not found_warnings:
        return "NO MATCHING WARNING WORDS"

    levels = ["LOW", "MEDIUM", "HIGH"]

    highest_level = "LOW"

    for word in found_warnings:

        severity = security_rules[word]["severity"]

        if levels.index(severity) > levels.index(highest_level):
            highest_level = severity

    return highest_level


# 5. Display analysis results

def display_results(found_warnings, language):

    print("\n" + "=" * 45)
    print("             ANALYSIS RESULTS")
    print("=" * 45)

    if not found_warnings:

        print("\nNo matching warning words were detected.")

        print("\nIMPORTANT:")
        print("This does NOT mean the message is safe.")
        print("The program checks keywords only.")

        return

    severity = get_severity(found_warnings)

    print("\nPotential warning signs detected!")
    print("Warning level:", severity)

    print("\nDetected keywords:")

    for word in found_warnings:
        print("-", word)

    print("\nSAFETY RECOMMENDATIONS:")

    for word in found_warnings:

        advice = security_rules[word][language]

        print("-", advice)

    print("\nRemember:")
    print("Never share OTPs, passwords or PINs.")


# 6. Show general safety tips

def show_safety_tips(language):

    print("\n" + "=" * 45)
    print("             CYBER SAFETY TIPS")
    print("=" * 45)

    if language == "english":

        for number, tip in enumerate(safety_tips, start=1):
            print(f"{number}. {tip}")

    else:

        tamil_tips = [
            "OTP, கடவுச்சொல் மற்றும் PIN-ஐ யாரிடமும் பகிர வேண்டாம்.",
            "எதிர்பாராத இணைப்புகளை அழுத்த வேண்டாம்.",
            "தெரியாத நபர்கள் அனுப்பும் செயலிகளை நிறுவ வேண்டாம்.",
            "வங்கிச் செய்திகளை அதிகாரப்பூர்வ செயலி மூலம் சரிபார்க்கவும்.",
            "அச்சுறுத்தி பணம் கேட்பவர்களை நம்ப வேண்டாம்.",
            "சந்தேகமான இணையக் குற்றங்களை அதிகாரப்பூர்வமாகப் புகாரளிக்கவும்."
        ]

        for number, tip in enumerate(tamil_tips, start=1):
            print(f"{number}. {tip}")


# 7. Select language

def select_language():

    while True:

        print("\nSELECT YOUR LANGUAGE")
        print("1. English")
        print("2. Tamil")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            return "english"

        elif choice == "2":
            return "tamil"

        else:
            print("Invalid choice. Please select 1 or 2.")


# 8. Main program

def main():

    print("\n" + "=" * 45)
    print("              CYBERVOICE")
    print("  Speak in your language. Understand the threat.")
    print("=" * 45)

    print("\nWelcome to CyberVoice!")

    language = select_language()

    while True:

        print("\n" + "-" * 45)
        print("                 MAIN MENU")
        print("-" * 45)

        print("1. Analyze a suspicious message")
        print("2. View cyber safety tips")
        print("3. Change language")
        print("4. Exit")

        choice = input("\nEnter your choice: ").strip()

        if choice == "1":

            print("\nPaste or type the suspicious message.")
            print("Do NOT enter actual OTPs, passwords or PINs.")

            user_message = input("\nMessage: ").strip()

            if not user_message:
                print("Please enter a message.")
                continue

            detected_words = analyze_message(user_message)

            display_results(detected_words, language)

        elif choice == "2":

            show_safety_tips(language)

        elif choice == "3":

            language = select_language()

        elif choice == "4":

            print("\nThank you for using CyberVoice!")
            print("Stay alert. Stay safe online.")
            break

        else:

            print("\nInvalid choice. Please select 1, 2, 3 or 4.")


# 9. Start the application

if __name__ == "__main__":
    main()
