# Short course in Python using codes and encryption as the topic

## Session 1

[Reference and
Inspiration](https://inventwithpython.com/hacking/chapter1.html)

-   Introduce the course
-   Introduce the Caesar cypher
-   Make your own paper Caesar cypher decoding wheel
-   Encode a message for a friend. Give them the encoded message and
    tell them the key and let them decode it
-   Homework
    -   Give students a coded message and ask them to think about how
        they could decode it without knowing the key
    -   W ZCJS QCRSG. TCF WBTCFAOHWCB OPCIH HVS BSLH ZSGGCB JWGWH
        VHHD://QCRSG.AS/NNRTGS

## Session 2 - Code a Caesar cypher in Python

### Code Topics

-   Basic syntax using the Python shell
    -   Do some math calculations
    -   Operators especially %
    -   Variables
    *   Length of strings: len()
-   Edit, Save and Run .py files
    -   For loops
        - range()
    -   If/Else
    -   Type a small programme to print out odd numbers between 0-10

``` {.python}
##############################
# Print odd numbers
##############################
for num in range(10):
    if num % 2 != 0:
        print num
```

* Using files for the code
    *   Save the file, calling it "odd.py"
    *   Run the programme:

    python odd.py

### Caesar cypher encrypt

Load the file encrypt.py and take a look at the code

``` {.python}
##############################
# Caesar Cypher - Encrypt
##############################

# Define the alphabet that we are going to encode
# Any other character in the message will be left unchanged
LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

# Define variables to hold our message, the key and the translated message
message = 'This is secret'
key = 4
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
        num = (num + key) % len(LETTERS)
# get the letter from the changed number
        translated = translated + LETTERS[num]
    else:
# the symbol is not in the alphabet so just add it unchanged
        translated = translated + symbol

# we have now been through every letter in the message so we can print the translated version
print(translated)
```

#### Questions

1.  What happens if you change the key?
2.  What happens if you encrypt the already encrypted message using a
    key equal to 26 - your original encryption key?
3.  Why does this happen?

### Caesar cyper decrypt

``` {.python}
##############################
# Caesar Cypher - Decrypt
##############################

# Define the alphabet that we are going to encode
# Any other character in the message will be left unchanged
LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

# Define variables to hold our message, the key and the translated message
message = 'XLMW MW WIGVIX'
key = 4
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
```

#### Advanced

* Put the decrypt code in a for loop to try every key on an encrypted message

## Session 3 - Brute Force Cracking

* How many keys are there?
* Is it feasible to try them all using the code wheel?
* Wouldn't the computer do it more quickly?

### Code Concepts

* Functions
* User input
* while loop (input checking)
* type errors
    - Checking for types

### caesar.py

```python

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
    # We are going to try all keys
    for key in range(len(LETTERS)):
        print str(key) + ": " + decrypt(key, message)
else:
    # We will need a key from the user
    key = int(raw_input("Please type a whole number for the key: "))
    if mode == 'd':
        print decrypt(key, message)
    else:
        print encrypt(key, message)
```

Have the code for crack with blanks for them to fill in...

#### Questions

* What happens if you try you enter something other than one of the specified
  mode letters?
* Take a look at the while loop that does this checking
* What happens if you don't put in a whole number for the key?

#### Advanced

* Use the type() function to check the key the user gives to make sure that it
  is an integer (whole number)
    * Hint type this into the Python shell: type(5) == int

## Session 4 - Substitution cypher

* increase the number of keys by shuffling them rather than shifting them.
* How many keys are there now? (26!) 

### Code concepts

* Libraries and  "import"
* math.factorial()
* Lists (a = list('abcdefghijklmnopqrstuvwxyz'))
* random.shuffle()
* Python objects and variables - variables are pointers to objects, so b = a
  does not create a copy, it just points to the same object (Different from
  simple variables) - Be careful as shuffling in place my not have the desired
  effect. Suggest use b = list(a) for simplicity (Don't want to really get into
  copy)

```python
>>> a = list('abcdefghijklmnopqrstuvwxyz')
>>> b = list(a)
>>> random.shuffle(b)
>>> b
['t', 'b', 'm', 'i', 'j', 'g', 's', 'c', 'r', 'p', 'k', 'd', 'n', 'f', 'w', 'e', 'l', 'a', 'q', 'u', 'v', 'y', 'x', 'o', 'z', 'h']
>>> a
['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
```


