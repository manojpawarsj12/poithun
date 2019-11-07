# imports
import os
import tkinter as tkr
from tkinter import filedialog, simpledialog

import mutagen.mp3
from pygame import mixer


def play():
    mp3 = mutagen.mp3.MP3(playlist.get(tkr.ACTIVE))
    mixer.init(frequency=mp3.info.sample_rate,
               size=-16, channels=8, buffer=4096)
    mixer.music.load(playlist.get(tkr.ACTIVE))
    var.set(playlist.get(tkr.ACTIVE))
    mixer.music.play()


def end():
    mixer.music.stop()


def pause():
    mixer.music.pause()


def contin():
    mixer.music.unpause()


def increase():
    volume = mixer.music.get_volume()
    volume = volume+0.1
    mixer.music.set_volume(volume)


def decrease():
    volume = mixer.music.get_volume()
    volume = volume-0.1
    mixer.music.set_volume(volume)


def file():
    d = filedialog.askdirectory(
        initialdir=os.getcwd(), title='Please select a directory')
    if os.path.isdir(d):
        os.chdir(d)
    else:
        print("wrong file path try again \n")
        exit(0)
    print(os.getcwd)
    songlist = os.listdir()
    songlist1 = list()
    for item in songlist:
        if item.endswith('.mp3'):
            songlist1.append(item)
    for item in songlist1:
        pos = 0
        playlist.insert(pos, item)
        pos += 1


def downloads():
    a = simpledialog.askstring(
        prompt="enter name of song that you want to download", title="music download")
    os.system('python songdownload.py dl {0}'.format(a))
# defining player


player = tkr.Tk()
player.title("audio player")
player.geometry("700x600")
button1 = tkr.Button(player, width=5, height=3, text='play', command=play)
button2 = tkr.Button(player, width=5, height=3, text='stop', command=end)
button3 = tkr.Button(player, width=5, height=3,
                     text='continue', command=contin)
button4 = tkr.Button(player, width=5, height=3, text='pause', command=pause)
button5 = tkr.Button(player, width=5, height=3,
                     text='increase volume', command=increase)
button6 = tkr.Button(player, width=5, height=3,
                     text='decrease volume', command=decrease)
button7 = tkr.Button(player, width=5, height=3,
                     text='select a file ', command=file)
button8 = tkr.Button(player, width=5, height=3,
                     text='download songs', command=downloads)


playlist = tkr.Listbox(player, highlightcolor="blue", selectmode=tkr.SINGLE)
label1 = tkr.LabelFrame(player, text="Song Name")
label1.pack(fill='both', expand='yes')
var = tkr.StringVar()
songtitle = tkr.Label(player, textvariable=var)
button7.pack(fill='x')
button1.pack(fill='x')
button3.pack(fill='x')
button4.pack(fill='x')
button2.pack(fill='x')
button5.pack(fill='x')
button6.pack(fill='x')
button8.pack(fill='x')
songtitle.pack()
playlist.pack(fill='both', expand="yes")

player.mainloop()
