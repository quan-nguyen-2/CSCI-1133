# <Quan Nguyen>
# <nguy4658@umn.edu>
# CSCI 1133 Section <070>
# encrypt

def encrypt(words):
    if not words == '':
        lower_words = words.lower()
        words = list(words)
        for i in range(len(lower_words)):
            if lower_words[i] == 'a':
                words[i] = '$'
            if lower_words[i] == 'e':
                words[i] = '&'
            if lower_words[i] == 'i':
                words[i] = '^'
            if lower_words[i] == 'o':
                words[i] = '*'
            if lower_words[i] == 'u':
                words[i] = '%'
        return ''.join(words)
    else:
        print('error in encryption, try again.')

print(encrypt("This message is a secret"))
print(encrypt(''))
print(encrypt("They will never decipher this"))
