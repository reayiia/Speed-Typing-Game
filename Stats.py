import GenerateStringclass
class Stats:

    def __init__(self):
        self.wc = 1
        self.wpm = 0
        self.wrong = 0
        
    def setwc(self, sen):  #will return sentence wordcount
        self.wc = GenerateStringclass.senWordCount(sen)
        
    def wpmm(self, ft): #words per minute calculator
        self.wpm = (self.wc*60)/ft
        return self.wpm
    
    def incwrong(self): #increments amount wrong
        self.wrong +=1
        
    def getright(self): #calculates amount of words right
        return self.wc-self.wrong
    
    def accuracy(self): #calculate accuracy
        return (self.wc-self.wrong)/self.wc

    def reset(self): #resets data
        self.wc = 1
        self.wpm = 0
        self.wrong = 0
        

