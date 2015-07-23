# STEM_Python_Crypto

## Introduction

A short course for school children to become familiar with Python using codes
and cyphers as a vehicle.  I am writing this course as a Science Technology
Engineering and Maths (STEM) Ambassador, aiming to improve the take-up of these
subjects among school children.

The majority of the ideas come from [Invent with Python -
Hacking](https://inventwithpython.com/hacking/chapters/), but the course is
much reduced to fit into a term of 45 minute sessions

This is very much, "Work in Progress", and at the moment I am just capturing ideas and structure.

## Session 1 - Introduction to the Caesar cypher

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

## Session 2 - Introduction to Python

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
``````

## Session 3 - Code a Caesar cypher in Python

### Code Concepts

* Reinforcement of what was learned last week
* Algorithms
* Reading code
* Comments

### Actions

* Load encrypt.py
* Review the code - maybe get them to fill in some code blanks
* Run the code with your own message

### Questions

1.  What happens if you change the key?
2.  What happens if you encrypt the already encrypted message using a
    key equal to 26 - your original encryption key?
3.  Why does this happen?

### Advanced

* Change the code to create a "Decrypt" program - hint You only need to add
  one line of code...
* Save your modified program as "decrypt.py"
* Encrypt a message for a friend, give them the cyphertext and tell them the
  key and let them decrypt and read the message

## Session 4 - Modularizing the Caesar cypher

### Code Concepts

* Functions
* The "main" function
* User input
* Errors - unexpected types
* Casting to different types - int(), float(), str().

## Session 5 - Brute force attack

### Code Concepts

* Lists - Bit contrived, but store each decryption attempt in a list
* List.append()
* Iterators

### Actions

* How many different keys are there?

### Questions


### Advanced

## Session 6 - Detecting English

### Code Concepts

* Dictionary data structure

### Actions


### Questions


### Advanced

## Session 7 - Substitution Cyper

### Code Concepts

* Libraries and  "import"
* math.factorial()
* Lists (a = list('abcdefghijklmnopqrstuvwxyz'))
* random.shuffle()
* Python objects and variables - variables are pointers to objects, so b = a
  does not create a copy, it just points to the same object (Different from
  simple variables) - Be careful as shuffling in place my not have the desired
  effect. Suggest use b = list(a) for simplicity (Don't want to really get into
  copy)

### Actions

* Provide partial code - ask them to create the "decrypt" function

### Questions

* Take a look at the encrypted output, do you see any patterns?
* Anyone played "Codeword" puzzles?
* Introduce the dotted.decimal encoding for words as in [book](https://inventwithpython.com/hacking/chapter18.html)

### Advanced

* Write a function that converts a word into the dotted.decimal format
* Modify the dictionary programme to create a python dictionary
  containing dotted decimal versions of all of the words in the
  dictionary as the keys and a list of words as the values.
