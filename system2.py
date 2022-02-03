from tkinter import *
import sounddevice as sd
from scipy.io.wavfile import write 
from tkinter import messagebox
import matplotlib.pyplot as plt
import scipy
import scipy.io.wavfile as wav
from spafe.features.lpc import lpc
import matplotlib.pyplot as plt
from matplotlib import cm
import numpy as np
from tkinter import *
import matplotlib.pyplot as plt
import csv
import os
import warnings
import pyaudio
import wave
import sys


warnings.filterwarnings('ignore')

root = Tk()
root.geometry("1280x950")
root.title("Kadazandusn Speech Recognition")

def onclick():
    CHUNK = 1024
    FORMAT = pyaudio.paInt16
    CHANNELS = 2
    RATE = 16000
    RECORD_SECONDS = 3
    WAVE_OUTPUT_FILENAME = "babar.wav"

    p = pyaudio.PyAudio()

    stream = p.open(format=FORMAT,
                    channels=CHANNELS,
                    rate=RATE,
                    input=True,
                    frames_per_buffer=CHUNK)

    #print("* recording")

    frames = []

    for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
        data = stream.read(CHUNK)
        frames.append(data)

    #print("* done recording")

    stream.stop_stream()
    stream.close()
    p.terminate()

    wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(p.get_sample_size(FORMAT))
    wf.setframerate(RATE)
    wf.writeframes(b''.join(frames))
    wf.close()
    
def onclick1():
    CHUNK = 1024
    FORMAT = pyaudio.paInt16
    CHANNELS = 2
    RATE = 16000
    RECORD_SECONDS = 3
    WAVE_OUTPUT_FILENAME = "gayo.wav"

    p = pyaudio.PyAudio()

    stream = p.open(format=FORMAT,
                    channels=CHANNELS,
                    rate=RATE,
                    input=True,
                    frames_per_buffer=CHUNK)

    #print("* recording")

    frames = []

    for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
        data = stream.read(CHUNK)
        frames.append(data)

    #print("* done recording")

    stream.stop_stream()
    stream.close()
    p.terminate()

    wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(p.get_sample_size(FORMAT))
    wf.setframerate(RATE)
    wf.writeframes(b''.join(frames))
    wf.close()
    
    
def onclick2():
    CHUNK = 1024
    FORMAT = pyaudio.paInt16
    CHANNELS = 2
    RATE = 16000
    RECORD_SECONDS = 3
    WAVE_OUTPUT_FILENAME = "korut.wav"

    p = pyaudio.PyAudio()

    stream = p.open(format=FORMAT,
                    channels=CHANNELS,
                    rate=RATE,
                    input=True,
                    frames_per_buffer=CHUNK)

    #print("* recording")

    frames = []

    for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
        data = stream.read(CHUNK)
        frames.append(data)

    #print("* done recording")

    stream.stop_stream()
    stream.close()
    p.terminate()

    wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(p.get_sample_size(FORMAT))
    wf.setframerate(RATE)
    wf.writeframes(b''.join(frames))
    wf.close()
    

def onclick3():
    CHUNK = 1024
    FORMAT = pyaudio.paInt16
    CHANNELS = 2
    RATE = 16000
    RECORD_SECONDS = 3
    WAVE_OUTPUT_FILENAME = "palad.wav"

    p = pyaudio.PyAudio()

    stream = p.open(format=FORMAT,
                    channels=CHANNELS,
                    rate=RATE,
                    input=True,
                    frames_per_buffer=CHUNK)

    #print("* recording")

    frames = []

    for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
        data = stream.read(CHUNK)
        frames.append(data)

    #print("* done recording")

    stream.stop_stream()
    stream.close()
    p.terminate()

    wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(p.get_sample_size(FORMAT))
    wf.setframerate(RATE)
    wf.writeframes(b''.join(frames))
    wf.close()
    
def onclick4():
    CHUNK = 1024
    FORMAT = pyaudio.paInt16
    CHANNELS = 2
    RATE = 16000
    RECORD_SECONDS = 3
    WAVE_OUTPUT_FILENAME = "tanak.wav"

    p = pyaudio.PyAudio()

    stream = p.open(format=FORMAT,
                    channels=CHANNELS,
                    rate=RATE,
                    input=True,
                    frames_per_buffer=CHUNK)

    #print("* recording")

    frames = []

    for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
        data = stream.read(CHUNK)
        frames.append(data)

    #print("* done recording")

    stream.stop_stream()
    stream.close()
    p.terminate()

    wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(p.get_sample_size(FORMAT))
    wf.setframerate(RATE)
    wf.writeframes(b''.join(frames))
    wf.close()
    

def onclick5():
    CHUNK = 1024
    FORMAT = pyaudio.paInt16
    CHANNELS = 2
    RATE = 16000
    RECORD_SECONDS = 3
    WAVE_OUTPUT_FILENAME = "duo.wav"

    p = pyaudio.PyAudio()

    stream = p.open(format=FORMAT,
                    channels=CHANNELS,
                    rate=RATE,
                    input=True,
                    frames_per_buffer=CHUNK)

    #print("* recording")

    frames = []

    for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
        data = stream.read(CHUNK)
        frames.append(data)

    #print("* done recording")

    stream.stop_stream()
    stream.close()
    p.terminate()

    wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(p.get_sample_size(FORMAT))
    wf.setframerate(RATE)
    wf.writeframes(b''.join(frames))
    wf.close()
    

def onclick6():
    global wf
    global myLabel1
    num_ceps = 13
    lifter = 1
    normalize = True
    
#read wav 
    (fs,sig) = wav.read(wf)
