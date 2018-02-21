import datetime
import random
from tkinter import *
from tkinter import simpledialog
from tkinter import messagebox
from PIL import ImageTk, Image

# Initialize variables
userBalance = 300
userBetAmount = 0
betType = 0

#determine spin results
def rouletteSpin():
    global rouletteSpinNumber
    global rouletteSpinNumberDisplay
    rouletteSpinNumber = random.randint(0, 37)
    if rouletteSpinNumber == 37:
        rouletteSpinNumberDisplay = "00"
    else:
        rouletteSpinNumberDisplay = rouletteSpinNumber
    return (rouletteSpinNumber, rouletteSpinNumberDisplay)


def oddOrEven(rouletteSpinNumber):
    if rouletteSpinNumber == 0:
        return "none"
    elif rouletteSpinNumber % 2 == 0:
        return "even"
    else:
        return "odd"


def bottomOrTopHalf(rouletteSpinNumber):
    if rouletteSpinNumber > 0 and rouletteSpinNumber <= 18:
        return "1-18"
    elif rouletteSpinNumber >= 19 and rouletteSpinNumber <= 36:
        return "19-36"

def DozenSet(rouletteSpinNumber):
    if rouletteSpinNumber > 0 and rouletteSpinNumber <= 12:
        return "1st-12"
    elif rouletteSpinNumber >= 12 and rouletteSpinNumber <= 24:
        return "2nd-12"
    elif rouletteSpinNumber >= 25 and rouletteSpinNumber <= 36:
        return "3rd-12"

def colorbet(rouletteSpinNumber):
    if rouletteSpinNumber in [1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25,
                              27, 30, 32, 34, 36]:
        return "red"
    elif rouletteSpinNumber in [2, 4, 6, 8, 10, 11, 13, 15, 17, 20, 22, 24,
                                26, 28, 29, 31, 33, 35]:
        return "black"

#results MetaData
def rouletteSpinNumberMetadata_command():
    global rouletteSpinNumberMetadata
    rouletteSpinNumberMetadata = [
        rouletteSpinNumberDisplay, oddOrEven(rouletteSpinNumber),
        bottomOrTopHalf(rouletteSpinNumber), DozenSet(rouletteSpinNumber),
        colorbet(rouletteSpinNumber)
        ]
    rouletteSpinNumberMetadataDisplay.set(rouletteSpinNumberMetadata)

    # save rouletteSpinNumberMetadata to a local file
    with open(datetime.datetime.now().strftime("%b_%Y_%d") +
        " Roulette History.txt", "a") as history:
        history.write(str(rouletteSpinNumberMetadata) + "\n")
        history.close()

    winOrLose_command()

## validate bet amount at user entry, not at betType
def validBet(userBetEntered_text):
    global userBalance
    global validBetAmount
    validBetAmount = int(userBetEntered_text.get())
    if validBetAmount > userBalance and userBalance > 0:
        messagebox.showinfo("Bad Bet Amount", "You are betting more than you have available.")
        validBetAmount=0
    else:
        userBalance = userBalance - validBetAmount
        bankBalance.set("Current Bank Balance: " + str(userBalance))
        return validBetAmount


#listbox reset
def get_selected_row(event):
    try:
        global selected_tuple
        index=list1.curselection()[0]
        selected_tuple=list1.get(index)
        e1.delete(0,END)
        e1.insert(END,selected_tuple[1])
        e2.delete(0,END)
        e2.insert(END,selected_tuple[2])
        e3.delete(0,END)
        e3.insert(END,selected_tuple[3])
        e4.delete(0,END)
        e4.insert(END,selected_tuple[4])
    except IndexError:
        pass

#view payouts button
def viewpayout_command():
    f=open("payouts.txt", "r")
    pay=f.readlines()
    messagebox.showinfo("Payouts", "\n".join(pay))

#betting buttons
def straightBet_command():
    global betType
    global userNumber
    betType = 1
    validBet(e21)
    goodLuck_text.set("A win on a single number pays 35 to 1! Good luck!!")
    userNumber = simpledialog.askstring("Mark Your Bet!", "Enter number from 0-36 or 00:")
    rouletteSpin()
    rouletteSpinNumberMetadata_command()
    return (betType,userNumber)

