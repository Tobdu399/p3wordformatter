def format_word(word):
    formatted_word = []
    completed_word = ""

    for letter in word:
        formatted_word.append(letter)

    formatted_word[0] = formatted_word[0].upper()
    completed_word += formatted_word[0]             # Add the capitalized letter

    for i in range(1, len(formatted_word)):
        formatted_word[i] = formatted_word[i].lower()
        completed_word += formatted_word[i]         # Add rest of the letters in lowercase

    return print(completed_word)                    # Return the formatted word

