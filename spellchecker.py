from tkinter import *  # gui
from textblob import TextBlob  # for processing textual data
from tkmacosx import Button  # Mac only - button background to work

root = Tk()
root.title('Spelling Checker')
root.geometry('750x400')
root.config(background='#91D8E4')


def check_spelling():
    word = enter_text.get()
    a = TextBlob(word)
    right = str(a.correct())  # correct spelling

    cs = Label(root, text='Correct spelling is : ', font=('Comic sans MS', 20), bg='#91D8E4', fg='#460C68')
    cs.place(x=100, y=250)
    spell.config(text=right)


heading = Label(root, text='Spelling Checker', font=('Arial', 20, 'bold'), bg='#91D8E4', fg='#460C68')
heading.pack(pady=(50, 0))  # puts space between widgets (pad y, pad x)
enter_text = Entry(root, justify='center', width=30, font=('Comic sans MS', 20, 'bold'), bg='white', border=2)
enter_text.pack(pady=10)
enter_text.focus()

Button = Button(root, text='Check spelling', font=('Arial', 20, 'bold'), bg='#758ED9', fg='white',
                highlightbackground='#758ED9', command=check_spelling)
Button.pack()

spell = Label(root, font=('Arial', 20), bg='#91D8E4', fg='#460C68')
spell.place(x=350, y=250)

root.mainloop()  # starts event loop to run application
