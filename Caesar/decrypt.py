##############################
# Caesar Cypher - Decrypt
##############################

# Define the alphabet that we are going to encode
LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

# Define variables to hold our message, the key and the translated message
message = 'NBCM CM MYWLYN'
key = 20
translated = ''

# Convert the message to uppercase
message = message.upper()

# Repetatively do something for every symbol in the message
for symbol in message:
# See if the current symbol is in the alphabet we defined earlier
    if symbol in LETTERS:
# if it is then we get a number that represents its position
        num = LETTERS.find(symbol)
# change the number based on the key
        num = (num + len(LETTERS) - key) % len(LETTERS)
# get the letter from the changed number
        translated = translated + LETTERS[num]
    else:
# the symbol is not in the alphabet so just add it unchanged
        translated = translated + symbol

# we have now been through every letter in the message so we can print the translated version
print(translated)
