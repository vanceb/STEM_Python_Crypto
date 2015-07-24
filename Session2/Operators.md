# Python Operators

## Mathematical Operators

-----------------------------------------------------------
Operator  Description                  Example
--------  ---------------------------  --------------------
`+`       Addition - Adds values on    `10 + 20 = 30`
          either side of the operator

`-`       Subtraction - subtracts the  `20 - 10 = 10`
          right hand value from the
          left hand value

`*`       Multiplication - multiplies  `5 * 5 = 25`
          values on either side of
          the operator

`/`       Division - divides the left  `4 / 2 = 2`
          hand value by the right
          hand value

`%`       Modulus - divides the left   `23 % 13 = 10`
          hand value by the right
          hand value and returns the
          remainder

`**`      Exponent - raises the left   `2 ** 3 = 8`
          hand value to the power of
          the right

`//`      Floor - divides the left     `3.0 // 2 = 1.0`
          hand value by the right
          hand value and returns
          the whole number only

-------------------------------------------------------------

Mathematical operators can be used on numbers or variables that contain numbers, or a mixture of the two.  If all numbers are integers (whole numbers) the result will be an integer - be aware of this for division.  If any of the numbers is a float (numbers with a decimal point), then the result will be a float.

## Comparison Operators

-----------------------------------------------------------
Operator  Description                  Example
--------  ---------------------------  --------------------
`==`      Equal - if the value of the  `a = 5` \
          left hand operator equals    `a == 5 -> true` \
          the value of the right hand  `a == 7 -> false` \
          operator then it returns
          `true`

`!=`      Not equal - if the left      `a = 7` \
          hand value is not equal to   `a != 7 -> false` \
          the right hand value then    `a != 8 -> true` \
          it returns `true`

`>`        Greater than - if the value  `a = 33` \
          on the left is larger than   `a > 25 -> true` \
          the value on the right then  `a > 50 -> false` \
          it returns `true`

`<`       Less than - if the value on  `a = 12` \
          the left is smaller than     ` a < 30 -> true ` \
          the value on the right then  ` a < 12 -> false ` \
          it returns `true`

`>=`      Greater than or equal to -   `a = 44` \
          if the value on the left is  `a >= 22 -> true` \
          equal to or larger than the  `a >= 50 -> false` \
          value on the right then this `a >= 44 -> true` \
          is true

`<=`      Less than or equal to -      `a = 75` \
          if the value on the left is  `a <= 122 -> true` \
          equal to or smaller than the `a <= 50 -> false` \
          value on the right then this `a <= 75 -> true` \
          is true

---------------------------------------------------------------

Comparison operators return `true` or `false` depending on then values being
compared. 

## Assignment Operators

-----------------------------------------------------------
Operator  Description                  Example
--------  ---------------------------  --------------------
`=`       Assigns the value of the     `a = 5 + 8` \
          right hand expression to     `a` now equals `13`
          the variable on the left

`+=`      Adds the value of the        `a = 4` \
          right hand expression to     `a += 5` \
          the value of the left hand   this is equivalent to \
          variable and assigns it      `a = a + 5` \
          to the variable on the left  so `a` is `9`

`-=`      Subtracts the value of the   `a = 7` \
          right hand expression from   `a -= 2 + 2` \
          the value of the left hand   this is equivalent to \
          variable and assigns it      `a = a - (2 + 2)` \
          to the variable on the left  so `a` now equals `3`

------------------------------------------------------------

All of the other operators listed in the [Mathematical Operators] section
can be put before the equals sign to follow this pattern.  If you find this
confusing you can always use the long-hand equivalent shown in the
examples.  The only one you really need here is the basic assignment, `=`

## Operator Precedence

Just as in basic maths we have to decide which operators are used first in
a complex expression.  Take the following example:

    2 + 2 * 5 = 12

not `20` because multiplication and division is done before addition
and subtraction. You can use brackets to make the order explicit:

    (2 + 2) * 5 = 20

Now the brackets ensure that the addition is done
before the multiplication.  Python has the same set of rules and you can use
brackets to make sure the order is clear.  However, Python has many more
operators than you use in normal maths and it therefore defines the
following order for the order of operators.

------------------------------------------------------------------
Operators         Description
----------------  ------------------------------------------------
`**`              Exponent (raise to the power)

`~ + -`           Complement and unary `+` and `-`, e.g. `a = -4`

`* / % //`        Multiply, divide, modulus, and floor

`+ -`             Addition and subtraction

`< <= >= >`       Comparison operators

`== !=`           Equality operators

`= += -= ...`     Assignment operators

`is` and `is not` Identity operators

`in` and `not in` Membership operators

`and not or`      Logical operators

-------------------------------------------------------------------

Some of these operators you haven't been introduced to yet, but they are
included for reference
