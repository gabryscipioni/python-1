import math
from tkinter import *


#Finestra
window = Tk()
window.title("Gestione Tavoli")
root = Tk()
root.geometry("300x300")
#window.geometry("1920x1080")
window.resizable(True, True)
window.config(background = "#2e2c2c")
window.scrollbar.pack(side=Tk.RIGHT, fill=Tk.Y)
scrollbar = Scrollbar(root)
scrollbar.pack(side=RIGHT, fill=Y)

mylist = Listbox(root, yscrollcommand=scrollbar.set)
for i in range(100):
    mylist.insert(END, f"Item {i}")
mylist.pack(side=LEFT, fill=BOTH)



Pl1, S1 = False, False
hours1, minutes1, seconds1, euro1, cent1 = 0, 0, 0, 0, 0

Pl2, S2 = False, False
hours2, minutes2, seconds2, euro2, cent2 = 0, 0, 0, 0, 0

Pl3, S3 = False, False
hours3, minutes3, seconds3, euro3, cent3 = 0, 0, 0, 0, 0

Pl4, S4 = False, False
hours4, minutes4, seconds4, euro4, cent4 = 0, 0, 0, 0, 0

Pl5, S5 = False, False
hours5, minutes5, seconds5, euro5, cent5 = 0, 0, 0, 0, 0

#Widget
Cronometro_1 = Label(window, text=" Tavolo 1  = ", font=("Microsoft Yahei", 50), bg="#2e2c2c", fg="green")
Cronometro_1.grid(row=0, column=0, padx = 5, pady = 5)

Cronometro_2 = Label(window, text=" Tavolo 2  = ", font=("Microsoft Yahei", 50), bg="#2e2c2c", fg="green")
Cronometro_2.grid(row=1, column=0, padx = 5, pady = 5)

Cronometro_3 = Label(window, text=" Tavolo 3  = ", font=("Microsoft Yahei", 50), bg="#2e2c2c", fg="green")
Cronometro_3.grid(row=2, column=0, padx = 5, pady = 5)

Cronometro_4 = Label(window, text=" Tavolo 4  = ", font=("Microsoft Yahei", 50), bg="#2e2c2c", fg="green")
Cronometro_4.grid(row=3, column=0, padx = 5, pady = 5)

Cronometro_5 = Label(window, text=" Tavolo 5 = ", font=("Microsoft Yahei", 50), bg="#2e2c2c", fg="green")
Cronometro_5.grid(row=4, column=0, padx = 5, pady = 5)

Time_1 = Label(window, text = "00:00:00", font=("Microsoft Yahei", 50), bg="#2e2c2c", fg="white")
Time_1.grid(row=0, column=1, padx = 10, pady = 50)

Saldo_1 = Label(window, text = "€ 00,00", font=("Microsoft Yahei", 50), bg="#2e2c2c", fg="white")
Saldo_1.grid(row=0, column=2, padx = 10, pady = 50)

Time_2 = Label(window, text = "00:00:00", font=("Microsoft Yahei", 50), bg="#2e2c2c", fg="white")
Time_2.grid(row=1, column=1, padx = 10, pady = 50)

Saldo_2 = Label(window, text = "€ 00,00", font=("Microsoft Yahei", 50), bg="#2e2c2c", fg="white")
Saldo_2.grid(row=1, column=2, padx = 10, pady = 50)

Time_3 = Label(window, text = "00:00:00", font=("Microsoft Yahei", 50), bg="#2e2c2c", fg="white")
Time_3.grid(row=2, column=1, padx = 10, pady = 50)

Saldo_3 = Label(window, text = "€ 00,00", font=("Microsoft Yahei", 50), bg="#2e2c2c", fg="white")
Saldo_3.grid(row=2, column=2, padx = 10, pady = 50)

Time_4 = Label(window, text = "00:00:00", font=("Microsoft Yahei", 50), bg="#2e2c2c", fg="white")
Time_4.grid(row=3, column=1, padx = 10, pady = 50)

Saldo_4 = Label(window, text = "€ 00,00", font=("Microsoft Yahei", 50), bg="#2e2c2c", fg="white")
Saldo_4.grid(row=3, column=2, padx = 10, pady = 50)

Time_5 = Label(window, text = "00:00:00", font=("Microsoft Yahei", 50), bg="#2e2c2c", fg="white")
Time_5.grid(row=4, column=1, padx = 10, pady = 50)

Saldo_5 = Label(window, text = "€ 00,00", font=("Microsoft Yahei", 50), bg="#2e2c2c", fg="white")
Saldo_5.grid(row=4, column=2, padx = 10, pady = 50)

