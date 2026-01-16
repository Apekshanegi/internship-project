import re
#Create helper functions
def check_length(password):
    return len(password) >= 8


def check_upper_lower(password):
    return bool(re.search(r"[A-Z]", password)) and bool(re.search(r"[a-z]", password))


def check_number(password):
    return bool(re.search(r"[0-9]", password))


def check_special(password):
    return bool(re.search(r"[!@#$%^&*(),.?\":{}|<>]", password))

# Strength calculator

def password_strength(password):
    score = 0

    if check_length(password):
        score += 1
    if check_upper_lower(password):
        score += 1
    if check_number(password):
        score += 1
    if check_special(password):
        score += 1

    return score


def main():
    password = input("Enter your password: ")
    score = password_strength(password)

    if score <= 2:
        print("Weak Password ❌")
    elif score <= 4:
        print("Medium Password ⚠️")
    else:
        print("Strong Password ✅")


if __name__ == "__main__":
    main()


