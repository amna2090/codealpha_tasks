import re

def check_password_strength(password):
    
    length = len(password) >= 8
    uppercase = re.search(r"[A-Z]", password)
    lowercase = re.search(r"[a-z]", password)
    digit = re.search(r"[0-9]", password)
    special = re.search(r"[!@#$%^&*(),.?\":{}|<>]", password)

    score = 0

    if length:
        score += 1
    if uppercase:
        score += 1
    if lowercase:
        score += 1
    if digit:
        score += 1
    if special:
        score += 1

    if score == 5:
        print("Strong Password ")
    elif score >= 3:
        print("Medium Password ")
    else:
        print("Weak Password ")


password = input("Enter your password: ")
check_password_strength(password)
