save_words = []

while True:
    word = input("Insert word: ")
    if word == '':
        break
    else:
        new_word = word.lower()
        word_without_first = new_word[1:len(new_word)]
        if new_word[0] in word_without_first:
            save_words.append(word)
for i in range(len(save_words)):
    print(save_words[i])
                    