# compute lpcs
    lpcs = lpc(sig=sig, fs=fs, num_ceps=num_ceps)
    print(lpcs)
    
    lpcs_feat = lpc(sig,fs,num_ceps)
    print(lpcs_feat)
    
    print("")
    print("MEAN OF EACH COLUMN")
    mean = lpcs_feat.mean(axis=0)
    print(mean)
    
    myLabel1 = Label(root,text=mean,bg="white" ,width ="50", height ="4").grid(row=3,column=2)
    myLabel2 = Label(root,text=mean,bg="white" ,width ="50", height ="4").grid(row=4,column=2)
    
    
def myDelete():
    myLabel1 = Label(root,bg="white" ,width ="50", height ="4").grid(row=3,column=2).destroy()
def myDelete1():
    myLabel2 = Label(root,bg="white" ,width ="50", height ="4").grid(row=4,column=2).destroy()
def myDelete2():
      myLabel3 = Label(root,bg="white" ,width ="50", height ="4").grid(row=5,column=2).destroy()
def myDelete3():
      myLabel4 = Label(root,bg="white" ,width ="50", height ="4").grid(row=6,column=2).destroy()
def myDelete4():
     myLabel5 = Label(root,bg="white" ,width ="50", height ="4").grid(row=7,column=2).destroy()
def myDelete5():
     myLabel6 = Label(root,bg="white" ,width ="50", height ="4").grid(row=8,column=2).destroy()
     
#Top HeadeR
myLabel0 = Label(root, text="",width ="50",bg="red",height ="2").grid(row=0,column=0)
myLabel7 = Label(root, text="",width ="50",bg="grey",height ="2").grid(row=1,column=0)
myLabel8 = Label(root, text="",width ="50",bg="red",height ="2").grid(row=2,column=0)

myLabel0 = Label(root, text="",width ="50",bg="red",height ="2").grid(row=0,column=0)
myLabel7 = Label(root, text="",width ="50",bg="grey",height ="2").grid(row=1,column=0)
myLabel8 = Label(root, text="",width ="50",bg="red",height ="2").grid(row=2,column=0)

myLabel0 = Label(root, text="",width ="50",bg="red",height ="2").grid(row=0,column=1)
myLabel7 = Label(root, text="",width ="50",bg="grey",height ="2").grid(row=1,column=1)
myLabel8 = Label(root, text="",width ="50",bg="red",height ="2").grid(row=2,column=1)

myLabel0 = Label(root, text="",width ="50",bg="red",height ="2").grid(row=0,column=2)
myLabel7 = Label(root, text="",width ="50",bg="grey",height ="2").grid(row=1,column=2)
myLabel8 = Label(root, text="",width ="50",bg="red",height ="2").grid(row=2,column=2)



#Button and Textview
#button1
myLabel1 = Label(root, text="", bg="white" ,width ="50", height ="4").grid(row=3,column=1)
myButton1 = Button(root, text="BABAR",width ="30", height ="4", command=onclick).grid(row=3,column=0)
#button2
myLabel2 = Label(root, text="",bg = "white" ,width ="50", height ="4").grid(row=4,column=1)
myButton2 = Button(root, text="GAYO",width ="30", height ="4", command=onclick1).grid(row=4,column=0)
#button3
myLabel3 = Label(root, text="",bg = "white" ,width ="50", height ="4").grid(row=5,column=1)
myButton3 = Button(root, text="KORUT" ,width ="30", height ="4", command = onclick2).grid(row=5,column=0)
#button4
myLabel4 = Label(root, text="",bg = "white" ,width ="50", height ="4").grid(row=6,column=1)
myButton4 = Button(root, text="PALAD" ,width ="30", height ="4", command = onclick3).grid(row=6,column=0)
#button5
myLabel5 = Label(root, text="",bg = "white" ,width ="50", height ="4").grid(row=7,column=1)
myButton5 = Button(root, text="TANAK",width ="30", height ="4", command = onclick4).grid(row=7,column=0)
#button6
myLabel6 = Label(root, text="",bg = "white" ,width ="50", height ="4").grid(row=8,column=1)
myButton6 = Button(root, text="DUO" ,width ="30", height ="4", command = onclick5).grid(row=8,column=0)



myLabelS = Label(root, text="",width ="53", height ="2").grid(row=10,column=0)
myLabelS = Label(root, text="",width ="53", height ="2").grid(row=10,column=1)
myLabelS = Label(root, text="",width ="53", height ="2").grid(row=11,column=0)
myLabelS = Label(root, text="",width ="53", height ="2").grid(row=11,column=1)

myButtonWave  = Button(root, text="Score", width ="30", height ="2", command=onclick6).grid(row=12,column=1)
myButtonExit  = Button(root, text="EXIT",bg = "grey" ,command=root.destroy, width ="30", height ="2" ).grid(row=12,column=2)

myButtonReset1 = Button(root, text="Clear Text",width ="15", height ="2", command=myDelete).grid(row=3,column=2)
myButtonReset2 = Button(root, text="Clear Text",width ="15", height ="2", command=myDelete1).grid(row=4,column=2)
myButtonReset3 = Button(root, text="Clear Text",width ="15", height ="2", command=myDelete2).grid(row=5,column=2)
myButtonReset4 = Button(root, text="Clear Text",width ="15", height ="2", command=myDelete3).grid(row=6,column=2)
myButtonReset5 = Button(root, text="Clear Text",width ="15", height ="2", command=myDelete4).grid(row=7,column=2)
myButtonReset6 = Button(root, text="Clear Text",width ="15", height ="2", command=myDelete5).grid(row=8,column=2)




root.mainloop()


