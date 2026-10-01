dictionary = {
    "book": ["a written work", "to reserve"],
    "light": ["illumination", "not heavy"],
    "bank": ["a financial institution", "the side of a river"]
}

word = input("Enter a word to search: ").lower()

meanings = dictionary.get(word, ["Word not found."])

print("Meanings:", meanings)