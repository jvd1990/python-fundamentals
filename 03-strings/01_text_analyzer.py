text = input("Enter a sentence: ")

word_count = len(text.split())
total_characters = len(text)
english_letters = sum(character.isalpha() and character.isascii() for character in text)

print("Number of words:", word_count)
print("Total characters:", total_characters)
print("English letters:", english_letters)