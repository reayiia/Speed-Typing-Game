import socket, Timerclass

class user:

    def __init__(self, stat): #objects crucial to data
        self.host = socket.gethostname() #change to ip of server
        self.port = 1234
        self.co = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.workobjstats = stat
        self.workobjtime = Timerclass.oTime(0)
        self.stats = []
        self.sentence = ' '
        self.ID = int.from_bytes(self.getID(), byteorder='big' , signed=False) 
    
    
    def openconnection(self):
        self.co = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.co.connect((self.host,self.port))
        
    def savegameinfo(self):
        self.stats.append([round(self.workobjstats.accuracy()*100,1), self.workobjstats.getright(), self.workobjstats.wrong, self.workobjtime.Elapsed, round(self.workobjstats.wpmm(self.workobjtime.Elapsed),1)])

#sending a 1 means new sentence, 2-2+52 means get opponent stats, 53 = requestforID, 54 newgamenotice
    def askfornewsen(self):
        self.openconnection()
        self.co.sendall(int.to_bytes(1, byteorder = 'big'))
        self.sentence = self.co.recv(2000)
        self.terminateconnection() #convert from bytes
        
    def getnsaves(self):
        return len(self.stats)
    
    def getID(self):
        self.openconnection()
        self.co.sendall(int.to_bytes(53, byteorder = 'big'))
        temp = self.co.recv(2000)
        self.terminateconnection()
        return temp
    
    def askforopstats(self):
        self.openconnection()
        self.co.sendall(int.to_bytes(2+self.ID, byteorder= 'big'))
        temp = self.co.recv(2000) 
        self.terminateconnection()    
        return temp      #[current stats, best stats]
        
    def terminateconnection(self):
        self.co.close()
        
    def resetall(self):
        self.workobjstats.reset()
        self.workobjtime.reset()
        
    def newgamenotice(self):
        self.openconnection()
        self.co.sendall(int.to_bytes(54, byteorder= 'big'))
        print("server returned:", self.co.recv(2000))
        self.terminateconnection()
        
    def liststcleanup(self, al):
        temp = al
        for l in temp:
            if(len(l)>5):
                l.pop(len(l)-1)
        return temp
    
    def bestselector(self):  #chooses best stats from pool of data
        hold = [0,0,10000,100000,0]
        self.stats = self.liststcleanup(self.stats)
        print("bestsele:", self.stats)
        for e in self.stats:
            for i in range(0, len(e)):
                if(i == 2 or i == 3):
                    if(e[i]<hold[i]):
                        hold[i] = e[i]
                else:
                    if(e[i]>hold[i]):
                        hold[i] = e[i]
        if(hold == [0,0,10000,10000,0]):
            return [0,0,0,0,0]
        print("bestsele:", hold)                
        return hold
    
    def forwardstats(self):
        temp = []
        if(len(self.stats)>0):
            self.stats = self.liststcleanup(self.stats)
            print("forwardst:", self.stats)
            temp.append(self.stats[len(self.stats)-1])
            temp.append(self.bestselector())
            self.openconnection()
            self.co.sendall(bytes(str(temp), 'utf-8'))
            print("server returned:", self.co.recv(2000))
            self.terminateconnection()
        
    def getsptimeobj(self):
        return self.workobjtime
        