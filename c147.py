#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 12 19:25:11 2023

@author: bonnie
"""
from tkinter import *

root=Tk()
root.title("ASCII values")

root.geometry("400x400")
root.configure(background = 'snow')

enter_word = Entry(root)
enter_word.place(relx=0.5, rely=0.4, anchor=CENTER)

label = Label(root, text = "name in ascii: ", bg="light yellow", fg="black")

def asciiConverter():
    input_word = enter_word.get()
    
    for letter in input_word :
        label["text"] += str(ord(letter)) + "  "
    
btn = Button(root, text="show name in ascii", command=asciiConverter, bg='gold', fg='black')
btn.place(relx=0.5, rely=0.5, anchor=CENTER)
    
label.place(relx=0.5, rely=0.6, anchor=CENTER)
    
root.mainloop()
