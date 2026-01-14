def counting_vow(text):
    vowels="aeiou"
    return sum(1 for char in text.lower() if char in vowels)
text=input("Enter a text/word: ")
print(counting_vow(text))