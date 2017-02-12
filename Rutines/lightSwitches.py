from tkinter import *
from tkinter import ttk
import RPi.GPIO as GPIO
import time     as tm
import numpy    as np

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(17, GPIO.OUT)
GPIO.setup(27, GPIO.OUT)
GPIO.setup(22, GPIO.OUT)
switch_B =0
switch_R =0


def switchingLighs(registers,percentage):
    w = registers
    while w < registers:
        input_data = int(percentage)
        print("input data")
        print(input_data)
        #clock_out = int(input("clock out data:"))
        data0=[0,0,0,0,0,0,0,0]
        data25 = [0,1,0,0,0,0,0,0]
        data50 = [0,0,1,0,0,0,0,0]
        data75 = [0,0,0,1,0,0,0,0]
        data100 = [0,0,0,0,1,0,0,0]
        if input_data == 0:
            a = 0
            while a < 4:
                v = data0[a]
                if v==0:
                    GPIO.output(17, GPIO.LOW)
                    GPIO.output(27, GPIO.HIGH)
                    GPIO.output(27, GPIO.LOW)
                    GPIO.output(17, GPIO.LOW)
                    GPIO.output(22, GPIO.HIGH)
                    GPIO.output(22, GPIO.LOW)
                    a=a+1
                    print("11 was set to one")
                elif v==1:
                    GPIO.output(17, GPIO.HIGH)
                    GPIO.output(27, GPIO.HIGH)
                    GPIO.output(27, GPIO.LOW)
                    GPIO.output(17, GPIO.LOW)
                    GPIO.output(22, GPIO.HIGH)
                    GPIO.output(22, GPIO.LOW)
                    a=a+1
                    print("11 was set to zero")
        elif input_data == 25:
            a = 0
            while a < 4:
                v = data25[a]
                if v==0:
                    GPIO.output(17, GPIO.LOW)
                    GPIO.output(27, GPIO.HIGH)
                    GPIO.output(27, GPIO.LOW)
                    GPIO.output(17, GPIO.LOW)
                    GPIO.output(22, GPIO.HIGH)
                    GPIO.output(22, GPIO.LOW)
                    a=a+1
                    print("11 was set to one")
                elif v==1:
                    GPIO.output(17, GPIO.HIGH)
                    GPIO.output(27, GPIO.HIGH)
                    GPIO.output(27, GPIO.LOW)
                    GPIO.output(17, GPIO.LOW)
                    GPIO.output(22, GPIO.HIGH)
                    GPIO.output(22, GPIO.LOW)
                    a=a+1
                    print("11 was set to zero")
        elif input_data == 50:
            b = 0
            while b < 4:
                v2 = data50[b]
                if v2 == 0:
                    GPIO.output(17, GPIO.LOW)
                    GPIO.output(27, GPIO.HIGH)
                    GPIO.output(27, GPIO.LOW)
                    GPIO.output(17, GPIO.LOW)
                    GPIO.output(22, GPIO.HIGH)
                    GPIO.output(22, GPIO.LOW)
                    b=b+1
                    print("11 was set to one")
                elif v2 == 1:
                    GPIO.output(17, GPIO.HIGH)
                    GPIO.output(27, GPIO.HIGH)
                    GPIO.output(27, GPIO.LOW)
                    GPIO.output(17, GPIO.LOW)
                    GPIO.output(22, GPIO.HIGH)
                    GPIO.output(22, GPIO.LOW)
                    b = b + 1
                    print("11 was set to zero")
        elif input_data == 75:
            c = 0
            while c < 4:
                v3 = data75[c]
                if v3 == 0:
                    GPIO.output(17, GPIO.LOW)
                    GPIO.output(27, GPIO.HIGH)
                    GPIO.output(27, GPIO.LOW)
                    GPIO.output(17, GPIO.LOW)
                    GPIO.output(22, GPIO.HIGH)
                    GPIO.output(22, GPIO.LOW)
                    c = c + 1
                    print("11 was set to one")
                elif v3 == 1:
                    GPIO.output(17, GPIO.HIGH)
                    GPIO.output(27, GPIO.HIGH)
                    GPIO.output(27, GPIO.LOW)
                    GPIO.output(17, GPIO.LOW)
                    GPIO.output(22, GPIO.HIGH)
                    GPIO.output(22, GPIO.LOW)
                    c = c + 1
                    print("11 was set to zero")
        elif input_data == 100:
            d = 0
            while d < 4:
                v4 = data100[d]
                if v4 == 0:
                    GPIO.output(17, GPIO.LOW)
                    GPIO.output(27, GPIO.HIGH)
                    GPIO.output(27, GPIO.LOW)
                    GPIO.output(17, GPIO.LOW)
                    GPIO.output(22, GPIO.HIGH)
                    GPIO.output(22, GPIO.LOW)
                    d = d + 1
                    print("11 was set to one")
                elif v4 == 1:
                    GPIO.output(17, GPIO.HIGH)
                    GPIO.output(27, GPIO.HIGH)
                    GPIO.output(27, GPIO.LOW)
                    GPIO.output(17, GPIO.LOW)
                    GPIO.output(22, GPIO.HIGH)
                    GPIO.output(22, GPIO.LOW)
                    d = d + 1
                    print("11 was set to zero")
        w=w+1


