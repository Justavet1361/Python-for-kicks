# Script:  A series of statements

# Statement:  a unit of code that the Python interpreter can execute.  They represent an action or command (e.g. print statement,
#   assignment statements)
#   Statement elements include data types (constants and variables), reserved words, operators, functions, and objects

# Expression:  a type of statement, or part of a statement, that evaluates and produces a return


# reserved words:  and (a logical operator), as (to create an alias), assert (for debugging), break (to break out of a loop), class (to define a class)
#   continue (to continue to the next iteration of a loop), def (to define a function), del (to delete an object), else (used in conditional statements)
#   elif (used in conditiona statements, same as else if), except (usedd with exceptions, what to do when an exception occurs), 
#   False ( Boolean value, result of comparrison operations), finally (used with exceptions, what to do when an exception occures)
#   from (to import specific parts of a module), for (to create a loop), global (to declare a global variable), if (to make a conditional statement)
#   import (to import a module), in (to check if a value is present in a list, tuple, etc.), is (to test if two variables are equal)
#   lambda (to create an anonymous function), not (a logical operator), nonlocal (to declare a non-local variable), None (represents the null value)
#   or (a logical operator), pass (a null statement, a statement that will do nothing), raise (to raise an exception) return (to exit a funtion and return a value)
#   True (boolean value, result of comparison operations), try (to make a try...except statemtn), while (to create a while loop) with (use to simplify exception handling)
#   yield (to end a function, returns a generator)

# to get a list of keywords
import keyword
keyword.kwlist()
help('keywords')

# Constants:  
#   A "literal" meaning written into the pyton code.  
#   Or a "special" variable assigned at the beginning of the program.  Use all capital letters for variables that will be used as
#       a constant in the program


NUMBER_5 = 5  # is an example of assigning a constant

#  Comments:  begin with a hashtag, by convention, start a new line after 72 characters.
#       They can be "in-line" putting # comment next to a statement - keep these minimal
 
# Variables:  Spots in memory allocated to store some data.  Produced using the assignment statement.
variable1 = 1  #  Think of the equal sign as an arrow pointing to the variable name.  1 is the data placed in that spot.
# everything to the right of the equal sign happens first, then it is stored in that spot.  Expressions on the right can contain the variable
# variables can be re-assigned later in the code, and the old value gets wiped out
variable1 = 2  # now the variable1 spot holds the number 2 instead of 1.  The unused value 2 is removed via "garbage collection" by the interpreter

# variable naming conventions:  Variable names can contain _underslashes, numbers, and letters
    # They are case sensitive and you cannot start with a number.
    # By convention, start with a lowercase letter, then camelcase or underscore
    # Menomic - use names that make sense to the users of the program (back end programmers keep it short to avoid stack overflow)
    # Recommended not to use the same word with different cases or to start with a capital letter
    # Note: The lower_case_with_underscores naming convention, also known as snake_case, 
    #   is commonly used in Python. It isn’t enforced, but it’s a widely adopted standard.
# Python now offers full Unicode support, so you can also use Unicode characters in your variable names like π.

# Operators:  The main types of operators are arithmetic, relational, assigment, logical, membership, identity, and bitwise
         # operators may do different things depending on the data type of the variables fed in. e.g. concatenate
#   Arithmetic operators include:  addition +, subtraction -, multiplication *, division /, exponentiation **, floor division //, and modulus %
#       These are done in PEMDAS order.
        # + concantenates two strings and does not add spaces
#   Relational operators include: >, <, =, >=, <=, or != (not equal)  These are evaluated as True or False
#   Assignment operators include:  =, +=, -+, /=, *=, %=, **=, //=, and the new Walrus operator :=
#   Logical operators include:  and, or, not (these are all reserved words).  They return the boolean True or False
#   Membership operators include: in, not in. They return the boolean True or False
#   Identity operators include:  is, not is.  They return the boolean True or False
#   Bitwise operators include: & (Binary AND), | (Binary OR), ^ (Binary XOR), ~ (Binary One's Comlement)
#   <<(Binary Left Shift), >> (Binary Right Shift)
#

# Data Types:  text, numeric, sequence, mapping, set, boolean, binary, none type.  The data type is set when you assign a value to the variable
    # Numberid data types:  integer aka int, float, complex
x = 5       # int
x = 20.5    # float
x = 1j      #complex
    # Sequence data types:  list, tuple, range
x = ["apple", "banana", "cherry"]   #list
x = ("apple", "banana", "cherry")   #tuple
x = range(6)                        # range
    # Mapping data type: dictionary aka dict
x = {"name" : "John", "age" : 36}   # dict
    # Set data types:  set, frozenset
