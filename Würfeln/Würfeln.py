from random import *
from tkinter import *
import time
Mut = 3
score = 0

def T1():
    global Mut
    global score
    GZ = randint(1,3)
    if GZ == 1:
        text.delete(0.0, END)
        text.insert(END, 'Score: '+str(score)+'\nGeist\n schnell weg!!')
        Mut=Mut-1
    elif GZ == 2 or GZ == 3:
        text.delete(0.0, END)
        text.insert(END, 'Score: '+str(score)+'\nGlück gehabt\n die Luft ist rein')
        Mut = Mut + 0.5
        score=score+1
    if Mut < 0:
        text.delete(0.0, END)
        text.insert(END, ('Score: '+str(score)+'\nDer Geist hat dich erwischt\n du hast so viele Türen geschaft:',score))
        window.update()
        time.sleep(3)
        window.quit()



def T2():
    global Mut
    global score
    GZ = randint(1,3)
    if GZ == 2:
        text.delete(0.0, END)
        text.insert(END, 'Score: '+str(score)+'\nGeist\n schnell weg!!')
        Mut = Mut -1
    elif GZ == 1 or GZ == 3:
        text.delete(0.0, END)
        text.insert(END, 'Score: '+str(score)+'\nGlück gehabt\n die Luft ist rein')
        Mut = Mut + 0.5
        score= score+1
    if Mut < 0:
        text.delete(0.0, END)
        text.insert(END, 'Score: '+str(score)+'\nDer Geist hat dich erwischt\n du hast so viele Türen geschaft:',score)
        window.update()
        time.sleep(3)
        window.quit()
def T3():
    global Mut
    global score
    GZ = randint(1,3)
    if GZ == 3:
        text.delete(0.0, END)
        text.insert(END, 'Score: '+str(score)+'\nGeist\n schnell weg!!')
        Mut = Mut -1
    elif GZ == 2 or GZ == 1:
        text.delete(0.0, END)
        text.insert(END, 'Score: '+str(score)+'\nGlück gehabt\n die Luft ist rein')
        Mut = Mut + 0.5
        score= score+1
    if Mut < 0:
        text.delete(0.0, END)
        text.insert(END, 'Score: '+str(score)+'\nDer Geist hat dich erwischt\n du hast so viele Türen geschaft:',score)
        window.update()
        time.sleep(3)
        window.quit()

window = Tk()
text = Text(window, height=3)
b1 = Button(window, text='1', command=T1)
b2 = Button(window, text='2', command=T2)
b3 = Button(window, text='3', command=T3)
text.pack()
text.insert(END, 'Geisterspiel \n Score: '+str(score)+'\n vor dir sind drei Türen \n hinter einer steht ein Geist')
window.update()
b1.pack()
b2.pack()
b3.pack()
mainloop()
