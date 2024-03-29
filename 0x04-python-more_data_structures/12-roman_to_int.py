#!/usr/bin/python3
def roman_to_int(roman_string):
    """function that converts a Roman numeral to an integer."""
    if not roman_string or not isinstance(roman_string, str):
        return 0

    roman_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50,
                  'C': 100, 'D': 500, 'M': 1000}
    
    result = 0
    prev_value = 0
    
    for char in roman_string[::-1]:  # Start from the end of the string
        value = roman_dict.get(char, 0)
        
        if value < prev_value:
            result -= value
        else:
            result += value
        
        prev_value = value
    
    return result
