from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox
root=Tk()
root.title("Akshay's Adress Book")
addressBook={}

def addcontact():
    nameValue=name.get()
    emailValue=email.get()
    mobileValue=mobile.get()
    addressValue=address.get()

    addressBook[nameValue]=(addressValue,emailValue,mobileValue)
    bookList.insert(END,nameValue)

    clearentries()
    messagebox.showinfo("succses","contacts have been added succsefuly")
def clearentries():
    name.delete(0,END)
    email.delete(0,END)
    mobile.delete(0,END)
    address.delete(0,END)
def editcontact():
    selectedName=bookList.get(bookList.curselection())
    contactInfo=addressBook[selectedName]
    name.delete(0,END)
    name.insert(0,selectedName)
    address.delete(0,END)
    address.insert(0,contactInfo[0])
    email.delete(0,END)
    email.insert(0,contactInfo[1])
    mobile.delete(0,END)
    mobile.insert(0,contactInfo[2])
def deletecontacts():
    selectedName=bookList.get(bookList.curselection())
    del addressBook[selectedName]
    bookList.delete(bookList.curselection())
    clearentries()
    messagebox.showinfo("sucses!","the contact got deleted sucsesfuly")











bookName=Label(root,text="My Adress Book",width=40)
bookName.grid(row=0,column=1,pady=10,columnspan=3)

openButton=Button(root,text="Open")
openButton.grid(row=0,column=3,pady=10,)

bookList=Listbox(root,height=15,width=30)
bookList.grid(row=2,column=0,columnspan=3,rowspan=6,pady=10)

nameLabel=Label(root,text="Name:")
nameLabel.grid(row=1,column=3)

name=Entry(root)
name.grid(row=1,column=4,padx=10)

addressLabel=Label(root,text="Address:")
addressLabel.grid(row=2,column=3)

address=Entry(root)
address.grid(row=2,column=4,padx=10)

mobileLabel=Label(root,text="Mobile:")
mobileLabel.grid(row=3,column=3)

mobile=Entry(root)
mobile.grid(row=3,column=4,padx=10)

emailLabel=Label(root,text="Email:")
emailLabel.grid(row=4,column=3)

email=Entry(root)
email.grid(row=4,column=4,padx=10)

editButton=Button(root,text="Edit",command=editcontact)
editButton.grid(row=5,column=3,pady=10,)

deleteButton=Button(root,text="Delete",command=deletecontacts)
deleteButton.grid(row=5,column=4,pady=10,)

addButton=Button(root,text="Add",command=addcontact)
addButton.grid(row=6,column=3,pady=10,)

saveButton=Button(root,text="Save")
saveButton.grid(row=6,column=4,pady=10,)









root.mainloop()