def odd_command():
    global betType
    global userOddOrEven
    betType = 2
    validBet(e21)
    goodLuck_text.set("Odd or even bets pay 1 to 1! Good luck!")
    userOddOrEven = "odd"
    rouletteSpin()
    rouletteSpinNumberMetadata_command()
    return (betType, userOddOrEven)

def even_command():
    global betType
    global userOddOrEven
    betType = 2
    validBet(e21)
    goodLuck_text.set("Odd or even bets pay 1 to 1! Good luck!")
    userOddOrEven = "even"
    rouletteSpin()
    rouletteSpinNumberMetadata_command()
    return (betType, userOddOrEven)

def bottomHalf_command():
    global betType
    global userBottomOrTop
    betType = 3
    validBet(e21)
    goodLuck_text.set("Bottom or Top Half bets pay 1 to 1! Good luck!")
    userBottomOrTop = "19-36"
    rouletteSpin()
    rouletteSpinNumberMetadata_command()
    return (betType, userBottomOrTop)

def topHalf_command():
    global betType
    global userBottomOrTop
    betType = 3
    validBet(e21)
    goodLuck_text.set("Bottom or Top Half bets pay 1 to 1! Good luck!")
    userBottomOrTop = "1-18"
    rouletteSpin()
    rouletteSpinNumberMetadata_command()
    return (betType, userBottomOrTop)

def oneTwelve_command():
    global betType
    global userDozenSet
    betType = 4
    validBet(e21)
    goodLuck_text.set("Dozen bets pay 2 to 1! Good luck!")
    userDozenSet = "1st-12"
    rouletteSpin()
    rouletteSpinNumberMetadata_command()
    return (betType, userDozenSet)

def thirteenTwentyFour_command():
    global betType
    global userDozenSet
    betType = 4
    validBet(e21)
    goodLuck_text.set("Dozen bets pay 2 to 1! Good luck!")
    userDozenSet = "2nd-12"
    rouletteSpin()
    rouletteSpinNumberMetadata_command()
    return (betType, userDozenSet)

def twentyFiveThirtySix_command():
    global betType
    global userDozenSet
    betType = 4
    validBet(e21)
    goodLuck_text.set("Dozen bets pay 2 to 1! Good luck!")
    userDozenSet = "3rd-12"
    rouletteSpin()
    rouletteSpinNumberMetadata_command()
    return (betType, userDozenSet)

def black_command():
    global betType
    global userColor
    betType = 5
    validBet(e21)
    goodLuck_text.set("Color bets pay 1 to 1! Good luck!")
    userColor = "black"
    rouletteSpin()
    rouletteSpinNumberMetadata_command()
    return (betType, userColor)

def red_command():
    global betType
    global userColor
    betType = 5
    validBet(e21)
    goodLuck_text.set("Color bets pay 1 to 1! Good luck!")
    userColor = "red"
    rouletteSpin()
    rouletteSpinNumberMetadata_command()
    return (betType, userColor)


# This code will compare the userNumber against the rouletteSpinNumber and determine win or lose message to user.
# The input value from the user must first be converted to an int to be able to compare numbers, else we'll see datatype error
# We use == to compare two values
def winOrLose_command():
    global userBalance
    if betType == 1:
        if userNumber in rouletteSpinNumberMetadata:
            winOrLose_text.set("You won in Straight Up single number!")
            userBalance = userBalance + int(validBetAmount) * 35
        else:
            winOrLose_text.set("You lost! Please try again!")
    elif betType == 2:
        if userOddOrEven in rouletteSpinNumberMetadata:
            winOrLose_text.set("You won Odd or Even bet!")
            userBalance = userBalance + int(validBetAmount) * 2
        else:
            winOrLose_text.set("You lost! Please try again!")
    elif betType == 3:
        if userBottomOrTop in rouletteSpinNumberMetadata:
            winOrLose_text.set("You won Bottom or Top Half!")
            userBalance = userBalance + int(validBetAmount) * 2
        else:
            winOrLose_text.set("You lost! Please try again!")
    elif betType == 4:
        if userDozenSet in rouletteSpinNumberMetadata:
            winOrLose_text.set("You won Dozen Set bet!")
            userBalance = userBalance + int(validBetAmount) * 3
        else:
            winOrLose_text.set("You lost! Please try again!")
    elif betType == 5:
        if userColor in rouletteSpinNumberMetadata:
            winOrLose_text.set("You won Color bet!")
            userBalance = userBalance + int(validBetAmount) * 2
        else:
            winOrLose_text.set("You lost! Please try again!")

    bankBalance.set("Current Bank Balance: " + str(userBalance))

