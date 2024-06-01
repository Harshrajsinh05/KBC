from tkinter import *
from tkinter.ttk import Progressbar
import threading
import time
import random

audianceFrame = None

class MyThread(threading.Thread):
    global flag 
    flag = False
    def __init__(self, start, end):
        super().__init__()
        self.start_count = start
        self.end_count = end
        self.running = True

    def run(self):
        global c 
        c = self.end_count
        while c >= self.start_count and self.running:
            timeLabel = Label(mainFrame,height=1,width=3,text=c, font=('arial',50, 'bold'),bg="#2d3548", fg='white') 
            timeLabel.place(x=580,y=155)
            c -= 1
            # print(c)
            time.sleep(1)
        if(c==0):
            lossframe = Frame(root, height=root.winfo_screenheight(), width=root.winfo_screenwidth(), bg="#1e2633")
            lossframe.place(x=0, y=0)

            lossText = Text(lossframe, font=('arial', 17, 'bold'), height=2, bg='#1e2633', fg='white', width=70, wrap='word', bd=0)
            lossText.insert(END, """                        TIME IS FINISHED TRY AGAIN LATER""")
            lossText.place(relx=0.5, rely=0.5, anchor='center')
            
            quit_button = Button(lossframe, text="Quit", font=('arial', 14, 'bold'), bg='#1e2633', fg='white',height=2,width=20, command=quit_game)
            quit_button.place(relx=0.5, rely=0.6, anchor='center')

    def stop(self):
        self.running = False
    
def stop_thread():
    my_thread.stop()
    my_thread.join()  # Wait for the thread to finish


def play_thread(end):
    global my_thread
    my_thread = MyThread(1,end)
    my_thread.start()

def givetime(th):
    time.sleep(3)
q=''
winning=1

def play():
    root.config(bg='#1e2633')
    button.destroy()
    global mainFrame
    mainFrame = Frame(root, height=root.winfo_screenheight(), width=root.winfo_screenwidth())
    mainFrame.pack()
    mainbackground = Label(mainFrame, image=mainbackgroundphoto, height=710, width=1270)
    mainbackground.pack()

    global que, optionA, optionB, optionC, optionD, prizelabel,audiancepolebutton,half_halfbutton,doublebutton,switchbutton

    prizelabel = Label(root, image=prizephoto, bg="#1e2633")
    prizelabel.place(x=root.winfo_screenwidth()-141, y=0)


    
    audiancepolebutton = Button(mainFrame, image=audianceploephoto, bg='#1e2633', bd=0, activebackground='#1e2633',command=plotgraph)
    audiancepolebutton.place(x=427, y=350)

    half_halfbutton = Button(mainFrame, image=half_halfphoto, bg='#1e2633', bd=0, activebackground='#1e2633',command=half_halflifeline)
    half_halfbutton.place(x=557, y=350)

    doublebutton = Button(mainFrame, image=doublephoto, bg='#1e2633', bd=0, activebackground='#1e2633',command=doubletime)
    doublebutton.place(x=687, y=350)

    switchbutton = Button(mainFrame, image=switcharrowphoto, bg='#1e2633', bd=0, activebackground='#1e2633',command=changeQue)
    switchbutton.place(x=817, y=350)

    que = Text(mainFrame, font=('arial', 17, 'bold'), height=2, bg='#1e2633', fg='white', width=63, wrap='word', bd=0)
    que.place(x=227, y=410)

    que.insert(END, q)
    que.configure(state='disabled')

    optionALabel = Label(mainFrame,text="A:",height=1,width=1,bg="#1e2633",fg="white")
    optionALabel.place(x=210,y=557)
    
    optionBLabel = Label(mainFrame,text="B:",height=1,width=1,bg="#1e2633",fg="white")
    optionBLabel.place(x=673,y=557)
    
    optionCLabel = Label(mainFrame,text="C:",height=1,width=1,bg="#1e2633",fg="white")
    optionCLabel.place(x=210,y=627)
    
    optionDLabel = Label(mainFrame,text="D:",height=1,width=1,bg="#1e2633",fg="white")
    optionDLabel.place(x=673,y=627)

    optionA = Button(mainFrame, text=QNOP_dic[q][0], height=2, width=51, bg='#1e2633', activebackground='#1e2633', cursor="hand2", fg='white', activeforeground="white",bd=0)
    optionA.place(x=227, y=550)

    optionB = Button(mainFrame, text=QNOP_dic[q][1], height=2, width=51, bg='#1e2633', activebackground='#1e2633', cursor="hand2", fg='white', activeforeground="white", bd=0)
    optionB.place(x=690, y=550)

    optionC = Button(mainFrame, text=QNOP_dic[q][2], height=2, width=51, bg='#1e2633', activebackground='#1e2633', cursor="hand2", fg='white', activeforeground="white", bd=0)
    optionC.place(x=227, y=620)

    optionD = Button(mainFrame, text=QNOP_dic[q][3], height=2, width=51, bg='#1e2633', activebackground='#1e2633', cursor="hand2", fg='white', activeforeground="white", bd=0)
    optionD.place(x=690, y=620)

    optionA.bind('<Button-1>', selectOption)
    optionB.bind('<Button-1>', selectOption)
    optionC.bind('<Button-1>', selectOption)
    optionD.bind('<Button-1>', selectOption)

    
    play_thread(30)



