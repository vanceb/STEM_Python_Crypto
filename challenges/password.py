import io

def loadPasswords():
    passwds = {}
    with io.open("passwords.txt", 'r', encoding='utf-8') as file:
        for passwd in file:
            passwd = passwd.strip()
            passwds[passwd] = None
    return passwds


if __name__ == "__main__":

    bad_passwords = loadPasswords()
    password = input("Please try a password: ")
    if password in bad_passwords:
        print("That is a bad password!")
    else:
        print("Great!")

