import string

def alphabet_position(letter):
    return int(string.ascii_lowercase.index(str.lower(letter)))

def rotate_character(char, rot):
    if char.isalpha():
        pos = alphabet_position(char)
        if char.islower():
            return string.ascii_lowercase[(pos + rot) % 26]
        if char.isupper():
            return string.ascii_uppercase[(pos + rot) % 26]

def encrypt(text, rot):
    newtext = ""
    for char in text:
        if not char.isalpha():
            newtext += char
        else:
            newtext += str(rotate_character(char, int(rot)))
    return newtext
