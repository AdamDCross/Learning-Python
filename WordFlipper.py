# Swaps the first letter of each word around.
#   - "Fuck Tom" would become "Tuck Fom".

word1 = input("\nPlease enter the first word: ")
word2 = input("\nPlease enter the second word: ")

completedWord = ""

# Check whether the entered word is over 0 characters and that it is only alphabetic characters.
if len(word1) > 0 and len(word2) > 0 and word1.isalpha() and word2.isalpha():

    print("\n** Valid input **")

    firstOneCharWord1 = word1[0]
    restOfWord1 = word1[1:]

    firstOneCharWord2 = word2[0]
    restOfWord2 = word2[1:]

    completedWord = firstOneCharWord2 + restOfWord1 + " " + firstOneCharWord1 + restOfWord2

# Print the PygLatin word.
print('\nFlipped m8: ', completedWord)