x = {"apple", "banana", "cherry"}   # set
x = frozenset{"apple", "banana", "cherry"}  #frozenset
    # Boolean data type:  boolean aka bool
x = True                            # bool
    # Binary data types:  bytes, bytearray, memoryview
x = b"Hello"                        # bytes
x = bytearray(5)                    # bytearray
x = memoryview(bytes(5))            # memoryview
    # None data type:  NoneType
x = None                            # NoneType

type(variable1) # type() function to get back the data type
# Built in Types - the standard types in the interpreter accoring to python.org:  numerics, sequences, mappings, classes, instances, and exceptions
#       Truth value testing, Boolean Operations, Comparisons

# Built In Functions:  These are always available in the python interpreter and can be used
#   without needing an import statement.
#   Argument:  what is placed within the parantheses - differs for each type of function and most have default settings


'''
abs()           # returns the absolute value of a number
any()           # returns True if all items in an iterable object are true
all()           # returns True if any item in an iterable object is true
anext()         # 
aiter()
ascii()
byte()
bytearray()
bool()
breakpoint()
bin()
chr()
classmethod()
complex()
compile()
callable()
dict()
dir()
delattr()
divmod()
enumerator()
eval()
exec()
filter()
float()
format()        # formats a specified value
frozenset()
getattr()
globals()
hasattr()
hash()
help()
hex()
id()
input()
int()
isinstance()
issubclass()
iter()
len()
list()
locals()
map()
max()
memoryview()
min()
next()
object()
oct()
open()
ord()
pow()
print() # prints to the standard output device, typically the screen
property()
range()
repr()
reversed()
round()
set()
setattr()
slice()
sorted()
staticmethod()
str()
sum()
super()
tuple()
type()
vars()
zip()
'''

# Python String Methods: capitalize(), casefold(), center(), count(), encode(), endswith(), expandtabs(), find(), format(), format_map()
#       index(), isalnum(), isalpha(), isascii(), isdecimal(), isdigit(), isidentifier(), islower(), isnumeric(), isprintable(), isspace()
#       istitle(), isupper(), join(), ljust(), lower(), lstrip(), maketrans(), partition(), replace(), rfind(), rindex(), rjust(), rpartition()
#       rsplit(), rstrip(), split(), splitlines(), startswith(), strip(), swapcase(), title(), translate(), upper(), zfill().

# Python List/Array Methods:  append(), clear(), copy(), count(), extend(), index(), insert(), pop(), remove(), reverse(), sort()

# Python Dictionary Methods:  clear(), copy(), fromkeys(), get(), items(), keys(), pop(), popitem(), setdefault(), update(), values()

# Python Tuple Methods:  count(), index()

# Python Set Methods:  add(), clear(), copy(), difference(), difference_update(), discard(), intersection(), intersection_update(), isdisjoint()
#       issubset(), issuperset(), pop(), remove(), symmetric_difference(), symmetric_difference_update(), union(), update()

# Python File Methods:  close(), detach(), filno(), flush(), isatty(), read(), readable(), readline(), readlines(), seek(), seekable(), tell()
#       truncate(), writable(), whitelines()



# Python Random Module - used to make random numbers.  Methods:  seed(), getstate(), setstate(), getrandbits(), randrange(), randint(), choice(), choices()
#       shuffle(), sample(), random(), uniform(), triangular(), betavariate(), expovariate(), gammavariate(), gauss(), lognormvariate()
#       mormalvariate(),vonmisesvariate(), paretovariate(), weibullvariate()

# Python Requests Module - make a request to a web page and print the response.  Methods: del(), get(), head(), patch(), post(), put(), request()

# Python Statistics Module - built in module that you can use to calculate math statistics of numerical data.  Methods:   statistics.harmonic_mean()
#       statistics.mean(), statistics. median(), statistics.median_grouped(), statistics.median_high(), statistics.median_low(), statistics.mode()
#       statistics.pstdev(), statistics.stddev(), statistics.pvariance(), statistics.variance()

# Python Math Module - built in module used for mathmatical tasks.  Methods:  math.acos(), math.acosh(), math.asin(), math.asinh(), math.atan()
#       math.atanh(), math.cell(), math.comb(), math.copysign(), math.cos(), math.cosh(), math.degrees90, math.dist(), math.erf(), math.erfc()
#       math.exp(), math.expm1(), math.fabs(), math.factorial(), math.floor(), math.fmod(), math frexp(), math.fsum(), math.gamma(), math.gcd()
#       math.hypot(), math.isclose(), math.isfinite(), math.isinf(), math.isnan(), math.isqrt(), mth.ldxp(), math.lgamma(), math.log(), math.log10()
#       math.log1p(), math.log2(), math.perm(), math.pow(), math.prod(), math.radians(), math.remainder(), math.sin(), math.sinh() math.sqrt(), math.tan(), math.tanh()
#       math.trunc()
#       
#       Math Constants:  math.e (euler's number 2.7182...),  math.inf (returns a floating-point positive infinity), math.nan (returns a floating point NaN not a number value)
#                       math.pi (returns pi 3.1415...), math.tau (returns tau 6.2831...)

