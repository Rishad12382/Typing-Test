words =['people','thing','time','day','man','woman','child','verbs','english','be','have','do','say','go','get','make','know','see','come','look','want','use','as','and','but','nut','or','many','why','how','whom','her','door','tv','mobile','laptop']



def time():
    global timeleft,score,miss
    if(timeleft >= 11):
        pass
    else:
        timeLabelCount.configure(fg='white')
    if(timeleft>0):
        timeleft -=1
        timeLabelCount.configure(text=timeleft)
        timeLabelCount.after(1000,time)
    else:
        gameplayDetailLabel.configure(text='Score = {} | mistake = {} | Total Score = {}'.format(score,miss,score-miss))
        rr = messagebox.askretrycancel('Notification','for play again hit retry button')
        if (rr == True):
            score = 0
            timeleft = 60
            miss = 0
            timeLabelCount.configure(text=timeleft)
            wordLabel.configure(text=words[0])
            scoreLabelCount.configure(text=score)
def startgame(event):
    global score,miss
    if(timeleft == 60):
        time()
    gameplayDetailLabel.configure(text='')
    if(wordEntry.get() == wordLabel['text']):
        score += 1
        scoreLabelCount.configure(text=score)
        print("Score ",score)
    else:
        miss += 1

    random.shuffle(words)
    wordLabel.configure(text=words[0])
    wordEntry.delete(0,END)

from tkinter import *
from tkinter import Label
import random
from tkinter import messagebox


root = Tk()
root.geometry('600x600+400+100')
root.configure(bg='black')
root.title('Typing Speed Test')

score = 0
timeleft = 60
count = 0
sliderwords = ''
miss = 0


fontLabel = Label(root, text='Welcome "Test Your Speed Here"', font=('inherit', 26, 'italic bold'),
                  bg='black', fg='gold',)
fontLabel.place(x=10, y=10)


random.shuffle(words)
wordLabel = Label(root, text=words[0], font=('inherit', 35, 'italic bold'), bg='black', fg='gold')
wordLabel.place(x=225, y=210)
scoreLabel = Label(root, text='Your Score :', font=('inherit', 20, 'italic bold'), bg='black', fg='gold')
scoreLabel.place(x=18, y=80)

scoreLabelCount = Label(root, text=score, font=('inherit', 20, 'italic bold'), bg='black', fg='gold')
scoreLabelCount.place(x=80, y=130)

timerLabel = Label(root, text='TimeLeft :', font=('inherit', 20, 'italic bold'), bg='black', fg='gold')
timerLabel.place(x=400, y=80)
timeLabelCount = Label(root, text=timeleft, font=('inherit', 20, 'italic bold'), bg='black', fg='gold')
timeLabelCount.place(x=450, y=130)

gameplayDetailLabel = Label(root,text='Type word and press enter button',font=('inherit', 20, 'italic bold'), bg='black', fg='gold')
gameplayDetailLabel.place(x=80,y=400)
wordEntry = Entry(root, font=('inherit', 25, 'italic bold'), bd=5, justify='center')
wordEntry.place(x=115, y=300)
wordEntry.focus_set()

root.bind('<Return>',startgame)

root.mainloop()
