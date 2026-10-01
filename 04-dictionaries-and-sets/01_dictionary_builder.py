word = input("Enter a word: ")
meanings_text = input("Enter meanings separated by commas: ")

meanings = [meaning.strip() for meaning in meanings_text.split(",")]
dictionary = {word: meanings}

print("Dictionary:", dictionary)