## Begin GUI
window=Tk()
window.title("Roulette360")

lf1=Label(window,text="***** Welcome to Roulette360 *****", font=("Helvetica", 12), fg="orange", padx=5, pady=5)
lf1.grid(row=1, sticky=N)

path = "roulettewheel.jpg"
img = ImageTk.PhotoImage(Image.open(path))
i1 = Label(window, image = img)
i1.grid(row=2)

bankBalance = StringVar()
l11=Label(window,textvariable=bankBalance, font=("Helvetica, 11"), fg="green", padx=5, pady=5)
l11.grid(row=4, sticky=W)

lf2=LabelFrame(window,text="Place Your Bet!", padx=5, pady=5)
lf2.grid(row=5, columnspan=3, sticky=W)

l21=Label(lf2,text="Bet Amount: ", font=("Helvetica, 10"), fg="orange")
l21.grid(row=5, column=1)

userBetEntered_text=IntVar()
e21=Entry(lf2,textvariable=userBetEntered_text, width=3)
e21.grid(row=5,column=2)

l22=Label(lf2, text=" ", font=("Helvetica, 8"), fg="green", padx=5, pady=5)
l22.grid(row=6, column=1)

b0=Button(window,text="View Payouts", font=("Helvetica, 8"), fg="green", command=viewpayout_command)
b0.grid(row=4, column=2)

b1=Button(lf2,text="Straight Bet", command=straightBet_command, bg="green", fg="white", padx=1, pady=1)
b1.grid(row=7, column=1)

b2=Button(lf2,text="Odd", command=odd_command, padx=1, pady=1)
b2.grid(row=10, column=5)

b3=Button(lf2,text="Even", command=even_command, padx=1, pady=1)
b3.grid(row=10, column=2)

b4=Button(lf2,text="19 to 36", command=bottomHalf_command, padx=1, pady=1)
b4.grid(row=10, column=6)

b5=Button(lf2,text="1 to 18", command=topHalf_command, padx=1, pady=1)
b5.grid(row=10, column=1)

b6=Button(lf2,text="1st 12", command=oneTwelve_command, padx=1, pady=1)
b6.grid(row=9, column=2)

b7=Button(lf2,text="2nd 12", command=thirteenTwentyFour_command, padx=1, pady=1)
b7.grid(row=9, column=3)

b8=Button(lf2,text="3rd 12", command=twentyFiveThirtySix_command, padx=1, pady=1)
b8.grid(row=9, column=4)

b9=Button(lf2,text="Black", command=black_command, bg="black", fg="white", padx=1, pady=1)
b9.grid(row=10, column=3)

b10=Button(lf2,text="Red", command=red_command, bg="red", fg="white", padx=1, pady=1)
b10.grid(row=10, column=4)

lf3=LabelFrame(window, text="Spin Results", height=1300, width=1300, padx=5, pady=5)
lf3.grid(row=2, column=2)

rouletteSpinNumberMetadataDisplay = StringVar()
l3=Label(lf3, textvariable=rouletteSpinNumberMetadataDisplay, fg="blue")
l3.grid(row=2)

t1=LabelFrame(window, text="Test Prints Here")
t1.grid(row=12, sticky=W)

test_Text=StringVar()
t2=Label(t1, textvariable=test_Text, fg="red")
t2.grid(row=13, column=1)

goodLuck_text=StringVar()
gl1=Label(window, textvariable=goodLuck_text)
gl1.grid(row=2, column=0)

winOrLose_text=StringVar()
t2=Label(window, textvariable=winOrLose_text)
t2.grid(row=16, column=1)

test_Text.set("Window is Ready. Current Bet: " + str(userBetAmount))
bankBalance.set("Current Bank Balance: " + str(userBalance))

window.mainloop()
##End GUI
