def flip_string(text):
    return text[::-1]

if __name__ =="__main__":
    text_entered=input("Please enter a text/phrase: ")
    print(flip_string(text_entered))