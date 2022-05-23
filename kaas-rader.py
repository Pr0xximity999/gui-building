from cProfile import label
from tkinter import *
import tkinter

window = tkinter.Tk()
window.geometry('300x400')
window.columnconfigure(1, weight=3)
window.resizable(0,0)
awnsers = {}
rbs = {}
lbls = {}

def calcAwnser(questionName, arg2, arg3): #The function to handle the yes or no input
    global stringV, awnsers
    awnser = awnsers[questionName].get()

    print(awnser)

    #The first question
    if questionName == 'isKaasGeel':
        if awnser == 'ja': 
            mkQuestion('Zitten er gaten in?', 'heeftKaasGaten', 1)
        else:
            mkQuestion('Heeft de kaas blauwe schimmels?', 'heeftKaasSchimmel', 1)
    

    #The second questions
    if questionName == 'heeftKaasGaten':
        if awnser == 'ja':
            mkQuestion('Is de kaas belachelijk duur?', 'isKaasDuur', 2)
        else:
            mkQuestion('Is de kaas zo hard als een steen', 'isKaasSteen', 2)
    
    if questionName == 'heeftKaasSchimmel':
        if awnser == 'ja':
            mkQuestion('Heeft de kaas een korst?', 'heeftKaasKorstSchimmel', 2)
        else:
            mkQuestion('Heeft de kaas een korst?', 'heeftKaasKorst', 2)
    

    #The third questions
    


def mkQuestion(question:str, questionName:str, row:int):#A function to make a yes or no question
    global stringV, awnsers

    #Checks if there isn't already something on that row
    if row in lbls.keys():
        for i in range(row, len(lbls.values())):
            lbls[i].destroy()
            rbs[f'1 {i}'].destroy()
            rbs[f'2 {i}'].destroy()

    stringV = StringVar(name=questionName)
    stringV.trace('w', calcAwnser)
    awnsers.update({questionName: stringV})

    questionLbl = Label(window, text=question)
    questionLbl.grid(column=0, row=row, sticky=W)
    lbls.update({row : questionLbl})
    
    rb = Radiobutton(window, text='Ja', value='ja', variable=stringV, tristatevalue='x')
    rb.grid(column=1, row=row, sticky=E)
    rbs.update({f'1 {row}' : rb})

    rb = Radiobutton(window, text='Nee', value='nee', variable=stringV, tristatevalue='x')
    rb.grid(column=2, row=row, sticky=E)
    rbs.update({f'2 {row}' : rb})

#The startQuestion
mkQuestion('Is de kaas geel?', 'isKaasGeel', 0)


window.mainloop()