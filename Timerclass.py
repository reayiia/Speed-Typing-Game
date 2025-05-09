import time

class oTime:

    def __init__(self, Elapsed):
            self.Elapsed = 0
            self.proceed = True
            self.table = []

    
    def stopwatch(self):
        num = self.Elapsed
        if(self.proceed==True):
            self.Elapsed+=1
            print("time:", num)
            time.sleep(1)
            self.stopwatch()
        else:
            return num

        
    def getTime(self):
        return self.Elapsed
    
    def timegeneric(self, num):
        time.sleep(num)

    def getTimes(self):
        return self.table

    def setCond(self, cond):
        self.proceed = cond
        
    def lap(self):
        self.table.append(self.Elapsed)    
        
    def reset(self):            
        self.Elapsed = 0
        self.proceed = True
        self.table = []
        
    def getcond(self):
        return self.proceed
    

  