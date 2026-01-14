def count_cases(text):
    upper=0
    lower=0
    for char in text:
        if char.isupper():
            upper+=1
        elif char.islower():
            lower+=1
    print(f"There's {upper} upper cases and {lower} lower cases.") 
entered_text=input("Enter a word/sentence: ")
count_cases(entered_text)