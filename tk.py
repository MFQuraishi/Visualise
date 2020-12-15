from tkinter import *
from PIL import Image, ImageTk
import os
from tkinter import messagebox
from tkinter import filedialog

root = Tk()
root.geometry("1000x750")
root.resizable(False, False)


def resize_image(root, copy_of_image, label1):
    new_height = 750
    new_width = 900
    image=copy_of_image.resize((new_width,new_height))
    photo = ImageTk.PhotoImage(image)
    label1.configure(image=photo)
    label1.image = photo


def next():
    global n
    global items_list
    n = (n+1)%len(items_list)
    img1 = items_list[n]
    print(img1)
    image = Image.open(directory_name + "/" + img1)
    copy_of_image = image.copy()
    photo = ImageTk.PhotoImage(image)
    label = Label(root, image=photo)
    label.bind('<configure>',resize_image(root,copy_of_image,label1))
    label.pack()

def previous():
    global n
    global items_list
    n = (n-1)%len(items_list)
    img1 = items_list[n]
    print(img1)
    image = Image.open(directory_name + "/" + img1)
    copy_of_image = image.copy()
    photo = ImageTk.PhotoImage(image)
    label = Label(root, image=photo)
    label.bind('<configure>',resize_image(root,copy_of_image,label1))
    label.pack()

def browse_folder():
    global directory_name
    global items_list
    global n
    
    directory_name =  filedialog.askdirectory(initialdir="./", title="Select Folder")
    items_list = os.listdir(directory_name)
    if len(items_list) <= 0:
        messagebox.showerror("error", "no images in the given folder")
        exit0()
    n = 0
    img1 = items_list[n]

    image = Image.open(directory_name+ "/" + img1)
    copy_of_image = image.copy()
    photo = ImageTk.PhotoImage(image)

    label = Label(root, image=photo)
    label.bind('<configure>',resize_image(root,copy_of_image,label1))
    label.pack()
    
    
def exit0():
    root.destroy( )

    
#menu bar
menubar = Menu(root)
root.config(menu = menubar)
file_menu = Menu(menubar)
menubar.add_cascade(label="File",menu=file_menu)
file_menu.add_command(label="Browse Folder", command=browse_folder)
file_menu.add_separator()
file_menu.add_command(label="exit", command=exit0)



#images part and swipe buttons
n=0
items_list = os.listdir("images")
directory_name = "./images/"

if len(items_list) <= 0:
    messagebox.showerror("error", "no images in the given folder")
    exit0()
    
img1 = items_list[n]

image = Image.open(directory_name + img1)
copy_of_image = image.copy()
photo = ImageTk.PhotoImage(image)

label1 = Label(root, image=photo)
label1.bind('<configure>',resize_image(root,copy_of_image,label1))
label1.pack()

b1 = Button(root,text=">>", width=5, height=10, command=next)
b1.place(x=960,y=300)

b2 = Button(root,text="<<", width=5, height=10, command=previous)
b2.place(x=0,y=300)

root.mainloop()
