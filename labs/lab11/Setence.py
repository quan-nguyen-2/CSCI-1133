class Sentence:
    def __init__(self, string):
        self.string = string

    def getSentence(self):
        return self.string

    def getWords(self):
        return self.string.split()

    def getLength(self):
        return len(self.string)

    def NumWords(self):
        return len(split(self.string))

class SentenceV1:
    def __init__(self, string):
        self.string = string.split()

    def getSentence(self):
        return " ".join(self.string)

    def getWords(self):
        return self.string

    def getLength(self):
        count = 0
        for i in self.string:
            count += 1
        return count
        
    def getNumWords(self):
        return len(self.string)



#I thought the first method was just more simpler than the second one
#because I just had an easier time thinking about the different functions because
    # I felt like it was one last step
        
        


    
