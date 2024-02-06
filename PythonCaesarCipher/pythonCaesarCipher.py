# BY KHAWAR KHAN
# ENCRYPTION AND DECRYPTION OF A MESSAGE
# BY CYPHER TEXT METHOD
# Author: Khawar Khan
# Git Repository : https://github.com/KhawarGit/PythonCaesarCipher

from tkinter import *

m = Tk()
m.geometry("1000x600")
m.configure(background='peach puff')
m.title("The Cipher Converter by KHAWAR KHAN.")
creator = Label(m, text="Encrypter and Decrypter By Using Cypher text By \n   KHAWAR KHAN",font="comicsansms 20 bold",bd=10,relief=RIDGE).pack(side=BOTTOM, fill=X)
def cipher():
    cipher = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

    encrypted = ""
    x = t.get()
    k = int(z.get())
    for i in range(len(x)):
        if x[i] != ' ':
            c = x[i].upper()
            ci = (cipher.index(c)+k)%26
            j = cipher[ci]
            encrypted += j
        else:
            encrypted += ' '
    ch.set(str(encrypted))

def decrypt():
    decrypt = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

    decrypted = ""
    x = t.get()
    k = int(z.get())
    for i in range(len(x)):
        if x[i] != ' ':
            c = x[i].upper()
            ci = (decrypt.index(c)-k)%26
            j = decrypt[ci]
            decrypted += j
        else:
            decrypted += ' '
    ch.set(str(decrypted))





t = StringVar()
z = IntVar()
ch = StringVar()

l = Label(m, text = 'Write the text to convert : ',font = "comicaansms 20 bold").pack(side=LEFT, anchor=NW)
e1 = Entry(m,font = "comicaansms 20 bold",textvariable=t).place(x = 600, y = 0)

l2 = Label(m,text = "Give the key value i.e. value of K : ",font = "comicaansms 20 bold").place(x=0, y=50)
e2 = Entry(m,font = "comicaansms 20 bold",textvariable=z).place(x = 600, y=50)

la = Label(m,text="The converted text is : ",font = "comicaansms 20 bold").place(x=0, y=100)
e3 = Entry(m,font = "comicaansms 20 bold",state = DISABLED,textvariable=ch).place(x=600,y=100)

b = Button(m,text="Encrypt to cipher",font = "comicaansms 20 bold",command=cipher).place(x=600, y=150)
b1 = Button(m,text="Decrypt from cipher",font = "comicaansms 20 bold",command = decrypt).place(x=600,y=200)

m.mainloop()