def new_func(window):
    listbox = Tk.Listbox(window, yscrollcommand=scrollbar.set)

new_func(window)

#Funzioni 1
def Play1():
    global S1, Pl1, hours1, minutes1, seconds1, euro1, cent1
    if S1:
        hours1, minutes1, seconds1, euro1, cent1 = 0, 0, 0, 0, 0
    if not Pl1:
        update1()
        Pl1 = True
    S1 = False

def Pause1():
    global Pl1
    if Pl1:
        Time_1.after_cancel(update_time1)
        Pl1 = False

def Stop1():
    global S1
    if S1:
        Time_1.config(text='00:00:00', fg="white")
        Saldo_1.config(text='€ 00,00', fg="white")
    S1 = True
    Pause1()

def update1():
    global hours1, minutes1, seconds1, euro1, cent1
    seconds1 += 1
    cent1 += 0.27777777778
    if cent1 == 100:
        cent1 = 0
        euro1 += 1
    if seconds1 == 60:
        minutes1 += 1
        seconds1 = 0
    if minutes1 == 60:
        hours1 += 1
        minutes1 = 0

    hours_string = f'{hours1}' if hours1 > 9 else f'0{hours1}'
    minutes_string = f'{minutes1}' if minutes1 > 9 else f'0{minutes1}'
    seconds_string = f'{seconds1}' if seconds1 > 9 else f'0{seconds1}'

    euro_string = f'{euro1}' if euro1 > 9 else f'0{euro1}'
    cent_string = f'{math.trunc(cent1)}' if cent1 > 9 else f'0{math.trunc(cent1)}'

    if(hours1 < 1 or seconds1 % 2 != 0):
        Time_1.config(text=hours_string + ':' + minutes_string + ':' + seconds_string, fg = "white")
        Saldo_1.config(text= '€ ' + euro_string + ',' + cent_string, fg = "white")
    
    else:
        Time_1.config(text=hours_string + ':' + minutes_string + ':' + seconds_string, fg = "red")
        Saldo_1.config(text= '€ ' + euro_string + ',' + cent_string, fg = "red")

    global update_time1
    update_time1 = Time_1.after(1000, update1)

#Funzioni 2
def Play2():
    global S2, Pl2, hours2, minutes2, seconds2, euro2, cent2
    if S2:
        hours2, minutes2, seconds2, euro2, cent2 = 0, 0, 0, 0, 0
    if not Pl2:
        update2()
        Pl2 = True
    S2 = False

def Pause2():
    global Pl2
    if Pl2:
        Time_2.after_cancel(update_time2)
        Pl2 = False

def Stop2():
    global S2
    if S2:
        Time_2.config(text='00:00:00', fg="white")
        Saldo_2.config(text='€ 00,00', fg="white")
    S2 = True
    Pause2()

def update2():
    global hours2, minutes2, seconds2, euro2, cent2
    seconds2 += 1
    cent2 += 1
    if cent2 == 100:
        cent2 = 0
        euro2 += 1
    if seconds2 == 60:
        minutes2 += 1
        seconds2 = 0
    if minutes2 == 60:
        hours2 += 1
        minutes2 = 0

    hours_string = f'{hours2}' if hours2 > 9 else f'0{hours2}'
    minutes_string = f'{minutes2}' if minutes2 > 9 else f'0{minutes2}'
    seconds_string = f'{seconds2}' if seconds2 > 9 else f'0{seconds2}'

    euro_string = f'{euro2}' if euro2 > 9 else f'0{euro2}'
    cent_string = f'{round(cent2, 1)}' if cent2 > 9 else f'0{round(cent2, 1)}'

    if(hours2 < 1 or seconds2 % 2 != 0):
        Time_2.config(text=hours_string + ':' + minutes_string + ':' + seconds_string, fg = "white")
        Saldo_2.config(text= '€ ' + euro_string + ',' + cent_string, fg = "white")
    
    else:
        Time_2.config(text=hours_string + ':' + minutes_string + ':' + seconds_string, fg = "red")
        Saldo_2.config(text= '€ ' + euro_string + ',' + cent_string, fg = "red")

    global update_time2
    update_time2 = Time_2.after(1000, update2)

#Funzioni 3
def Play3():
    global S3, Pl3, hours3, minutes3, seconds3, euro3, cent3
    if S3:
        hours3, minutes3, seconds3, euro3, cent3 = 0, 0, 0, 0, 0
    if not Pl3:
        update3()
        Pl3 = True
    S3 = False

