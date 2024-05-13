# Complete the method/function so that it converts dash/underscore delimited words into camel casing. 
# The first word within the output should be capitalized only if the original word was capitalized 
# (known as Upper Camel Case, also often referred to as Pascal case). 
# The next words should be always capitalized.

# Examples
# "the-stealth-warrior" gets converted to "theStealthWarrior"
# "The_Stealth_Warrior" gets converted to "TheStealthWarrior"
# "lets_go_team" gets converted to "letsGoTeam"

def solution(string):
    output = ''
    capitalize = False
    for letter in string:
        if letter in {'-', '_', ' '}:
            capitalize = True
        elif capitalize:
            output += letter.upper()
            capitalize = False
        else:
            output += letter
    return output

import re
def solution(string):
    delimiter = re.compile('[-_ ][A-Za-z]')
    return delimiter.sub(lambda match: match.group()[-1].upper(), string)