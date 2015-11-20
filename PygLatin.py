# Pig Latin Converter for Single Words.

word = input("\nPlease input a word: ")
completedWord = ""

# Check whether the entered word is over 0 characters and that it is only alphabetic characters.
if len(word) > 0 and word.isalpha():

    print("\n** Valid input **")

    # Set the word to all lower case.
    word = word.lower()

    firstTwoChars = word[0] + word[1]

    restOfWord = word[2:]

    completedWord = restOfWord + firstTwoChars + "ay"

# Print the PygLatin word.
print('\nTranslated word is: ', completedWord)