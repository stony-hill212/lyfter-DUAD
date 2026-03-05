def count_cases(text):
    upper=0
    lower=0
    for char in text:
        if char.isupper():
            upper+=1
        elif char.islower():
            lower+=1
    return upper,lower

def show_cases(text):
    upper,lower=count_cases(text)
    print(f"There's {upper} upper cases and {lower} lower cases.")

if __name__ =="__main__":
    entered_text=input("Enter a word/sentence: ")
    show_cases(entered_text)

