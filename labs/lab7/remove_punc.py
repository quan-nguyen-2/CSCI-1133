def remove_punc(text, punc):
    a_string = text
    for i in punc:
        a_string = a_string.replace(i, "")
    return a_string
print(remove_punc('Rem!ove, o?nly th3 exc!amati.n points!', '!'))
print(remove_punc('??Ge!t r;!;id of m,o,s,t punctuation','.!;,?'))
