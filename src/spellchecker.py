from tkinter import *  # gui
from tkinter import Label

from textblob import TextBlob  # for processing textual data
from tkmacosx import Button  # Mac only - button background to work


# Sets up main window
def create_window():
    root = Tk()
    root.title('Spell Checker')
    root.geometry('600x300')
    root.config(background='#FFCCE5')
    return root


# GUI elements
def labels_buttons(root):
    # Spelling Checker header label
    heading = Label(root, text='Spelling Checker', font=('Arial', 20, 'bold'), bg='#FFCCE5', fg='#460C68')
    heading.pack(pady=(50, 0))  # puts space between widgets (pad y, pad x)

    enter_text = Entry(root, justify='center', width=30, font=('Arial', 20, 'bold'), bg='white', border=2)
    enter_text.pack(pady=10)
    enter_text.focus()

    # Correct spelling label
    cs = Label(root, text='Correct spelling is : ', font=('Arial', 20), bg='#FFCCE5', fg='#460C68')
    cs.place(x=100, y=200)

    # Spell label
    spell = Label(root, font=('Arial', 20), bg='#FFCCE5', fg='#460C68')
    spell.place(x=300, y=200)

    # Check spelling button
    # lambda used to ensure the function is only called when the button is clicked and not when the button is created.
    check_button = Button(root, text='Check spelling', font=('Arial', 20, 'bold'), bg='white', fg='#758ED9',
                          highlightbackground='#758ED9', command=lambda: check_spelling(enter_text, spell))
    check_button.pack()


# Checks for correct spelling of word
def check_spelling(enter_text, spell):
    word = enter_text.get()
    corrected_word = str(TextBlob(word).correct())  # returns correct spelling

    # Updates text label with the correct spelling
    spell.config(text=corrected_word)


def run():
    root = create_window()
    labels_buttons(root)
    root.mainloop()  # starts event loop to run application


run()
