#!/usr/bin/python3

def remove_char_at(input_str, n):
    if n < 0 or n >= len(input_str):
        return input_str  
    result_str = ""
    for i in range(len(input_str)):
        if i != n:
            result_str += input_str[i]  # Append non-skipped characters
                                                                                
    return result_str  
            