def half_halflifeline():
    half_halfbutton.config(image=disablehalf_halfphoto,state=DISABLED)
    if(QNOP_dic[q][0]==QNA_dic[q]):
        optionB.config(text="")
        optionC.config(text="")
    elif(QNOP_dic[q][1]==QNA_dic[q]):
        optionA.config(text="")
        optionD.config(text="")
        
    elif(QNOP_dic[q][2]==QNA_dic[q]):
        optionA.config(text="")
        optionD.config(text="")
        
    elif(QNOP_dic[q][3]==QNA_dic[q]):
        optionA.config(text="")
        optionB.config(text="")
    
def changeQue():
    switchbutton.config(image=disableswitcharrowphoto,state=DISABLED)
    global q
    QNA_dic.pop(q)
    QNOP_dic.pop(q)
    q = random.choice(list(QNA_dic.keys()))

    que.config(state='normal')
    que.delete(1.0, END)
    que.insert(END, q)
    que.config(state='disabled')

    optionA.config(text=QNOP_dic[q][0])
    optionB.config(text=QNOP_dic[q][1])
    optionC.config(text=QNOP_dic[q][2])
    optionD.config(text=QNOP_dic[q][3])

def doubletime():
    doublebutton.config(image=disabledoublephoto,state=DISABLED)
    
    stop_thread()
    if(winning>5 and winning<=10):
        play_thread(c+90)
    elif(winning>10):
        play_thread(c+60)
    else:
        play_thread(c+30)

def plotgraph():


    audiancepolebutton.config(image=disabledaudiancepole,state=DISABLED)
    global audianceFrame
    audianceFrame = Frame(mainFrame,height=200,width=142,bg="#1e2633")
    audianceFrame.place(x=0,y=30)

    progressbarA = Progressbar(audianceFrame,orient=VERTICAL,length=160)
    progressbarA.place(x=0,y=0)
    progressbarALabel = Label(audianceFrame,text="A",font=('arial',19,'bold'),bg="#1e2633")
    progressbarALabel.place(x=0,y=170)

    progressbarB = Progressbar(audianceFrame,orient=VERTICAL,length=160)
    progressbarB.place(x=40,y=0)
    progressbarBLabel = Label(audianceFrame,text="B",font=('arial',19,'bold'),bg="#1e2633")
    progressbarBLabel.place(x=40,y=170)

    progressbarC = Progressbar(audianceFrame,orient=VERTICAL,length=160)
    progressbarC.place(x=80,y=0)
    progressbarCLabel = Label(audianceFrame,text="C",font=('arial',19,'bold'),bg="#1e2633")
    progressbarCLabel.place(x=80,y=170)

    progressbarD = Progressbar(audianceFrame,orient=VERTICAL,length=160)
    progressbarD.place(x=120,y=0)
    progressbarDLabel = Label(audianceFrame,text="D",font=('arial',19,'bold'),bg="#1e2633")
    progressbarDLabel.place(x=120,y=170)

    if(QNOP_dic[q][0]==QNA_dic[q]):
        progressbarA.config(value=80)
        progressbarB.config(value=20)
        progressbarC.config(value=50)
        progressbarD.config(value=10)
    
    elif(QNOP_dic[q][1]==QNA_dic[q]):
        progressbarA.config(value=20)
        progressbarB.config(value=80)
        progressbarC.config(value=50)
        progressbarD.config(value=10)
        
    elif(QNOP_dic[q][2]==QNA_dic[q]):
        progressbarA.config(value=50)
        progressbarB.config(value=20)
        progressbarC.config(value=80)
        progressbarD.config(value=10)
        
    elif(QNOP_dic[q][3]==QNA_dic[q]):
        progressbarA.config(value=10)
        progressbarB.config(value=20)
        progressbarC.config(value=50)
        progressbarD.config(value=80)
        
