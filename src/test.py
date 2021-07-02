from tkinter import *
import os


def run():
    root.destroy()
    os.system('python C:\\Users\\mahek-bhavika\\Desktop\\TsecSem6\\MPR\\Emotion-detection-master\\src\\emotions.py --mode display')


root = Tk()
root.title('MPR')
root.geometry('1120x524')

bg = PhotoImage(file="resized.png")

# Create Canvas
canvas1 = Canvas(root, width=1120,
                 height=524)

canvas1.pack(fill="both")

# Display image
canvas1.create_image(0, 0, image=bg,
                     anchor="nw")
# Add Text
canvas1.create_text(560, 100, text="Welcome", font = ('Times', 45), fill="darkred")
canvas1.create_text(560, 300, text="Realtime Facial Emotion Detection", font = ('Times', 25), fill="darkred")

# Create Buttons
button1 = Button(root, text="Start", font = ('Times', 20), command=run)

# Display Buttons
button1_canvas = canvas1.create_window(515, 375,
                                       anchor="nw",
                                       window=button1)


root.mainloop()
