#convert decmal to hexadecimal (base 16)

def DecToHex(decimal_number):
    #define a dictionary to map decimal numbers with their hexadecimal equivalents

    hexadecimal_digits = {
        0:'0', 1:'1', 2:'2',  3:'3', 4:'4', 5:'5', 6:'6', 7:'7', 8:'8', 9:'9', 10:'a', 11:'b', 12:'c', 13:'d', 14:'e', 15:'f'
    }
    # Convert the decimal number to hexadecimal
    hexadecimal_string = ''
    while decimal_number > 0:
        remainder = decimal_number % 16
        hexadecimal_string = hexadecimal_digits[remainder] + hexadecimal_string
        decimal_number //= 16
    return hexadecimal_string
