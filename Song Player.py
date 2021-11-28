# Song Player

from tkinter import *
from tkinter import filedialog
import pygame

pygame.mixer.init()

window = Tk()


def addsong():
    songs = filedialog.askopenfilenames(initialdir="D:\\Songs", filetypes=(("mp3 Files", "*.mp3"), ), title="Choose The Song To Add in the List")

    for songs in songs:
        songs = songs.replace("D:/Songs/", "")
        songs = songs.replace(".mp3", "")
        SongList.insert(END, f"{songs}")


def playsong():
    songs = SongList.get(ACTIVE)
    songs = f"D:\\Songs\\{songs}.mp3"
    pygame.mixer.music.load(songs)
    pygame.mixer.music.play(loops=0)

    
paused = False


def pausesong(isPaused):
    global paused
    paused = isPaused

    if paused:
        pygame.mixer.music.unpause()
        paused = False

    else:
        pygame.mixer.music.pause()
        paused = True



def nextsong():
    next_song = SongList.curselection()
    next_song = next_song[0]+1
    songs = SongList.get(next_song)
    songs = f"D:\\Songs\\{songs}.mp3"
    pygame.mixer.music.load(songs)
    pygame.mixer.music.play(loops=0)
    SongList.select_clear(0, END)
    SongList.activate(next_song)
    SongList.selection_set(next_song, last=None)



def prevsong():
    next_song = SongList.curselection()
    next_song = next_song[0]-1
    songs = SongList.get(next_song)
    songs = f"D:\\Songs\\{songs}.mp3"
    pygame.mixer.music.load(songs)
    pygame.mixer.music.play(loops=0)
    SongList.select_clear(0, END)
    SongList.activate(next_song)
    SongList.selection_set(next_song, last=None)

def stopsong():
    pygame.mixer.music.stop()
    SongList.select_clear(ACTIVE)

def removeSong():
    SongList.delete(ANCHOR)
    pygame.mixer.music.stop()

def ClearList():
    SongList.delete(0, END)
    pygame.mixer.music.stop()


play_Image = PhotoImage(file="PLAY.png")
pause_Image = PhotoImage(file="PAUSE.png")
forward_Image = PhotoImage(file="FORWARD.png")
backward_Image = PhotoImage(file="BACKWARD.png")
stop_Image = PhotoImage(file="STOP.png")

SongList = Listbox(window, bg="black", fg="yellow", width=90, height=20, font="comicsansms 15", selectforeground="white", selectbackground="grey")
SongList.pack(padx=90, pady=15)

# Creating the menu
Mymenu = Menu(window)
window.config(menu=Mymenu)


# Add Song Button
AddSong = Menu(Mymenu, tearoff=0)
Mymenu.add_cascade(label="Add Songs", menu=AddSong)
AddSong.add_command(label="Add Songs", command=addsong)

RemoveSong = Menu(Mymenu, tearoff=0)
Mymenu.add_cascade(label="Remove Song", menu=RemoveSong)
RemoveSong.add_command(label="Remove a song", command=removeSong)
RemoveSong.add_command(label="Clear The List", command=ClearList)

# Button Frame
btn_Frame = Frame(window)
btn_Frame.pack()


# Buttons
play_button = Button(btn_Frame, image= play_Image,borderwidth=0, command=playsong)
pause_button = Button(btn_Frame, image= pause_Image, borderwidth=0 ,command=lambda: pausesong(paused))
forward_button = Button(btn_Frame, image= forward_Image,borderwidth=0 ,command=nextsong)
backward_button = Button(btn_Frame, image= backward_Image, borderwidth=0 ,command=prevsong)
stop_button = Button(btn_Frame, image=stop_Image, borderwidth=0, command=stopsong)

play_button.grid(row=0, column=2, padx=15, pady=15)
pause_button.grid(row=0, column=3, padx=15, pady=15)
forward_button.grid(row=0, column=1, padx=15, pady=15)
backward_button.grid(row=0, column=0, padx=15, pady=15)
stop_button.grid(row=0, column=4, padx=15, pady=15)



window.mainloop()
