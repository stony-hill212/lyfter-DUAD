def sort_dashed_str(text):
    if not isinstance(text,str):
        raise TypeError("Input must be a string")
    
    words=text.split("-")
    words.sort(key=str.lower)
    return "-".join(words)

if __name__=="__main__":
    entered_text=input("Please enter a series of word separated by dashes: ")
    print(sort_dashed_str(entered_text))

