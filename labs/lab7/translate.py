def piglatin(sentence):
    words = sentence.split()
    for i, word in enumerate(words):  
        if word[0] in 'aeiou':
            words[i] = words[i]+ "ay"
        else:

            has_vowel = False
        
            for j, letter in enumerate(word):
                if letter in 'aeiou':
                    words[i] = word[j:] + word[:j] + "ay"
                    has_vowel = True
                    break

            if(has_vowel == False):
                words[i] = words[i]+ "ay"

    pig_latin = ' '.join(words)
    return pig_latin.capitalize()
print(piglatin("Can you speak pig latin?"))

