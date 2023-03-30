import os
import tkinter
from tkinter import *
import customtkinter
from PIL import Image
import subprocess as sub
import sys


# Modes: system (default), light, dark
customtkinter.set_appearance_mode("system")
# Themes: blue (default), dark-blue, green
customtkinter.set_default_color_theme("blue")

app = customtkinter.CTk()

app.title("Spotify Playlist Downloader")
# app.iconbitmap("C:/Users/kaush/PycharmProjects/Spotify_Converter/spotlogo.png")
app.geometry('700x500')

logo = customtkinter.CTkImage(
    light_image=Image.open("spotlogo.png"), size=(225,225))
text_var = tkinter.StringVar(value="")
label = customtkinter.CTkLabel(app, image=logo, textvariable=text_var)
label.place(x=75, y=200)

# pl is playlist
pl_text = StringVar()
pl_label = customtkinter.CTkLabel(
    app, text='Playlist URL here: ',  width=150, height=30)
pl_label.place(x=10, y=10)
pl_entry = customtkinter.CTkEntry(
    app, textvariable=pl_text, width=150, height=30)
pl_entry.place(x=180, y=10)

# fl is file location
fl_text = StringVar()
fl_label = customtkinter.CTkLabel(
    app, text='Local folder location here: ', width=150, height=30)
fl_label.place(x=350, y=10)
fl_entry = customtkinter.CTkEntry(
    app, textvariable=fl_text, width=150, height=30)
fl_entry.place(x=540, y=10)


playlist_name = "https://open.spotify.com/playlist/5EuwVuogRqBqKJrSJsD29v"


def set_pl():
    command = "spotdl --output " + fl_text.get() + " " + pl_text.get()
    label = customtkinter.CTkTextbox(app, wrap="word")
    label.insert("0.0", os.popen(command).read())
    label.place(x=375, y=200)
    pl_entry.delete(0, END)
    fl_entry.delete(0, END)


enter_btn = customtkinter.CTkButton(
    app, text='Enter!', width=140, height=50, command=set_pl)
enter_btn.place(x=120, y=130)



app.mainloop()
