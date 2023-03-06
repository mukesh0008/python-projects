from tkinter import*

root = Tk()
root.geometry("500x300")

def getvals():
    print("registered")

Label(root, text="pharmacy Registration form", font="ar 15 bold").grid(row=0, column=3)

name = Label(root, text="name")
phone = Label(root, text="phone")
gender = Label(root, text="gender")
age = Label(root, text="age")
address = Label(root, text="address")

name.grid(row=1, column=2)
phone.grid(row=2, column=2)
gender.grid(row=3, column=2)
age.grid(row=4, column=2)
address.grid(row=5, column=2)

namevalue = StringVar
phonevalue = StringVar
gendervalue = StringVar
agevalue = StringVar
addressvalue = StringVar
checkvalue = IntVar

nameentry = Entry(root, textvariable =namevalue)
phoneentry = Entry(root, textvariable =phonevalue)
genderentry = Entry(root, textvariable =gendervalue)
ageentry = Entry(root, textvariable =agevalue)
addressentry = Entry(root, textvariable =addressvalue)

nameentry.grid(row=1, column=3)
phoneentry.grid(row=2, column=3)
genderentry.grid(row=3, column=3)
ageentry.grid(row=4, column=3)
addressentry.grid(row=5, column=3)


checkbtn = Checkbutton(text= "remember me?", variable = checkvalue)
checkbtn.grid(row=6, column=3)

Button(text="Submit", command=getvals).grid(row=7, column=3)



root.mainloop()
