# import modules
import pygame
import tkinter as tkr


pygame.init()

# Create Window
player = tkr.Tk()

# Edit Window
player.title("Audio Player")
player.geometry("205x34")

# get song
file = "Song3.mp3"

# Activate Event
def Play():
    pygame.mixer_init()
    pygame.mixer.music.load(file)
    pygame.mixer.music.play()

def ExitPlayer():
    pygame.mixer.music.stop()


# Register Button
Button1 = tkr.Button(player, width=5, height=3, text="Play", command=Play)
Button1.pack(fill="x")
Button2 = tkr.Button(player, width=5, height=3, text="Stop", command=ExitPlayer)
Button2.pack(fill="x")

# Song Name
label1 = tkr.LabelFrame(player, text="Song Name")
label1.pack(file="both", expand="yes")
contents1 = tkr.Label(label1, text=file)
contents1.pack()
# activate
player.mainloop()