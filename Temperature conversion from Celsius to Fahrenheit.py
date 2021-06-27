from tkinter import *

root=Tk()
root.geometry("400x300")
root.title("Celsius to Fahrenheit")
root.config(bg="black")

l1 = Label(root,text="Convertor From Celsius to Fahrenheit",font=("Roboto",15,"bold"),fg="White",bg="black")
l1.pack(side=TOP)

l2 = Label(root,text="Enter a value in Celsius to convert into Fahrenheit",font=("Roboto",10),fg="white",bg="black")
l2.place(x=50,y=80)

e1=Entry(width=48)
e1.place(x=50,y=110)

def equationforFtoC():
    temp_celsius=e1.get()
    if (temp_celsius.replace('.', '', 1).isdigit()):
        temp_fahrenheit = (float(temp_celsius) * 9 / 5) + 32
        output_fahrenheit.config(text='Temperature in Fahrenheit : ' + str(temp_fahrenheit))



output_fahrenheit = Label(root, font=(12),fg="white",bg="black")
output_fahrenheit.place(x=50,y=200)




b1 = Button(root,text="CONVERT!",font=(3242343242343),command=equationforFtoC,bg="black",fg="white")
b1.place(x=50,y=150)


























root.mainloop()






