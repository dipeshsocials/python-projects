def is_palindrome(text):
    cleaned = "".join(char.lower() for char in text if char.isalnum())
    return cleaned == cleaned[::-1]


print("===== Palindrome Checker =====")

text = input("Enter text: ")

if is_palindrome(text):
    print("✅ It is a palindrome.")
else:
    print("❌ It is not a palindrome.")
