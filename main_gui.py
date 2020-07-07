import random
import string
from tkinter import *

def generate():
    length = length_textbox.get()
    if length.isdigit():
        l = int(length)
        digits_count = 0
        u_letters_count = 0
        l_letters_count = 0
        punct_count = 0
        while True: # at least one symbol of each set(Uppercase letters, lowercase letters, numbers and punctuation)
            password=[]
            for i in range(l):
                password.append(random.choice(string.ascii_letters+string.digits+string.punctuation))
                if password[i] in string.ascii_lowercase:
                    l_letters_count+=1
                elif password[i] in string.ascii_uppercase:
                    u_letters_count+=1
                elif password[i] in string.digits:
                    digits_count+=1
                elif password[i] in string.punctuation:
                    punct_count+=1
            if (digits_count!=0) and (u_letters_count!=0) and (l_letters_count!=0) and (punct_count!=0):
                break
        pass_label.configure(text=''.join(password))

window = Tk()
window.title("Password generator")
window.geometry('320x100')
window.resizable(0, 0)
length_label = Label(window, text="Input password length:", font=("Calibri", 11))
length_label.grid(column=0, row=0, sticky=W)
length_textbox = Entry(window,width=10)
length_textbox.grid(column=0, row=1, sticky=W)
btn = Button(window, text="Generate", font=("Calibri", 11), command=generate)
btn.grid(column=0, row=2, sticky=W)
pass_label = Label(window, text='', font=("Calibri Bold", 11))
pass_label.grid(column=0,row=3, sticky=W)
window.mainloop()