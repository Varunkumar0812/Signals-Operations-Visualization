import matplotlib.pyplot as plt
import numpy as np
from tkinter import *
import tkinter as tk


root = tk.Tk()
root.geometry('400x400')
root.title('Basic Operations on Signal')
t = StringVar();
title = tk.Label(text="Basic Operations on sin(x) Signal", bg="Light Grey", font="Cambria", height=4, width=33,
                 fg="Dark Blue").place(x=15, y=10)
head1 = tk.Label(text="Click to see the original signal : ").place(x=10, y=140)
head2 = tk.Label(text="Select the operation you wish to perform : ").place(x=10, y=180)
ent = tk.Entry(textvariable=t).place(x = 100, y = 100)
l = np.linspace(-6.28, 6.28)

xpoints = l
ypoints = np.sin(l)

def get_inp_timeshift() :
    global ent
    en = int(t.get())
    print(en)
    right_shift(en)

def get_inp_timescale() :
    global ent
    en = float(t.get())
    print(en)
    time_scale(en)

def get_inp_ampscale() :
    global ent
    en = float(t.get())
    print(en)
    amp_scale(en)

def ori_sig():
    plt.plot(xpoints, ypoints)

    xaxisx = np.array([-8, 8])
    xaxisy = np.array(xaxisx) * 0

    yaxisy = np.array([-3, 3])
    yaxisx = np.array(yaxisy) * 0

    plt.plot(xaxisx, xaxisy)
    plt.plot(yaxisx, yaxisy)
    plt.show()


def right_shift(n):
    global l
    rs = []
    for x in l:
        rs.append(x - n)

    xpoints = rs

    plt.plot(xpoints, ypoints)

    xaxisx = np.array([-8 - n, 8 + n])
    xaxisy = np.array(xaxisx) * 0

    yaxisy = np.array([-3, 3])
    yaxisx = np.array(yaxisy) * 0

    plt.plot(xaxisx, xaxisy)
    plt.plot(yaxisx, yaxisy)
    plt.show()


def time_scale(n):
    global l
    ts = []
    for x in l:
        ts.append(n * x)

    xpoints = l
    ypoints = np.sin(ts)

    plt.plot(xpoints, ypoints)

    xaxisx = np.array([-8, 8])
    xaxisy = np.array(xaxisx) * 0

    yaxisy = np.array([-3, 3])
    yaxisx = np.array(yaxisy) * 0

    plt.plot(xaxisx, xaxisy)
    plt.plot(yaxisx, yaxisy)
    plt.show()


def amp_scale(n):
    global l
    amp = []
    ypoints = np.sin(l) * n

    plt.plot(xpoints, ypoints)

    xaxisx = np.array([-8, 8])
    xaxisy = np.array(xaxisx) * 0

    yaxisy = np.array([-n, n])
    yaxisx = np.array(yaxisy) * 0

    plt.plot(xaxisx, xaxisy)
    plt.plot(yaxisx, yaxisy)
    plt.show()


def reverse():
    global l
    ypoints = -1 * np.sin(l)

    plt.plot(xpoints, ypoints)

    plt.show()


def clo_win():
    plt.close()


# print("\n\t1 - Original Signal\n\t2 - Time Shifting\n\t3 - Time Scaling\n\t4 - Amplitude Scaling\n\t5 - Time Reversal")
# op = int(input("\nEnter your option : "))
#
# if op == 1 :
#     ori_sig()
# elif op == 2 :
#     n = int(input("Enter how many units you want to shift : "))
#     if n < 0 :
#         right_shift(abs(n))
#     else :
#         left_shift(n)
# elif op == 3 :
#     n = float(input("Enter how many units you want to scale : "))
#     time_scale(n)
# elif op == 4 :
#     n = int(input("Enter how many units you want to scale : "))
#     amp_scale(n)
# elif op == 5 :
#     reverse()
# else :
#     print("\n!! INVALID OPTION !!")

ori = tk.Button(text="Show Signal", fg="White", bg="Black", command=ori_sig).place(x=220, y=135)
ts = tk.Button(text="Time Shifting", height=2, width=20, bg='Light Blue', activebackground='Black',
               activeforeground='White', command=get_inp_timeshift).place(x=20, y=230)
tc = tk.Button(text="Time Scaling", height=2, width=20, bg='Light Blue', activebackground='Black',
               activeforeground='White', command = get_inp_timescale).place(x=210, y=230)
am = tk.Button(text="Amplitude Scaling", height=2, width=20, bg='Light Blue', activebackground='Black',
               activeforeground='White', command = get_inp_ampscale).place(x=20, y=300)
rv = tk.Button(text="Time Reversal", height=2, width=20, bg='Light Blue', activebackground='Black',
               activeforeground='White', command=reverse).place(x=210, y=300)
close = tk.Button(text="Close", width=6, fg="White", bg="Black", command=clo_win).place(x=320, y=135)

root.mainloop()
