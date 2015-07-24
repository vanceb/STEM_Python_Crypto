# Session 2 - Introduction to Python

## The Python Shell

In the Python shell you can type python code and see the results.  This is a
really good place to see what happens if you are not sure.

Open the Python shell, and see if you can get Python to tell you the answers to
the following questions, write your answers after the question on this
worksheet.  

### Simple maths

Let's start simple...

    2 + 2

    333333 - 3465

    195 / 15

    27 / 9 * 63

    2 ** 3

### Integer arithmetic

When using integers (whole numbers), you should be aware of how Python will
deal with them when you do maths.  Try the following and see if you understand
the answers Python gives you

    11 / 3

What is the answer Python gives?

Does it seem right to you, and if not do you understand how Python gets this
answer? (Hint - try some other divisions to see if you can work it out)

If you haven't got it yet, maybe this will help.  The modulus (%) operator
gives you the remainder of the division.  

    11 % 3

Does that now help you understand the division? (11/3 = 3 remainder 2)

### Floating point arithmetic

If you want to calculate with decimal numbers (floats), then one of the numbers
in your calculation must be a float

    11.0 / 3

    11 / 3.0


### Variables

So, Python can do maths for you!  Let's now use some variables

    # Variables assigned with integers
    a = 7
    b = 11
    c = a * b

    print (c)

    # Variables asigned with a mixture of an integer and a float
    a = 11
    b = 3.0
    c = a / b

    print (c)

### Strings

Variables can be used to hold text (strings) too.  Remember strings are a
number of characters surrounded by either single quotes `'` or double quotes
`"`.

    greeting = 'Hello '
    name = "John"
    print (greeting + name + '!')

You can get the length of the string using the `len()` function

    len(name)

    len("This is a long sentence I bet you don't to count the characters")

What do you think is going to happen here?

    'Hello ' * 3

## Writing programs, saving them and running them

Open a new file window by selecting `File->New File`

Type in the following simple programme which prints out the odd numbers between
1 and 10.

``` python
for number in range(10):
    if number % 2 != 0:
        print (number)
```

Save the file by selecting `File->Save` and call it `odd.py`, then run the
program by pressing the `F5` key.

Try to change the program so that it prints the even numbers instead. 
