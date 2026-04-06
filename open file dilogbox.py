from tkinter import *
from PIL import ImageTk,Image
from tkinter import filedialog
root = Tk()
root.title('codemy.com Image Viewer')
root.iconbitmap('C:\\Users\\pinku\\OneDrive\\Documents\\vs code tutorial (1)\\icon.ico')

root.filename = filedialog.askopenfilename(initialdir="C:\\Users\\pinku\\OneDrive\\Documents\\vs code tutorial (1)\\icon.ico",title="select a file",filetype=(("png files",".png"),("all files","*.*"))

root.mainloop()