def main():
    email_to_name = {}
    email = input("Email: ")
    while email != '':
        userName = get_user_name(email)
        check_name(email, userName, email_to_name)
        email = input("Email: ")

    for email, userName in email_to_name.items():
        print(f"{userName} ({email})")


def check_name(email, userName, email_to_name):
    checkKey = input(f"Is your name? {userName} (Y/n) ")
    if checkKey.upper() == "N" or checkKey == "no":
        userName = input("Name: ")
    email_to_name[email] = userName


def get_user_name(email):
    possibleName = email.split('@')[0]
    parts = possibleName.split('.')
    userName = " ".join(parts).title()
    return userName


main()
