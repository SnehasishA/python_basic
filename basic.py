"""use this option/pattern to pass anything as multiline string,
 this part will not be executed inside code"""

# use this # to comment out any line, this line will not be executed while running the code

#use print option to print any output
print("Hello World")

"""variable : are place holder for storing data
Rules for naming a variable : 1. Must start with letter (a-z & A-Z) or Underscore(_)
                              2. Shouldn't start with number (0-9 or any combination of 0-9)
                              3. It can contain alphanumaric characters & underscore(snehasish_95)
                              4. variabke name are case sensitive (snehasish Snehasish SNEHASISH all these are different)
                              5. Inbuilt keywords shouldn't be used as variable (help(keywords) to get inbuilt keywords)"""
x = 5
print(x)

"""data types in python
integers: numeric values without decimal value, can be negative value(-2, 9) also
floats: numeric values with decimal value, can be negative value(-1.2, 1.0, 3.9)
booleans: it's a data type to get answers in True or False format, for both first letter should be in Capital
strings: any value inside "" quotation , it can be alphabetic, numeric, alpha-numeric, special character
none: voide value or No value, should start with capital None
use type keyword to find the type of data"""
x = 5
print(type(x))
print(x)

y = 5.5
print(type(y))
print(y)

z = True
print(type(z))
print(z)

a = "snehasish @ 123 _ Sneha_12+95"
print(type(a))
print(a)

b = None
print(type(b))
print(b)

#print can be used to output multiple values separated with comma
print ("snehasish", "SNEHASISH_95", 1, 9.9, True)

"""operator in python : operator is a symbol to perform specific mathematical, relational or logical operations and produce
final result.
addition: (+)
subtraction: (-)
division: (/)
mod: (%) it will return remainder
multiplication: (*)
floor division: (//) it will return nearest smaller integer
to the power: (**)"""

a = 10
b = 6

print(a+b)
print(a-b)
print(a/b)
print(a*b)
print(a%b)
print(a//b)
print(a**b)

#string concatenation (only allows addition, multiplication(only with int))

c = "Snehasish"
d = " Adhikary"
print(c+d)

"""comparison Operators: are used to compair to values and the results are always in boolean
== True if equal
!= True if not equal
< less than & > grater than
<= less than or equal to >= grater than or equal to"""