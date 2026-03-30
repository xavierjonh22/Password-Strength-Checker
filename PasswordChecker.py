def check_length(password):

    return len(password) >= 8


def check_upper_lower(password):

    has_upper = any(char.isupper() for char in password)
    has_lower = any(char.islower() for char in password)
    return has_upper and has_lower


def check_special_character(password):

    return any(char in "!@#" for char in password)


def main():

    while True:
        password = input("Enter a password: ")
        errors = []

        if not check_length(password):
            errors.append("Must be at least 8 characters long.")
        if not check_upper_lower(password):
            errors.append("Must contain both uppercase and lowercase letters.")
        if not check_special_character(password):
            errors.append("Must include at least one special character (!, @, #).")

        if errors:
            print("Password does not meet the requirements:", " ".join(errors))
        else:
            print("Password is strong!")
            break


if __name__ == "__main__":
    main()
