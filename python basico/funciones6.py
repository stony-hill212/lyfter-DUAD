def sort_dashed_str(text):
    words=text.split("-")
    words.sort(key=str.lower)
    return "-".join(words)


entered_text=input("Please enter a series of words separated by dashes: ")
print(sort_dashed_str(entered_text))