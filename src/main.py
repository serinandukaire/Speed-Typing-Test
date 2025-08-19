## Play Against Family and Friends
## Word Imported from words.py
## Run Module to Play

from tkinter import *
from timeit import default_timer as timer
import random
from words import word_list


window = Tk()
window.geometry("450x200")

x = 0

def game():
    global x
    if x == 0:
        global window
        window.destroy()
        x = x+1
    
    def check_result():
        if entry.get() == word_list[word]:
            end = timer()
            p1 = Label(window,text = (end - start),font = "times 20")
            p1.place(x = 175,y = 130)
        else:
            p1 = Label(window,text = "wrong spelling",font = "times 20")
            p1.place(x = 175,y = 130)

    word = random.randint(0,(len(word_list)-1))
    start = timer()
    window = Tk()
    window.geometry("500x200")
    
    x2 = Label(window,text = word_list[word].upper(),font = "times 20")
    x2.place(x = 150,y = 10)
    
    x3 = Label(window,text = "Let's see how fast you can write:",font = "times 20")
    x3.place(x = 10,y = 50)
    
    entry = Entry(window)
    entry.place(x = 370,y = 60)
    
    b2 = Button(window,text = "SUBMIT", command = check_result,width = 12, bg = 'gray')
    b2.place(x = 150,y = 100)
    b3 = Button(window,text = "TRY AGAIN?", command = game,width = 12, bg = 'gray')
    b3.place(x = 250,y = 100)

    window.mainloop()


x1 = Label(window,text = "Click 'GO' to take a speed typing test ... ",font = "times 20")
x1.place(x=10,y=50)

b1 = Button(window,text = "GO", command = game,width = 12, bg = 'gray')
b1.place(x = 150,y = 100)

window.mainloop()
