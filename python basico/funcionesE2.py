def words_min(words,min_length):
    return[word for word in words if len(word)>=min_length]
my_list=["sunshine","moon","sun","air","space","fire","dumbbells","barbells","cables","kettlebells"]
min_letters=int(input("Enter the minimum amount of letters: "))
result=words_min(my_list,min_letters)
print(result)