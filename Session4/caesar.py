##############################
# Caesar Cypher
##############################

# Define the alphabet that we are going to encode
LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

# Define functions that do the work of the cypher
def caesar(key, message):
    # Convert the message to uppercase
    message = message.upper()
    translated = ''

    # Repetatively do something for every symbol in the message
    for symbol in message:
    # See if the current symbol is in the alphabet we defined earlier
        if symbol in LETTERS:
    # if it is then we get a number that represents its position
            num = LETTERS.find(symbol)
    # change the number based on the key
            num = (num + key) % len(LETTERS)
    # get the letter from the changed number
            translated = translated + LETTERS[num]
        else:
    # the symbol is not in the alphabet so just add it unchanged
            translated = translated + symbol

    # we have now been through every letter in the message so we can return the translated version
    return translated

# Define wrapper functions
def encrypt(key, message):
    return caesar(key, message)

def decrypt(key, message):
    decrypt_key = len(LETTERS) - key
    return caesar(decrypt_key, message)

def main():
    # This function is run if we run the file directly using python
    # We can use it to encrypt and decrypt messages with user input

    modes = 'ed' # The allowed modes
    mode = 'x' # The mode we are going to use (Currently invalid)

    # The while loop allows us to repeat the question if we don't get a
    # good answer
    while not mode in modes:
        # Get the desired mode from the user
        # Python2
        #mode = raw_input("Would you like to encrypt or decrypt (e/d): ")
        # Python3
        mode = input("Would you like to encrypt or decrypt (e/d): ")

    # Get the message from the user
    # Python2
    #message = raw_input("Please type your message: ")
    # Python3
    message = input("Please type your message: ")

    # We will need a key from the user
    # Python2
    #key = int(raw_input("Please type a whole number for the key: "))
    # Python3
    key = int(input("Please type a whole number for the key: "))
    if mode == 'd':
        print (decrypt(key, message))
    else:
        print (encrypt(key, message))

#####################################
# if we run this file with Python like:
# python caesar.py
# then the variable __name__ will be set to "__main__"
# and we will therefore run the main() function

if __name__ == '__main__':
    main()
