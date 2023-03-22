'''
A function that converts roman numerals to arabic numbers
the function iterates the string backwards with an initial value set as 1
if it encounters a number greater than it, it adds its value from the dictionary
if it encounters a number less than, it means its a special case for 
4,9, and their suffixes
thus , it subtracts the velue of the smaller numeral
'''

def roman_to_arabic(string: str):
    roman = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }

    value = 0
    last = "I"

   

    for numeral in string[::-1]:
        if roman[numeral] < roman[last]:
            value -= roman[numeral]
        else:
            value += roman[numeral]
        last = numeral
    return value

