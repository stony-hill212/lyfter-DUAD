my_list=[]
for i in range(5):
    word=input(f"Ingrese al palabra numero {i+1}: ")
    my_list.append(word)
long_words=[]
for word in my_list:
    if len(word)>4:
        long_words.append(word)
print(long_words)            