# Python cMath Module - built in module for working with complex numbers. Methods:  cmath.acos(x), cmath.acosh(x), cmath.asin(x), cmath.asinh(x), cmath.atan(x)
#       cmath.atanh(x), cmath.cos(x), cmath.cosh(x), cmath.exp(x), cmath.isclose(x), cmath.isfinite(x), cmath.isinf(x), cmath.isnan(x), cmath.log(x[base]), cmath.log10(x)
#       cmath.phase(), cmath.polar(), cmath.rect(), cmath.sin(x),cmath.sinh(), cmath.sqrt(x), cmath.tan(x), cmath.tanh(x)
#       math.trunc()
#
#       cMath Constants:  cmath.e (euler's number 2.7182...),  cmath.inf (returns a floating-point positive infinity), cmath.infj (returns a complex infinity value)
#           cmath.nan (returns a floating point NaN not a number value), cmath.nanj(returns a comlex NaN value), cmath.pi (returns pi 3.1415...), cmath.tau (returns tau 6.2831...)


# Exceptions:  
#   ArithmeticError (raised when an error occurs in mumeric calculation)
#   AssertionError (raised when an assert statement fails)
#   AttributeError (raised when attribute refernce or assignment fails)
#   Exception (base class for all exceptions)
#   EOFError (raised when the input() method hits an "end of filer" condition (EOF))
#   FloatingPointError (raised when a floating point calculation fails)
#   GeneratorExit (raised when a generator is closed (with the close() method)
#   ImportError (raised when an imported module does not exist)
#   IndentationError (raised when indentation is not correct)
#   IndexError (raised when an index of a swquence does not exist)
#   KeyError (raised when a key does not exist in a dictionary)
#   KeyboardInterrupt (raised when the user presses Ctrl+c, Crtrl+z, or Delete)
#   LookupError (raised when errors raised cannot be found)
#   MemoryError (raised when a program runs out of memory)
#   NameError (raised when a variable does not exist)
#   NotImplementedError (raised when an abstract method requires an inherited class to overide this method)
#   OSError (raised when a sysrtem related operation causes an error)
#   OverflowError (raised when the result of a numeric calculation is too large)
#   ReferenceError (raised when a weak reference object does not exist)
#   RuntimeError (raised when an error occurs that do not belong to any specific exceptions)
#   StopIteration   (raised when the next() method of an iterator has no further values)
#   SyntaxError (raised when a syntax error occurs)
#   TabError (raised when indentation consists of tabs or spaces)
#   SystemError (raised when the sys.exit() function is called)   
#   TypeError (raised whn two different types are combined)
#   UnboundLocalError (raised when a local variable is referenced before assignment)
#   UnicodeError (raised when a unicode problem occurs)
#   UnicodeEncodeError (raised when a unicode encoding problem occurs)
#   UnicodeDecodeError (raised when a unicode decoding problem occurs)  
#   UnicodeTranslateError (raised when a unicode translation problem occurs)
#   ValueError (raised when there is a wrong value in a specified data type)
#   ZeroDivisionError (raised when the second operator in a division is zero)

# References:
#
# Amos, D., Bader, D., Jablonski, J., Heisler, F. (2022). Python Basics:  A Practical Introduction to Python 3. (4th ed.).
#       USA: Real Python.  www.realpython.com.

# Gaddis, T. (2018). Starting out with Python (4th Ed) New York, NY: Pearson Educational.  pp 1-74
#
# Geeksforgeeks.com (2022, 16 Feb). Python Programming Language.
#   https://www.geeksforgeeks.org/python-programming-language/ 
#
# Myers, M. (2017).  A Smarter Way to Learn Python. Monee, IL: Mike Myers
#   Reference http://www.asmarterwaytolearn.com
#
# Ramos, L.P. (2021, 25 Jan). How to Use Python: Your First Steps. From RealPython.com
#   https://realpython.com/python-first-steps/
#
# Severance, C.R. (2009). Python for Everybody: Exploring Data Using Python 3. Creative Commons.  
#   Available for download at www.py4e.com.
#
# Tagliaferri, L. (2018).  How to Code in Python.  New York, NY: Digital Ocean.  
#   download:  https://assets.digitalocean.com/books/python/how-to-code-in-python.pdf
#
# w3schools.com (2022, 16 June). Python Tutorial. https://www.w3schools.com/python/default.asp