root = Tk()
root.title("light Switches")

mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
mainframe.columnconfigure(0, weight=1)
mainframe.rowconfigure(0, weight=1)

register_b = StringVar()
percentage0_b = IntVar()
percentage25_b = IntVar()
percentage50_b = IntVar()
percentage75_b = IntVar()
percentage100_b = IntVar()


def cb_check_0_b():
    global switch_B
    if percentage0_b.get():
        switch_B=0
        percentage_25_b.config(state=DISABLED)
        percentage_50_b.config(state=DISABLED)
        percentage_75_b.config(state=DISABLED)
        percentage_100_b.config(state=DISABLED)
    else:
        percentage_0_b.config(state=NORMAL)
        percentage_25_b.config(state=NORMAL)
        percentage_50_b.config(state=NORMAL)
        percentage_75_b.config(state=NORMAL)
        percentage_100_b.config(state=NORMAL)


def cb_check_25_b():
    global switch_B
    if percentage25_b.get():
        switch_B=25
        percentage_0_b.config(state=DISABLED)
        percentage_50_b.config(state=DISABLED)
        percentage_75_b.config(state=DISABLED)
        percentage_100_b.config(state=DISABLED)
    else:
        percentage_0_b.config(state=NORMAL)
        percentage_25_b.config(state=NORMAL)
        percentage_50_b.config(state=NORMAL)
        percentage_75_b.config(state=NORMAL)
        percentage_100_b.config(state=NORMAL)


def cb_check_50_b():
    global switch_B
    if percentage50_b.get():
        switch_B=50
        percentage_0_b.config(state=DISABLED)
        percentage_25_b.config(state=DISABLED)
        percentage_75_b.config(state=DISABLED)
        percentage_100_b.config(state=DISABLED)
    else:
        percentage_0_b.config(state=NORMAL)
        percentage_25_b.config(state=NORMAL)
        percentage_50_b.config(state=NORMAL)
        percentage_75_b.config(state=NORMAL)
        percentage_100_b.config(state=NORMAL)


def cb_check_75_b():
    global switch_B
    if percentage75_b.get():
        switch_B=75
        percentage_0_b.config(state=DISABLED)
        percentage_25_b.config(state=DISABLED)
        percentage_50_b.config(state=DISABLED)
        percentage_100_b.config(state=DISABLED)
    else:
        percentage_0_b.config(state=NORMAL)
        percentage_25_b.config(state=NORMAL)
        percentage_50_b.config(state=NORMAL)
        percentage_75_b.config(state=NORMAL)
        percentage_100_b.config(state=NORMAL)


def cb_check_100_b():
    global switch_B
    if percentage100_b.get():
        switch_B=100
        percentage_0_b.config(state=DISABLED)
        percentage_25_b.config(state=DISABLED)
        percentage_50_b.config(state=DISABLED)
        percentage_75_b.config(state=DISABLED)
    else:
        percentage_0_b.config(state=NORMAL)
        percentage_25_b.config(state=NORMAL)
        percentage_50_b.config(state=NORMAL)
        percentage_75_b.config(state=NORMAL)
        percentage_100_b.config(state=NORMAL)

registers_entry = ttk.Entry(mainframe, width=12, textvariable=register_b)
registers_entry.grid(column=2, row=1, sticky=(W, E))


# blue

register_b_label=ttk.Label(mainframe, text="Register B")
register_b_label.grid(column=1, row=1, sticky=E)
percentage_0_b = ttk.Checkbutton(mainframe, text="0 %", variable=percentage0_b, command=cb_check_0_b)
percentage_0_b.grid(column=2, row=2, sticky=(W, E))

percentage_25_b = ttk.Checkbutton(mainframe, text="25 %", variable=percentage25_b, command=cb_check_25_b)
percentage_25_b.grid(column=2, row=3, sticky=(W, E))

percentage_50_b = ttk.Checkbutton(mainframe, text="50 %", variable=percentage50_b, command=cb_check_50_b)
percentage_50_b.grid(column=2, row=4, sticky=(W, E))

percentage_75_b = ttk.Checkbutton(mainframe, text="75 %", variable=percentage75_b, command=cb_check_75_b)
percentage_75_b.grid(column=2, row=5, sticky=(W, E))

percentage_100_b = ttk.Checkbutton(mainframe, text="100 %", variable=percentage100_b, command=cb_check_100_b)
percentage_100_b.grid(column=2, row=6, sticky=(W, E))


#ttk.Button(mainframe, text="Switch", command=calculate).grid(column=2, row=7, sticky=(W, E))


