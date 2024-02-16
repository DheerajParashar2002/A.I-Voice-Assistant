import tkinter as tk
from PIL import Image,ImageTk,ImageSequence  #pip install Pillow
import time
import pygame
from pygame import mixer

mixer.init()

root = tk.Tk()
root.geometry("1000x620")
def play_gif():
    root.lift()
    root.attributes("-topmost",True)
    global img
    img = Image.open("image_processing20210729-32645-tn0q8p.gif")
    lbl = tk.Label(root)
    lbl.place(x=0,y=0)
    i=0
    mixer.music.load("ring 1.mp3")
    mixer.music.play()
    for img in ImageSequence.Iterator(img):
        img = img.resize((1000,620))
        img = ImageTk.PhotoImage(img)
        lbl.config(image=img)
        root.update()
        time.sleep(0.05)
    root.destroy()

play_gif()
root.mainloop()