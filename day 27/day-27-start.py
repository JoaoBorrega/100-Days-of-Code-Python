from tkinter import *

window = Tk()

window.title("My First GUI Program")
window.minsize(width=500, height=300)

# Label
my_label = Label(text="I am a Label", font=("Arial", 24, "bold"))
my_label["text"] = "New Text"
# my_label.config(text="New Text")
my_label.pack()
# podemos usar em vez do .pack, o .place, em que escolhemos a localização exata, por exemplo
# my_label.place(x=100, y=200)

# temos ainda a hipotese de escolher em grelha. por exemplo
# my_label.grid(column=0, row=0)

# Button
def button_clicked():
    print("I got clicked")
    new_text = input.get()
    my_label.config(text=new_text)

button = Button(text="Click Me", command=button_clicked)
button.pack()
# button.grid(column=1, row=1)

# Entry
input = Entry(width=10)
input.pack()
print(input.get())
# input.grid(column=2, row=2)

window.mainloop()


# 🚨 outro exercicio

from tkinter import *

window = Tk()

window.title("My First GUI Program")
window.minsize(width=500, height=300)
# window.config(padx=20, pady=20)

# Label
my_label = Label(text="I am a Label", font=("Arial", 24, "bold"))
my_label["text"] = "New Text"
# my_label.config(text="New Text")
my_label.grid(column=0, row=0)

# Button

def button_clicked():
    print("I got clicked")
    new_text = input.get()
    my_label.config(text=new_text)

button = Button(text="Click Me", command=button_clicked)
button.grid(column=1, row=1)

new_button = Button(text="New Button")
new_button.grid(column=2, row=0)

# Entry
input = Entry(width=10)
print(input.get())
input.grid(column=3, row=2)

window.mainloop()