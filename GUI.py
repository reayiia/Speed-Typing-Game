import tkinter as t, Typingclass, Stats, Userclass, threading

 #sentence reference from user clas, which gets sentence from server
data = Stats.Stats() 

user = Userclass.user(data)
user.askfornewsen() 
obtime = user.getsptimeobj()



project = t.Tk()

project.title("Wow such typing")
project.geometry(f"{project.winfo_screenwidth()}x{project.winfo_screenheight()}")

def keypressed(key):
    if(key.keycode != 40 and key.keycode != 39 and key.keycode != 38 and key.keycode != 37 and key.keycode!=8 and key.keycode!=13 and key.keycode!=16):
       cond = ty.typingans(key.char)
       
       print(ty.getcommonvals()[2])
       print(topoint(ty.getcommonvals()[2]))
       print(topoint(ty.getcommonvals()[2]+1))
       print( key.char)
       print("curr word", ty.getcommonvals()[1])
       print("words typed:", ty.getcommonvals()[3])
       print("4th:", ty.commonvals[4])
       print(data.wrong)
       
       if(cond == False):
           text.tag_add('wrong', topoint(ty.getcommonvals()[2]), addone(ty.getcommonvals()[2]+1))
           text.tag_config('wrong', foreground= 'red')
           if(ty.getcommonvals()[4] == True and data.wrong<=ty.getcommonvals()[3]):
               print("reached!")
               data.incwrong()
               ty.commonvals[4] = False
       else:
           text.tag_add('right', topoint(ty.getcommonvals()[2]-1), addone(ty.getcommonvals()[2]))
           text.tag_config('right', foreground= 'green')
    

def topoint(num): 
    concat = []

    concat.append("1")

    concat.append('.')

    concat.append(str(num))  
    
    return ''.join(concat)



def addone(num):
    if(num == 1.0):
        return 1.1
    else:
        if(num>1.0):
            return topoint(num)
        
def condcheck():
    print("checking...")
    while True:
        if(ty.commonvals[2] == len(sentence)-1):
            ty.obtime.setCond(False)
            print("Final time", ty.obtime.getTime()-ty.obtime.getTimes()[0])
            user.savegameinfo()
            user.forwardstats()
            loadscreen()
            
            while True:
                if(opstatfetch()[0][1]!= 0):
                    wait.destroy()
                    obtime.timegeneric(4)
                    displayresults()
                    break
                else:
                    obtime.timegeneric(5)
            #print("table:", self.obtime.table)
            
            break
        
def opstatfetch():
    temp = user.askforopstats().decode('utf-8')
    opcurr = [[0,0,0,0,0], [0,0,0,0,0]]
    if(temp != "N/A"):
        opcurr = user.liststcleanup(eval(temp))
        
    print(opcurr)
    return opcurr
        
def loadscreen():
    global wait
    wait = t.Toplevel()
    wait.title("Waiting for opponent...")
    wait.geometry("500x200")
    message = t.Label(wait, text= 'Waiting for opponent...')
    message.config(font=("Segoe UI", 12))
    message.pack()

