# We are going to use the decrypt function and the LETTERS
# from caesar.py so we need to tell python
from caesar import LETTERS
from caesar import decrypt

def main():
    # Get the message from the user
    # Python2
    #message = raw_input("Please type the encrypted message: ")
    # Python3
    message = input("Please type the encrypted message: ")

    # Try every key in sequence
    for key in range(len(LETTERS)):
        # Print out the key and the decrypted text for the user
        print(str(key) + ": " + decrypt(key, message))

if __name__ == '__main__':
    main()