# red
register_r = StringVar()
percentage0_r = IntVar()
percentage25_r = IntVar()
percentage50_r = IntVar()
percentage75_r = IntVar()
percentage100_r = IntVar()



def cb_check_0_r():
    global switch_R
    if percentage0_r.get():
        switch_R=0
        percentage_25_r.config(state=DISABLED)
        percentage_50_r.config(state=DISABLED)
        percentage_75_r.config(state=DISABLED)
        percentage_100_r.config(state=DISABLED)
    else:
        percentage_0_r.config(state=NORMAL)
        percentage_25_r.config(state=NORMAL)
        percentage_50_r.config(state=NORMAL)
        percentage_75_r.config(state=NORMAL)
        percentage_100_r.config(state=NORMAL)


def cb_check_25_r():
    global switch_R
    if percentage25_r.get():
        switch_R=25
        percentage_0_r.config(state=DISABLED)
        percentage_50_r.config(state=DISABLED)
        percentage_75_r.config(state=DISABLED)
        percentage_100_r.config(state=DISABLED)
    else:
        percentage_0_r.config(state=NORMAL)
        percentage_25_r.config(state=NORMAL)
        percentage_50_r.config(state=NORMAL)
        percentage_75_r.config(state=NORMAL)
        percentage_100_r.config(state=NORMAL)


def cb_check_50_r():
    global switch_R
    if percentage50_r.get():
        switch_R=50
        percentage_0_r.config(state=DISABLED)
        percentage_25_r.config(state=DISABLED)
        percentage_75_r.config(state=DISABLED)
        percentage_100_r.config(state=DISABLED)
    else:
        percentage_0_r.config(state=NORMAL)
        percentage_25_r.config(state=NORMAL)
        percentage_50_r.config(state=NORMAL)
        percentage_75_r.config(state=NORMAL)
        percentage_100_r.config(state=NORMAL)


def cb_check_75_r():
    global switch_R
    if percentage75_r.get():
        switch_R=75
        percentage_0_r.config(state=DISABLED)
        percentage_25_r.config(state=DISABLED)
        percentage_50_r.config(state=DISABLED)
        percentage_100_r.config(state=DISABLED)
    else:
        percentage_0_r.config(state=NORMAL)
        percentage_25_r.config(state=NORMAL)
        percentage_50_r.config(state=NORMAL)
        percentage_75_r.config(state=NORMAL)
        percentage_100_r.config(state=NORMAL)


def cb_check_100_r():
    global switch_R
    if percentage100_r.get():
        percentage_0_r.config(state=DISABLED)
        percentage_25_r.config(state=DISABLED)
        percentage_50_r.config(state=DISABLED)
        percentage_75_r.config(state=DISABLED)
        switch_R = 100
    else:
        percentage_0_r.config(state=NORMAL)
        percentage_25_r.config(state=NORMAL)
        percentage_50_r.config(state=NORMAL)
        percentage_75_r.config(state=NORMAL)
        percentage_100_r.config(state=NORMAL)


def calculate(*args):
    global switch_R, switch_B
    try:
        value_b = switch_B
        value_r = switch_R

        registers_b = int(register_b.get())
        registers_r = int(register_r.get())

        switchingLighs(registers_b,value_r)
        switchingLighs(registers_r,value_b)

        register_b.set(value_b)
        register_r.set(value_r)
    except ValueError:
        pass

registers_entry_r = ttk.Entry(mainframe, width=12, textvariable=register_r)
registers_entry_r.grid(column=4, row=1, sticky=(W, E))

register_r_label=ttk.Label(mainframe, text="Register R")
register_r_label.grid(column=3, row=1, sticky=E)

percentage_0_r = ttk.Checkbutton(mainframe, text="0 %", variable=percentage0_r, command=cb_check_0_r)
percentage_0_r.grid(column=4, row=2, sticky=(W, E))

percentage_25_r = ttk.Checkbutton(mainframe, text="25 %", variable=percentage25_r, command=cb_check_25_r)
percentage_25_r.grid(column=4, row=3, sticky=(W, E))

percentage_50_r = ttk.Checkbutton(mainframe, text="50 %", variable=percentage50_r, command=cb_check_50_r)
percentage_50_r.grid(column=4, row=4, sticky=(W, E))

percentage_75_r = ttk.Checkbutton(mainframe, text="75 %", variable=percentage75_r, command=cb_check_75_r)
percentage_75_r.grid(column=4, row=5, sticky=(W, E))

percentage_100_r = ttk.Checkbutton(mainframe, text="100 %", variable=percentage100_r, command=cb_check_100_r)
percentage_100_r.grid(column=4, row=6, sticky=(W, E))

ttk.Button(mainframe, text="Switch", command=calculate).grid(column=2, row=7, sticky=(W, E))


for child in mainframe.winfo_children(): child.grid_configure(padx=70, pady=15)

registers_entry.focus()
registers_entry_r.focus()
root.bind('<Return>', calculate)

root.mainloop()