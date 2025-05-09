import Timerclass, threading, multiprocessing, GenerateStringclass, Userclass

class Typing:
    
    def __init__(self, sen, user):
        self.sentence = sen
        self.commonvals = [True, [], 0, 0, True] 
        self.obtime = user.getsptimeobj()
    
        
    def typingans(self, char): #Compares character passed in to character in string then iterates 
        pos = self.commonvals[2]            #position in string in time for next call.
        if(char == self.sentence[pos]):
            self.commonvals[2] = pos+1
            if(self.commonvals[3]<=GenerateStringclass.senWordCount(self.sentence)):
                if(self.wordcomplete(char)):
                    self.obtime.lap()
                    self.commonvals[4] = True
                    
            
            return True
        else:
            self.commonvals[0] = False
            print(self.commonvals[3])
            return False
        
    def getcommonvals(self): #getter function for commonvals
        return self.commonvals
    
    def wordcomplete(self, char): #tells if word is complete via checking if space and end character locations are hit
        locs = self.throwlocs()
        if(locs[self.commonvals[3]] == len(self.sentence)-1):
            num = locs[self.commonvals[3]]
        else:
            num = locs[self.commonvals[3]]-1
        
        for e in locs:
            if(self.commonvals[2] == e):
                print("compared to:" ,self.sentence[num])
                if(char ==  self.sentence[num]):
                    self.commonvals[3] += 1
                    return True
        return False
        
    def throwlocs(self):  
        var = GenerateStringclass.getSpaces(self.sentence)
        var.append(len(self.sentence)-1)
        return var
    
    def reset(self):
        self.commonvals = [True, [], 0, 0, True]
        
 #common vals format at point [boolean, list, last position, wordcount, Condition to limit 1 inc per word]
            
    
       
        