# Between 10 and 20 characters long.
# Contains either one of “!” or “$”.
# Does not contain the word “password”.

def has_10_to_20_characters(password):
    return 10 <= len(password) <= 20

def has_spezial_character(password):
    return "!" in password or "$" in password

def password_is_not_in_password(password):
    return "password" not in password

def check_conditions(word_lenght, special_characters, has_passowrd):
    return word_lenght and special_characters and has_passowrd

def get_and_validate_password():
    password_is_valid = False
    valid_password = ""
    password = ""
    while not password_is_valid: # so lange password_is_valid == False
        password = input("choose a password: ")
        password_is_valid = check_conditions(has_10_to_20_characters(password), has_spezial_character(password), password_is_not_in_passwordz(password))
        valid_password = password
    return valid_password

def main():
  valid_password = get_and_validate_password()
  print("The chosen password is", valid_password)


if __name__ == "__main__":
  main()