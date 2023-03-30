import os
import tkinter
from tkinter import *
import customtkinter
from PIL import Image

# Modes: system (default), light, dark
customtkinter.set_appearance_mode("System")
# Themes: blue (default), dark-blue, green
customtkinter.set_default_color_theme("blue")

app = customtkinter.CTk()

app.config(background='white')
app.title("Spotify Playlist Downloader")
# app.iconbitmap("C:/Users/kaush/PycharmProjects/Spotify_Converter/spotlogo.png")
app.geometry('700x500')

logo = customtkinter.CTkImage(
    light_image=Image.open("spotlogo.png"), size=(225,225))
text_var = tkinter.StringVar(value="")
label = customtkinter.CTkLabel(app, image=logo, textvariable=text_var)
label.place(x=215, y=200)

# pl is playlist
pl_text = StringVar()
pl_label = customtkinter.CTkLabel(
    app, text='Playlist URL here: ', fg_color='black', width=150, height=30)
pl_label.place(x=10, y=10)
pl_entry = customtkinter.CTkEntry(
    app, textvariable=pl_text, width=150, height=30)
pl_entry.place(x=180, y=10)

# fl is file location
fl_text = StringVar()
fl_label = customtkinter.CTkLabel(
    app, text='Local folder location here: ', fg_color='black', width=150, height=30)
fl_label.place(x=350, y=10)
fl_entry = customtkinter.CTkEntry(
    app, textvariable=fl_text, width=150, height=30)
fl_entry.place(x=540, y=10)

playlist_name = "https://open.spotify.com/playlist/5EuwVuogRqBqKJrSJsD29v"


def set_pl():
    os.system("spotdl --output " + fl_text.get() + " " + pl_text.get())
    pl_entry.delete(0, END)
    fl_entry.delete(0, END)


enter_btn = customtkinter.CTkButton(
    app, text='Enter!', width=140, height=50, command=set_pl)
enter_btn.place(x=270, y=130)

app.mainloop()