def quit_game():
    root.destroy()  # Destroy the root window, effectively quitting the application
    my_thread.stop()

def selectOption(event):
    global q, winning, prizelabel
    
    if audianceFrame != None:
        audianceFrame.destroy()

    b = event.widget
    value = b['text']
    if(winning==15):
        winframe = Frame(root, height=root.winfo_screenheight(), width=root.winfo_screenwidth(), bg="#1e2633")
        winframe.place(x=0, y=0)


        winText = Text(winframe, font=('arial', 17, 'bold'), height=2, bg='#1e2633', fg='white', width=70, wrap='word', bd=0)
        winText.insert(END, """                  CONGRATULATIONS YOU WAN THE GAME """)
        winText.place(relx=0.5, rely=0.5, anchor='center')

        quit_button = Button(winframe, text="Quit", font=('arial', 14, 'bold'), bg='#1e2633', fg='white',height=2,width=20, command=quit_game)
        quit_button.place(relx=0.5, rely=0.6, anchor='center')

    elif (value == QNA_dic[q]):
        QNA_dic.pop(q)
        QNOP_dic.pop(q)
        winning+=1
        q = random.choice(list(QNA_dic.keys()))

        que.config(state='normal')
        que.delete(1.0, END)
        que.insert(END, q)
        que.config(state='disabled')

        optionA.config(text=QNOP_dic[q][0])
        optionB.config(text=QNOP_dic[q][1])
        optionC.config(text=QNOP_dic[q][2])
        optionD.config(text=QNOP_dic[q][3])

        prizepath = 'que' + str(winning) + '.png'
        nprizephoto = PhotoImage(file=prizepath)
        prizelabel.config(image=nprizephoto, bg="#1e2633")
        prizelabel.image = nprizephoto
        
        stop_thread()

        global my_thread
        my_thread_1 = threading.Thread(target=givetime)
        my_thread_1.start()
        my_thread_1.join()

        if(winning>5 and winning<=10):
            play_thread(60)
        elif(winning>10):
            play_thread(90)
        else:
            play_thread(30)
    else:
        lossframe = Frame(root, height=root.winfo_screenheight(), width=root.winfo_screenwidth(), bg="#1e2633")
        lossframe.place(x=0, y=0)


        lossText = Text(lossframe, font=('arial', 17, 'bold'), height=2, bg='#1e2633', fg='white', width=70, wrap='word', bd=0)
        lossText.insert(END, "YOU LOSS THE GAME CORRECT OPTION WAS " + QNA_dic[q])
        lossText.place(relx=0.5, rely=0.5, anchor='center')

        quit_button = Button(lossframe, text="Quit", font=('arial', 14, 'bold'), bg='#1e2633', fg='white',height=2,width=20, command=quit_game)
        quit_button.place(relx=0.5, rely=0.6, anchor='center')

QNOP_dic = {}
QNA_dic = {}


def mkdirQ():
    f = open('QNA.txt', "r")
    i = 0
    arr = f.readlines()
    print(arr)
    while(i <= len(arr)-5):
        QNOP_dic[arr[i][:-1]] = [arr[i+1][:-1], arr[i+2][:-1], arr[i+3][:-1], arr[i+4][:-1]]
        QNA_dic[arr[i][:-1]] = arr[i+5][:-1]
        i += 6

root = Tk()
root.geometry('{0}x{1}+1+1'.format(root.winfo_screenwidth(), root.winfo_screenheight()))
root.overrideredirect(1) 
root.config(bg='#1e2633')
root.title("Quiz Application")

audianceploephoto = PhotoImage(file='asktheaudience.png')
half_halfphoto = PhotoImage(file='50-50.png')
doublephoto = PhotoImage(file='doubletime.png')
disabledoublephoto = PhotoImage(file='doubletime_c.png')
switcharrowphoto = PhotoImage(file='switcharoo.png')
disableswitcharrowphoto = PhotoImage(file='switcharoo_c.png')
mainbackgroundphoto = PhotoImage(file='background.png')
prizephoto = PhotoImage(file='que1.png')
disabledaudiancepole = PhotoImage(file='asktheaudience_c.png')
disablehalf_halfphoto = PhotoImage(file='50-50_c.png')

mkdirQ()
q = random.choice(list(QNA_dic.keys()))

button = Button(root,activeforeground="white", text="START MATCH", font=("Helvetica", 32),background="#000000",activebackground="#000000",fg="white", command=play,bd=0)

button_width = button.winfo_reqwidth()
button_height = button.winfo_reqheight()
button.place(relx=0.5, rely=0.5, anchor='center', width=button_width, height=button_height)

root.mainloop()
