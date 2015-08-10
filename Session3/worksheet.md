# Session 3 - Programming a Python Caesar Cypher

Last week you went over the basics of the Python language.  This week we will expand on the basics to create a Python version of the Caesar cypher wheel you used in the first week.  We will give you the programme to encrypt your own messages, and ask you to read the code and comments to try and understand how it works.  You will then modify the code to create a decryption programme so you can read secret messages from other people.

## Reading code

When reading code it is alwas a good idea to read from top to bottom.  There are always times when you will need to jump around in the code to work out what is going on, but the first time you read the code try to look from top to bottom and understand the different sections.  Here are a few pointers to help you:

### Comments

Comments in Python code start with a hash `#`.  Any text following the hash on the same line is considered to be a comment and is ignored by Python.  It is just there for you, the programmer, to explain better what is happening.  When you write code it is good practice to include comments.  You may remember what is happening if you come back to the code in a few days, but in a few weeks it may not be so easy.

### Indentation

In Python, indentation is important.  The level of the indent identifies a block of text that will be run together.   The line that comes before an indented block will end with a `:`, and should give you a clue about when and how it will be run.  The end of a block of code can be identified by a less-indented line of code.    Indentation can happen multiple times - blocks of code within other blocks of code.i  **Note:** comments are ignored and do not have to be indented, but the code is easier to read if you indent them to match the code that they relate to.

## Caesar encryption

Take a look at the code below, read the code and the comments to try and understand how the programme works.  Note the indented blocks of code, there are 3 main blocks of code;  the unindented code, the code that is preceded by the `for` loop, and finally the code that is surrounded by the `if` / `else` statements

``` {.python .numberLines}
##############################
# Caesar Cypher - Encrypt
##############################

# Define the alphabet that we are going to encode
LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

# Define variables to hold our message, the key and the translated message
message = 'This is secret'
key = 20
translated = ''

# Convert the message to uppercase
message = message.upper()

# Repetatively do something for every symbol in the message
for symbol in message:
    # See if the current symbol is in the string of letters we defined earlier
    if symbol in LETTERS:
        # if it is then we get a number that represents its position
        num = LETTERS.find(symbol)
        # change the number based on the key
        num = (num + key) % len(LETTERS)
        # get the letter from the changed number and add it to the end of our translated message
        translated = translated + LETTERS[num]
    else:
        # the symbol is not in the alphabet so just add it unchanged
        translated = translated + symbol

# we have now been through every letter in the message so we can print the translated version
print(translated)
```

### Run the code

Open the `encrypt.py` programme in the `Session 3` folder.

Press the `F5` key to run the programme and look at the output.  Use your code wheel from the first week and encode the same message with the same key to make sure that the code works as we expect by comparing the message you get from the code wheel with the message that the programme generates.  They should be the same if our programme can be used instead of the code wheel.

### Experiment by changing things

* Change the message to your own message
* Change the key and see how your message changes
* What happens if you encrypt an already-encrypted message with a key equal to `26 - encryption-key`?
* What is special about the number 26?
* Can you add one line to your code to make it decrypt messages - think about modifying the key in the code...