def displayresults():
    global resultwin
    resultwin = t.Toplevel()
    resultwin.title("Final Results")
    resultwin.geometry("765x360")
    mystats = t.Label(resultwin, text= 'My Stats')
    mystats.config(font=("Segoe UI", 12))
    mystats.pack()
    accsec = t.Label(resultwin, text= f"Final Accuracy: {round(data.accuracy()*100, 1)}%")
    accsec.place(x=10, y=70)
    cwords = t.Label(resultwin, text= f"Total words correct: {data.getright()}")
    cwords.place(x=300, y=70)
    wwords = t.Label(resultwin, text= f"Total words incorrect: {data.wrong}")
    wwords.place(x=565, y=70)
    finalt = t.Label(resultwin, text= f"Total time: {obtime.Elapsed} seconds")
    finalt.place(x=10, y=145)
    wpmt = t.Label(resultwin, text= f"Words per minute: {round(data.wpmm(obtime.Elapsed),1)}")
    wpmt.place(x=300, y=145)
    
    oaccsec = t.Label(resultwin, text= f"Best final Accuracy: {user.bestselector()[0]}%")
    oaccsec.place(x=10, y=100)
    ocwords = t.Label(resultwin, text= f"Best total words correct: {user.bestselector()[1]}")
    ocwords.place(x=300, y=100)
    owwords = t.Label(resultwin, text= f"Best total words incorrect: {user.bestselector()[2]}")
    owwords.place(x=565, y=100)
    ofinalt = t.Label(resultwin, text= f"Best total time: {user.bestselector()[3]} seconds")
    ofinalt.place(x=10, y=175)
    owpmt = t.Label(resultwin, text= f"Best Words per minute: {user.bestselector()[4]}")
    owpmt.place(x=300, y=175)
    
    divider = t.Label(resultwin, text= "________________________________________________________________")
    divider.place(y=190)
    
    baccsec = t.Label(resultwin, text= f"Opponent Accuracy: {opstatfetch()[0][0]}%")
    baccsec.place(x=10, y=220)
    bcwords = t.Label(resultwin, text= f"Opponent total words correct: {opstatfetch()[0][1]}")
    bcwords.place(x=275, y=220)
    bwwords = t.Label(resultwin, text= f"Opponent total words incorrect: {opstatfetch()[0][2]}")
    bwwords.place(x=540, y=220)
    bfinalt = t.Label(resultwin, text= f"Opponent time: {opstatfetch()[0][3]} seconds")
    bfinalt.place(x=10, y=300)
    obwpmt = t.Label(resultwin, text= f"Opponent words per minute: {opstatfetch()[0][4]}")
    obwpmt.place(x=275, y=300)
    
    obaccsec = t.Label(resultwin, text= f"Opponent best Accuracy: {opstatfetch()[1][0]}%")
    obaccsec.place(x=10, y=250)
    obcwords = t.Label(resultwin, text= f"Opponent best total words correct: {opstatfetch()[1][1]}")
    obcwords.place(x=275, y=250)
    obwwords = t.Label(resultwin, text= f"Opponent best total words incorrect: {opstatfetch()[1][2]}")
    obwwords.place(x=540, y=250)
    obfinalt = t.Label(resultwin, text= f"Opponent best time: {opstatfetch()[1][3]} seconds")
    obfinalt.place(x=10, y=330)
    obwpmt = t.Label(resultwin, text= f"Opponent best words per minute: {opstatfetch()[1][4]}")
    obwpmt.place(x=275, y=330)
    
    restart = t.Button(resultwin, text= "Save and restart", command= lambda: saveandrestart(1)) 
    restart.pack()

def saveandrestart(exists):
    if(obtime.Elapsed>0):
        print("acknowledged")
        user.resetall()
    
    userin.delete(0, t.END)
    user.newgamenotice()
    user.askfornewsen()
    global sentence 
    sentence = user.sentence.decode('utf-8')
    data.setwc(sentence)
    global ty
    ty = Typingclass.Typing(sentence, user)
    ty.reset()
    text.delete('1.0', t.END)
    print(sentence)
    text.insert(t.END, sentence)
    project.update()
    
    threads()
    
    if(exists ==1):
        resultwin.destroy()

    
def movelabels():
    countertext.place(x=10, y=350)
    countertext.config(font=("Segoe UI", 12))
    
    wrongctext.place(x=1400, y=350)
    wrongctext.config(font=("Segoe UI", 12))
    
    averaget.place(x=1450, y=175)
    averaget.config(font=("Segoe UI", 12))
    
    project.update()
    
def timeandstattrack():
    while(obtime.getcond()==True):
        counter.config(text= obtime.Elapsed, font=("Segoe UI", 20))
        counter.place(relx=0.03, rely=0.5, anchor="center")
        
        wrongc.config(text= data.wrong, font=("Segoe UI", 20))
        wrongc.place(relx=0.967, rely=0.5, anchor="center")
        
        average.config(text= f"{round(data.accuracy()*100, 1)}%", font=("Segoe UI", 20))
        average.place(relx=0.967, rely=0.3, anchor="center")
        
        project.update()
        
def started(thr):
     print("started")
     while True:
         if(ty.commonvals[2]>0): 
            thr.start()
            break        


def threads():
    timethread = threading.Thread(target = ty.obtime.stopwatch)
    startthread = threading.Thread(target = started, args=(timethread,))
    condthread = threading.Thread(target = condcheck)
    updatethread = threading.Thread(target = timeandstattrack)

    startthread.start()
    updatethread.start()
    condthread.start()
    
    


text = t.Text(project, width = 100, height = 10)
text.place(relx=0.5, rely=0.10, anchor="center")
userin = t.Entry(project)
userin.pack(side=t.BOTTOM, fill=t.X)
userin.pack(ipady= 100)

#displayresults() #-------------------------------------------------




countertext = t.Label(project, text= 'Time Elapsed')
countertext.pack()

wrongctext = t.Label(project, text= 'Incorrect Words')
wrongctext.pack()

averaget = t.Label(project, text= 'Accuracy')
wrongctext.pack()
movelabels()

counter = t.Label(project, text= '0')
counter.pack()

wrongc = t.Label(project, text= '0')
wrongc.pack()

average = t.Label(project, text= '100%')
average.pack()

saveandrestart(0)


userin.bind("<Key>", keypressed)


project.mainloop()

print("Final time", obtime.getTime()-obtime.getTimes()[0])




