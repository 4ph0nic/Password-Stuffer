import random

def generate_variations(text):
    variations = []
    # Make all characters uppercase
    variations.append(text.upper())
    # Make all characters lowercase
    variations.append(text.lower())
    # Capitalize the first letter of each word
    variations.append(text.title())
    # Reverse the text
    variations.append(text[::-1])
    # Shuffle the characters randomly
    temp = list(text)
    random.shuffle(temp)
    variations.append("".join(temp))
    # Remove vowels
    temp = text
    for vowel in ['a', 'e', 'i', 'o', 'u']:
        temp = temp.replace(vowel, '')
    variations.append(temp)
    # Add numbers
    variations.append(text + "0")
    variations.append(text + "1")
    variations.append(text + "2")
    variations.append(text + "3")
    variations.append(text + "4")
    variations.append(text + "5")
    variations.append(text + "6")
    variations.append(text + "7")
    variations.append(text + "8")
    variations.append(text + "9")
    return variations

text = input("Enter password: ")
print("Variations: ", generate_variations(text))

