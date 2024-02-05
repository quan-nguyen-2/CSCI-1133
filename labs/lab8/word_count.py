def word_count(filename):
    f = open(filename, "r")
    r = f.read().split()
    y = len(r)
    return y

print(word_count("song.txt"))
    
