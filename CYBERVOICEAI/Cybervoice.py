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

print ("=====CYBERVOICE=====")
user_message = input ("Enter a suspicious message: ")
print ("------------------------------------------------")
detected_words = analyze_message(user_message)
print ()
if detected_words:
  if "otp" in detected_words:
    print ("Never share your OTP with anyone.")
  if "password" in detected_words:
    print ("Never share your password with anyone.")
  if "click here" in detected_words:
    print ("Avoid clicking unknown links.")
  if "bank account" in detected_words:
    print ("Verify through your bank's official channels.")
  if "urgent" in detected_words:
    print ("Be careful of messages that pressure you to act immediately.")

else:
  print ("\nNo matching warning words found.")
  print ("This does NOT mean the message is safe.")
print ()
print ("------------------------------------------------")
