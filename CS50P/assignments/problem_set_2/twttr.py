# sentence = input("Input: ")

# if sentence in ("a", "e", "i", "o", "u"):
#     sentence.replace()


# def replace_sentence(sentence, replacements):
#     new_sentence = sentence
#     for old_value, new_value in replacements:
#         new_sentence = new_sentence.replace(old_value, new_value)
#     return new_sentence


sentence = input("Input: ")
for letter in sentence:
    if letter in ("a", "e", "i", "o", "u"):
        pass
    else:
        print(letter, end="")

# ways of storing the output sentence from chatGPT
"""
sentence = input("Input: ")
output = ""
for letter in sentence:
    if letter in ("a", "e", "i", "o", "u"):
        pass
    else:
        output += letter

print("Output:", output)
"""