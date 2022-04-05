import tkinter #Imports tkinter Package
from tkinter import * #Imports all Module of tkinter Package
from PyDictionary import PyDictionary #Imports PyDictionary Module
dictionary = PyDictionary() #Creates Classes
#Window Design
win = tkinter.Tk() #Creates Window
win.geometry("700x400") #Define the size of the window, 700 is width and 400 is height
win.title("Python Dictionary by Raunak") #Sets the title of the window to Python Dictionary
win.attributes('-alpha',1.5) #Sets the transparency level to 0.8
win.iconbitmap('Brand-Logo-Icon.ico') #Sets the Icon for Window when image is of Ico Type
win.configure(bg="Cyan") #Sets the background color of the window to Green

#Define Helper Function to use the other atributes of PyDictionary Class
def dict():
   meaning.config(text=dictionary.meaning(search.get())) #Search for the entered word in PyDictionary Module

# Code to add widgets will go here...
Label(win, text="Dictionary", font=("Times New Roman" ,20)).pack(pady=20) #Label for App Name
#Input Box for Search
frame = Frame(win) #Creates a Frame
Label(frame, text="Type any Word ", font=("Poppins bold", 15)).pack(side=LEFT) #Labels the Frame
search = Entry(frame, font=("Times New Roman", 15)) #Creates GUI for Input Box
search.pack()
frame.pack(pady=10)
#Displays the Meaning
frame1 = Frame(win) #Creates Second Frame
Label(frame1, text="Meaning:", font=("Aerial", 18)).pack(side=LEFT) #Label to display Meaning
meaning = Label(frame1, text="", font=("Poppins",15), bg="orange") #Attribute to Display meaning
meaning.pack()
frame1.pack(pady=10)
#Button for Search
Button(win, text="Find Meaning", font=("Poppins bold",15), command=dict).pack() #Creates a Button
win.mainloop() #Executes tkinter
