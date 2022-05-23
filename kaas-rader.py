from tkinter import *
import tkinter
from tkinter.messagebox import showwarning

window = tkinter.Tk()
window.geometry('300x200')
window.columnconfigure(1, weight=3)
window.resizable(0,0)
awnsers = {}
rbs = {}

#Resets the screen
def restart():
    for widget in window.winfo_children():
        widget.destroy()
    
    awnsers.clear()
    rbs.clear()

    restartBtn = Button(window, text='Restart', command=restart)
    restartBtn.place(relx=0.8, rely=0.8, relwidth=0.2, relheight=0.2)

    mkQuestion('Is de kaas geel?', 'isKaasGeel', 0)

def calcAwnser(questionName, arg2, arg3): #The function to handle the yes or no input
    global stringV, awnsers
    awnser = awnsers[questionName].get()
    rbs[questionName + '1'].configure(state='disabled')
    rbs[questionName + '2'].configure(state='disabled')

    awnserIsYes = awnser == 'ja'

    #The first question
    if questionName == 'isKaasGeel' and awnserIsYes: 
        mkQuestion('Zitten er gaten in?', 'heeftKaasGaten', 1)
    elif questionName == 'isKaasGeel':
        mkQuestion('Heeft de kaas blauwe schimmels?', 'heeftKaasSchimmel', 1)
    

    #The second questions
    if questionName == 'heeftKaasGaten' and awnserIsYes:
        mkQuestion('Is de kaas belachelijk duur?', 'isKaasDuur', 2)
    elif questionName == 'heeftKaasGaten':
        mkQuestion('Is de kaas zo hard als een steen', 'isKaasSteen', 2)
    
    if questionName == 'heeftKaasSchimmel' and awnserIsYes:
        mkQuestion('Heeft de kaas een korst?', 'heeftKaasKorstSchimmel', 2)
    elif questionName == 'heeftKaasSchimmel':
        mkQuestion('Heeft de kaas een korst?', 'heeftKaasKorst', 2)
    

    #The third questions
    if questionName == 'isKaasDuur' and awnserIsYes:
        showwarning('KAAS', 'De gekozen kaas is Emmenthaler')
    elif questionName == 'isKaasDuur':
        showwarning('KAAS', 'De gekozen kaas is Leerdammer')
    
    if questionName == 'isKaasSteen' and awnserIsYes:
        showwarning('KAAS', 'De gekozen kaas is\nParmigiano Reggiano')
    elif questionName == 'isKaasSteen':
        showwarning('KAAS', 'De gekozen kaas is Goudse Kaas')
    
    if questionName == 'heeftKaasKorstSchimmel' and awnserIsYes:
        showwarning('KAAS', 'De gekozen kaas is Bleu de Rochbaron')
    elif questionName == 'heeftKaasKorstSchimmel':
        showwarning('KAAS', "De gekozen kaas is Foumme d'Amert")
    
    if questionName == 'heeftKaasKorst' and awnserIsYes:
        showwarning('KAAS', 'De gekozen kaas is Camembert')
    elif questionName == 'heeftKaasKorst':
        showwarning('KAAS', 'De gekozen kaas is Mozzarella')
        



def mkQuestion(question:str, questionName:str, row:int):#A function to make a yes or no question
    global stringV, awnsers

    questionLbl = Label(window, text=question)
    questionLbl.grid(column=0, row=row, sticky=W)

    stringV = StringVar(name=questionName)
    stringV.trace('w', calcAwnser)
    
    awnsers.update({questionName: stringV})
    
    rb = Radiobutton(window, text='Ja', value='ja', variable=stringV, tristatevalue='x')
    rb.grid(column=1, row=row, sticky=E)
    rbs.update({questionName + '1' : rb})

    rb = Radiobutton(window, text='Nee', value='nee', variable=stringV, tristatevalue='x')
    rb.grid(column=2, row=row, sticky=E)
    rbs.update({questionName + '2'  : rb})


#The start
restart()

window.mainloop()