from tkinter import *
import cv2
from PIL import Image, ImageTk

def resize_image(image_path, width, height):
    original_image = Image.open(image_path)
    resized_image = original_image.resize((width, height))
    return ImageTk.PhotoImage(resized_image)

root = Tk()
root.title("Nama Aplikasi")
root.geometry("550x675")
root.resizable(False, False)
root.config(bg="#6F8FAF")


#ask fun
def ask ():
    print("ask")

#send fun
def send ():
    print("send")

#delete fun
def del_text ():
    print("text delete")

# frame
frame = LabelFrame(root, padx=100, pady=7, borderwidth=3, relief="raised")
frame.grid(row=0, column=1, padx=55, pady=10)

# Text Label
text_label = Label(frame, text="Nama Aplikasi", font=("comic Sans ms", 14, "bold"), bg="#356696", fg="#FFFFFF")
text_label.grid(row=0, column=0, padx=20, pady=10)

# Image
image_path = "Image/2.png"
new_width = 150  # Ganti dengan ukuran yang diinginkan
new_height = 100  # Ganti dengan ukuran yang diinginkan
image = resize_image(image_path, new_width, new_height)
image_label = Label(frame, image=image)
image_label.grid(row=1, column=0, pady=20)


#ADDING TEXT
text = Text(root , font= ('courior 10 bold') , bg ="#356696")
text.grid(row = 2 , column= 0)
text.place(x= 100, y = 375 , width = 375 , height = 100)

#ENTRY WIDGET
entry = Entry(root , justify=CENTER)
entry.place(x=100 , y=500 , width= 350 , height=30)

#Button 1
Button1 = Button(root , text ="ASK" , bg="#356696" , pady=16 , padx=40, borderwidth=3 , relief=SOLID , command=ask)
Button1.place(x= 70 , y= 575)

#Button 2
Button2 = Button(root , text ="Send" , bg="#356696" , pady=16 , padx=40, borderwidth=3 , relief=SOLID , command=send)
Button2.place(x= 400 , y= 575)

#Button 3
Button3 = Button(root , text ="Delete" , bg="#356696" , pady=16 , padx=40, borderwidth=3 , relief=SOLID , command=del_text)
Button3.place(x= 225 , y= 575)

root.mainloop()
