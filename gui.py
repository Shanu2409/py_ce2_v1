from tkinter import *
from PIL import Image, ImageTk


def gui(src):
    root = Tk()
    root.geometry('368x240')
    root.title("Instagram")
    # root.iconbitmap(r'insta2.ico')

    frame = Frame(root, width=480, height=360)
    frame.pack()
    frame.place(anchor='e', relx=0.65, rely=0.5)

    def description():
        global result
        result = text.get("1.0", "end")
        # print(result)
        # return result

    def postAndClose():
        btn.config(command='hello')
        description()
        root.destroy()

    photo = Image.open(src)
    resized = photo.resize((240, 144))
    new_photo = ImageTk.PhotoImage(resized)

    labelphoto = Label(frame, image=new_photo)
    labelphoto.pack()

    btn = Button(root, text=' Post ', width=8, height=2, command=postAndClose)
    btn.pack(side=BOTTOM)
    btn.place(anchor='e', relx=0.90, rely=0.70)

    text = Text(root, width=12, height=4)
    text.pack(side=RIGHT)
    text.place(anchor='center', relx=0.83, rely=0.4)

    root.mainloop()

    return result


# print(gui("./InstaPost/t.png"))
