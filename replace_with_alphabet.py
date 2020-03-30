"""This method replaces letters in text with position in alphabet"""

def alphabet_position(text):
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    text = list(text)
    result = []
    for letter in text:
        if letter.isalpha():
            result.append(str(alphabet.index(letter.lower())+1))
    return ' '.join(result)

print(alphabet_position("The sunset sets at twelve o' clock."))
