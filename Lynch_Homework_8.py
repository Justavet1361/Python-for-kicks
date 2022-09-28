# Designed by Tamara Lynch: Week 6 In Class Assignment #2 26 September 2022.
# 
# Create a Python program called "Character Analyzer" 
# 
print('------------------ Character Analyzer--------------------\n')

user_input1 = (input('\nPlease enter any character to analyze: '))

# print the ASCII number in decimal and hexadecimal.

print('\nThe character you entered: '+ ascii(user_input1) + ' has the ACSII decimal value of: ', ord(user_input1))
print('\nIt has a hexadecimal value of: ', hex(ord(user_input1)))

# convert to an integer for analysis
user_input = int(ord(user_input1))

# Give the opposite version (Lower/upper) of the character if it is a letter.
# Indicate if it is a vowel.

if user_input == 32:
    print('This is a space character:_')
elif 33 <= user_input <= 47\
    or 58 <= user_input <=64\
    or 91 <= user_input <= 96\
    or 123<= user_input <= 126: 
    print('\nThis is a special character: ', chr(user_input))
elif user_input >= 65 and user_input <= 90:
    print('\nThis is an upper case character and here is the lower case value: ', chr(user_input).lower())
    if user_input == 101 or 105 or 111 or 117 or 125:
        print('\nThis is an upper case vowel')
    else:
        print('\nThis is not an uppercase vowel')
elif user_input >= 97 and user_input <= 122:
    print('\nThis is a lower case character and here is the upper case value: ', chr(user_input).upper())
    if user_input == 141 or 145 or 151 or 157 or 165:
       print('\nThis is a lower case vowel')
    else:
        print('T\nhis is not a lower case vowel')

user_input2 = int(input('\nYou may now enter an ASCII integer (0-126) for further analysis: '))

if user_input2 < 0 or user_input2 >126:
    print('\nThis is not a valid ASCII number!')

# Analyze a character's decimal indicator
# Indicate if it is a control character and give a friendly message that it cannot be printed.

if 0 < user_input2 <= 31:
    print('\nThis is an unprintable control character, used to control peripherals.')
elif user_input2 == 32:
    print('\nThis is a space character:_')
elif 33<= user_input2 <= 47\
    or 58 <= user_input2 <=64\
    or 91 <= user_input2 <= 96\
    or 123<= user_input2 <= 126: 
    print('\nThis is a special character: ', chr(user_input2))
elif chr(user_input2) >='0' and chr(user_input2) <= '9':
    print('\nIt worked!!:' , user_input2)
elif user_input >= 65 and user_input <= 90:
    print('\nThis is an upper case character and here is the lower case value: ', chr(user_input2).lower())
    if user_input == 101 or 105 or 111 or 117 or 125:
        print('\nThis is an upper case vowel')
    else:
        print('\nThis is not an uppercase vowel')
elif user_input >= 97 and user_input <= 122:
    print('\nThis is a lower case character and here is the upper case value: ', chr(user_input2).upper())
    if user_input == 141 or 145 or 151 or 157 or 165:
       print('\nThis is a lower case vowel')
    else:
        print('T\nhis is not a lower case vowel')
else:
    print('\nThis integer is Not in the ASCII table!!')

print('\n\nThank you for using the Character Analyzer')

print('==============================================================/n')