def Pause3():
    global Pl3
    if Pl3:
        Time_3.after_cancel(update_time3)
        Pl3 = False

def Stop3():
    global S3
    if S3:
        Time_3.config(text='00:00:00', fg="white")
        Saldo_3.config(text='€ 00,00', fg="white")
    S3 = True
    Pause3()

def update3():
    global hours3, minutes3, seconds3, euro3, cent3
    seconds3 += 1
    cent3 += 1
    if cent3 == 100:
        cent3 = 0
        euro3 += 1
    if seconds3 == 60:
        minutes3 += 1
        seconds3 = 0
    if minutes3 == 60:
        hours3 += 1
        minutes3 = 0
    
    hours_string = f'{hours3}' if hours3 > 9 else f'0{hours3}'
    minutes_string = f'{minutes3}' if minutes3 > 9 else f'0{minutes3}'
    seconds_string = f'{seconds3}' if seconds3 > 9 else f'0{seconds3}'

    euro_string = f'{euro3}' if euro3 > 9 else f'0{euro3}'
    cent_string = f'{round(cent3, 1)}' if cent3 > 9 else f'0{round(cent3, 1)}'
    
    if(hours3 < 1 or seconds3 % 2 != 0):
        Time_3.config(text=hours_string + ':' + minutes_string + ':' + seconds_string, fg = "white")
        Saldo_3.config(text= '€ ' + euro_string + ',' + cent_string, fg = "white")
    
    else:
        Time_3.config(text=hours_string + ':' + minutes_string + ':' + seconds_string, fg = "red")
        Saldo_3.config(text= '€ ' + euro_string + ',' + cent_string, fg = "red")

    global update_time3
    update_time3 = Time_3.after(1000, update3)

#Funzioni 4
def Play4():
    global S4, Pl4, hours4, minutes4, seconds4, euro4, cent4
    if S4:
        hours4, minutes4, seconds4, euro4, cent4 = 0, 0, 0, 0, 0
    if not Pl4:
        update4()
        Pl4 = True
    S4 = False

def Pause4():
    global Pl4
    if Pl4:
        Time_4.after_cancel(update_time4)
        Pl4 = False

def Stop4():
    global S4
    if S4:
        Time_4.config(text='00:00:00', fg="white")
        Saldo_4.config(text='€ 00,00', fg="white")
    S4 = True
    Pause4()

def update4():
    global hours4, minutes4, seconds4, euro4, cent4
    seconds4 += 1
    cent4 += 1
    if cent4 == 100:
        cent4 = 0
        euro4 += 1
    if seconds4 == 60:
        minutes4 += 1
        seconds4 = 0
    if minutes4 == 60:
        hours4 += 1
        minutes4 = 0
    hours_string = f'{hours4}' if hours4 > 9 else f'0{hours4}'
    minutes_string = f'{minutes4}' if minutes4 > 9 else f'0{minutes4}'
    seconds_string = f'{seconds4}' if seconds4 > 9 else f'0{seconds4}'

    euro_string = f'{euro4}' if euro4 > 9 else f'0{euro4}'
    cent_string = f'{round(cent4, 1)}' if cent4 > 9 else f'0{round(cent4, 1)}'
    
    if(hours4 < 1 or seconds4 % 2 != 0):
        Time_4.config(text=hours_string + ':' + minutes_string + ':' + seconds_string, fg = "white")
        Saldo_4.config(text= '€ ' + euro_string + ',' + cent_string, fg = "white")
    
    else:
        Time_4.config(text=hours_string + ':' + minutes_string + ':' + seconds_string, fg = "red")
        Saldo_4.config(text= '€ ' + euro_string + ',' + cent_string, fg = "red")

    global update_time4
    update_time4 = Time_4.after(1000, update4)

#Funzioni 5
def Play5():
    global S5, Pl5, hours5, minutes5, seconds5, euro5, cent5
    if S5:
        hours5, minutes5, seconds5, euro5, cent5 = 0, 0, 0, 0, 0
    if not Pl5:
        update5()
        Pl5 = True
    S5 = False

def Pause5():
    global Pl5
    if Pl5:
        Time_5.after_cancel(update_time5)
        Pl5 = False

def Stop5():
    global S5
    if S5:
        Time_5.config(text='00:00:00', fg="white")
        Saldo_5.config(text='€ 00,00', fg="white")
    S5 = True
    Pause5()

