from isEnglish import isEnglish

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

def crack(message):
    for key in range(len(LETTERS)):
        plaintext = decrypt(key, message)
        if isEnglish(plaintext):
            return plaintext
    return None
#####################################

# This is the main part of the programme flow

modes = 'edc' # The allowed modes
mode = 'x' # The mode we are going to use

# Whichever mode we use we will always need a message
message = raw_input("Please type your message: ")

while not mode in modes:
    # Get the desired mode from the user
    mode = raw_input("encrypt, decrypt, or crack? (e/d/c): ")

if mode == 'c':
    message = crack(message)
    if message != None:
        print message
    else:
        print "Unable to decypher this message"
else:
    # We will need a key from the user
    key = int(raw_input("Please type a whole number for the key: "))
    if mode == 'd':
        print decrypt(key, message)
    else:
        print encrypt(key, message)
