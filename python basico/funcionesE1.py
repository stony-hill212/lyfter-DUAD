def count_charac(text,char):
    count=0
    text=text.lower()
    char=char.lower()
    for c in text:
        if c==char:
            count+=1
    return count
entered_text=input("Please enter a word/text: ")
entered_charac=input("Please enter a character: ")  
result=count_charac(entered_text,entered_charac)
print(f"The character appears {result} times.")       