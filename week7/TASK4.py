from tkinter import*
window=()
window.title("Simple Calculator")
def calculate():
    num1=float(entry1.get())
    num2=float(entry2.get())
    total= num1+num2
    result_label.config(text="Total ="+str(total))
    label1 = Label(window,text="First Number")
    label1.pack()

    entry1 = Entry(window)
    entry1.pack()

    label2=Label(window, text="Second Number")
    label2.pack()
    entry2 = Entry(window)
    entry2.pack()
    calculate_button = Button(window, text="Calculate", command=calculate)
    calculate_button.pack()
    result_Label = Label(window, text="Total =")
    result_Label.pack()
    window.mainloop()