def update5():
    global hours5, minutes5, seconds5, euro5, cent5
    seconds5 += 1
    cent5 += 1
    if cent5 == 100:
        cent5 = 0
        euro5 += 1
    if seconds5 == 60:
        minutes5 += 1
        seconds5 = 0
    if minutes5 == 60:
        hours5 += 1
        minutes5 = 0
    hours_string = f'{hours5}' if hours5 > 9 else f'0{hours5}'
    minutes_string = f'{minutes5}' if minutes5 > 9 else f'0{minutes5}'
    seconds_string = f'{seconds5}' if seconds5 > 9 else f'0{seconds5}'

    euro_string = f'{euro5}' if euro5 > 9 else f'0{euro5}'
    cent_string = f'{round(cent5, 1)}' if cent5 > 9 else f'0{round(cent5, 1)}'
    
    if(hours5 < 1 or seconds5 % 2 != 0):
        Time_5.config(text=hours_string + ':' + minutes_string + ':' + seconds_string, fg = "white")
        Saldo_5.config(text= '€ ' + euro_string + ',' + cent_string, fg = "white")
    
    else:
        Time_5.config(text=hours_string + ':' + minutes_string + ':' + seconds_string, fg = "red")
        Saldo_5.config(text= '€ ' + euro_string + ',' + cent_string, fg = "red")

    global update_time5
    update_time5 = Time_5.after(1000, update5)

#Bottoni
Play_1 = Button(window, text="Play", font=("Microsoft Yahei", 16), bg="#ff8000", fg="black", bd=3, width = 5, command = Play1)
Play_1.place(x = 770, y = 70)

Pause_1 = Button(window, text="Pause", font=("Microsoft Yahei", 16), bg="#ff8000", fg="black", bd=3, width = 5, command = Pause1)
Pause_1.place(x = 870, y = 70)

Stop_1 = Button(window, text="Stop", font=("Microsoft Yahei", 16), bg="#ff8000", fg="black", bd=3, width = 5, command = Stop1)
Stop_1.place(x = 970, y = 70)

Play_2 = Button(window, text="Play", font=("Microsoft Yahei", 16), bg="#ff8000", fg="black", bd=3, width = 5, command = Play2)
Play_2.place(x = 770, y = 233)

Pause_2 = Button(window, text="Pause", font=("Microsoft Yahei", 16), bg="#ff8000", fg="black", bd=3, width = 5, command = Pause2)
Pause_2.place(x = 870, y = 233)

Stop_2 = Button(window, text="Stop", font=("Microsoft Yahei", 16), bg="#ff8000", fg="black", bd=3, width = 5, command = Stop2)
Stop_2.place(x = 970, y = 233)

Play_3 = Button(window, text="Play", font=("Microsoft Yahei", 16), bg="#ff8000", fg="black", bd=3, width = 5, command = Play3)
Play_3.place(x = 770, y = 398)

Pause_3 = Button(window, text="Pause", font=("Microsoft Yahei", 16), bg="#ff8000", fg="black", bd=3, width = 5, command = Pause3)
Pause_3.place(x = 870, y = 398)

Stop_3 = Button(window, text="Stop", font=("Microsoft Yahei", 16), bg="#ff8000", fg="black", bd=3, width = 5, command = Stop3)
Stop_3.place(x = 970, y = 398)

Play_4 = Button(window, text="Play", font=("Microsoft Yahei", 16), bg="#ff8000", fg="black", bd=3, width = 5, command = Play4)
Play_4.place(x = 770, y = 561)

Pause_4 = Button(window, text="Pause", font=("Microsoft Yahei", 16), bg="#ff8000", fg="black", bd=3, width = 5, command = Pause4)
Pause_4.place(x = 870, y = 561)

Stop_4 = Button(window, text="Stop", font=("Microsoft Yahei", 16), bg="#ff8000", fg="black", bd=3, width = 5, command = Stop4)
Stop_4.place(x = 970, y = 561)

Play_5 = Button(window, text="Play", font=("Microsoft Yahei", 16), bg="#ff8000", fg="black", bd=3, width = 5, command = Play5)
Play_5.place(x = 770, y = 727)

Pause_5 = Button(window, text="Pause", font=("Microsoft Yahei", 16), bg="#ff8000", fg="black", bd=3, width = 5, command = Pause5)
Pause_5.place(x = 870, y = 727)

Stop_5 = Button(window, text="Stop", font=("Microsoft Yahei", 16), bg="#ff8000", fg="black", bd=3, width = 5, command = Stop5)
Stop_5.place(x = 970, y = 727)


window.mainloop()
scrollbar.config(command=mylist.yview)

root.mainloop()