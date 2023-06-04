from bj import *
from tkinter import *
from tkinter import messagebox as m
import math


def chicha():
    return 0


root = Tk()
root.geometry("1000x750")
root.resizable(height=False, width=False)
background = PhotoImage(file=r"images/background.png")
temp = Label(root, width=1000, height=750, image=background)
temp.grid(row=0, column=0, rowspan=3)
frame_dealer = Frame(root, relief="groove", width=1000, height=100)
frame_dealer.grid(row=0, column=0,sticky="S")
root.rowconfigure(0, weight=20)
frame_player = Frame(root, relief="groove", width=196, height=250, bg="#00B343")
frame_player.grid(row=1, column=0)
root.rowconfigure(1, weight=10)
frame_buttons = Frame(root, relief="groove", width=1000, height=14, bg="#00B343")
frame_buttons.grid(row=2, column=0, sticky="WES")
root.rowconfigure(2, weight=1)
frame_of_dealer_cards = Frame(frame_dealer, bg="green")
frame_of_dealer_cards.grid(row=1, column=0, columnspan=3)
button_split = Button(frame_buttons, text="SPLIT", font="Arial 14", width=22, bg="limegreen", command=chicha)
button_split.grid(row=0, column=0, sticky="WES")
button_double = Button(frame_buttons, text="DOUBLE", font="Arial 14", width=22, bg="limegreen", command=chicha)
button_double.grid(row=0, column=1, sticky="WES")
button_hit = Button(frame_buttons, text="HIT", font="Arial 14", width=22, bg="limegreen", command=chicha)
button_hit.grid(row=0, column=2, sticky="S")
button_hold = Button(frame_buttons, text="HOLD", font="Arial 14", width=22, bg="limegreen", command=chicha)
button_hold.grid(row=0, column=3, sticky="WES")
# player_hands = Label(frame_player, text="Hands of player")
# player_hands.grid(row=0, column=1)
# k="images/clubs/2.png"
# k = PhotoImage(file=r"images/clubs/2.png")
# Label(frame_player, image=k).grid(row=0, column=0, columnspan=2, sticky="WE")
# st="images\\clubs"+"\\3"+".png"
# temp0 = PhotoImage(file=st)
# k=Label(frame_player, image=temp0)
# k.grid(row=0, column=1, sticky="WE")
generate_deck()
hands.append(Hand(1, 0, 0))
canvas_hand1 = Canvas(frame_player, relief="groove", width=196, height=250, bg="#00B343", borderwidth=0)
canvas_hand1.grid(row=0, column=0, padx=5)
for i in deck:
    # if i.card_suit.eq("clubs"):
    hands[0].cards_in_hand.append(i)
# labels = []
# for i in range(len(hands[0].cards_in_hand)):
#     labels.append(Label(frame_player, image=hands[0].cards_in_hand[i].photo, bg="black"))
# for i in range(len(hands[0].cards_in_hand)):
#     labels[i].grid(row=0, column=i, columnspan=5, sticky="WE")
m.showinfo(message="sljdnf")
# labels = []
# for i in range(len(hands[0].cards_in_hand)):
#     labels.append(Label(frame_dealer, image=hands[0].cards_in_hand[i].photo, bg="black"))
for i in range(12):
    # Frame(frame_dealer, width=27, height=0, bg="#00B343").grid(row=1, column=i)
    # labels[i].grid(row=0, column=i, columnspan=2, sticky="WE")
    # labels[i].place(x=0 + 30 * i, y=0)
    m.showinfo(message="sljdnf")
    z = math.floor((i) / 4)
    canvas_hand1.create_image(40 + 40 * (i - 4 * z), 50 + 75 * z, image=hands[0].cards_in_hand[i].photo)
canvas_hand2 = Canvas(frame_player, relief="groove", width=196, height=250, bg="#00B343", borderwidth=0)
canvas_hand2.grid(row=0, column=1, padx=5)
for i in range(12):
    # Frame(frame_dealer, width=27, height=0, bg="#00B343").grid(row=1, column=i)
    # labels[i].grid(row=0, column=i, columnspan=2, sticky="WE")
    # labels[i].place(x=0 + 30 * i, y=0)
    m.showinfo(message="sljdnf")
    z = math.floor((i) / 4)
    canvas_hand2.create_image(40 + 40 * (i - 4 * z), 50 + 75 * z, image=hands[0].cards_in_hand[i].photo)
canvas_hand3 = Canvas(frame_player, relief="groove", width=196, height=250, bg="#00B343", borderwidth=0)
canvas_hand3.grid(row=0, column=2, padx=5)
for i in range(12):
    # Frame(frame_dealer, width=27, height=0, bg="#00B343").grid(row=1, column=i)
    # labels[i].grid(row=0, column=i, columnspan=2, sticky="WE")
    # labels[i].place(x=0 + 30 * i, y=0)
    m.showinfo(message="sljdnf")
    z = math.floor((i) / 4)
    canvas_hand3.create_image(40 + 40 * (i - 4 * z), 50 + 75 * z, image=hands[0].cards_in_hand[i].photo)

canvas_hand4 = Canvas(frame_player, relief="groove", width=196, height=250, bg="#00B343", borderwidth=0)
canvas_hand4.grid(row=0, column=3, padx=5)
for i in range(12):
    # Frame(frame_dealer, width=27, height=0, bg="#00B343").grid(row=1, column=i)
    # labels[i].grid(row=0, column=i, columnspan=2, sticky="WE")
    # labels[i].place(x=0 + 30 * i, y=0)
    m.showinfo(message="sljdnf")
    z = math.floor((i) / 4)
    canvas_hand4.create_image(40 + 40 * (i - 4 * z), 50 + 75 * z, image=hands[0].cards_in_hand[i].photo)
canvas_hand5 = Canvas(frame_dealer, relief="groove", width=400, height=96, bg="#00B343", borderwidth=0)
canvas_hand5.grid(row=0, column=0, sticky="S")
for i in range(9):
    # Frame(frame_dealer, width=27, height=0, bg="#00B343").grid(row=1, column=i)
    # labels[i].grid(row=0, column=i, columnspan=2, sticky="WE")
    # labels[i].place(x=0 + 30 * i, y=0)
    m.showinfo(message="sljdnf")
    z = math.floor((i) / 4)
    canvas_hand5.create_image(40 + 40 * i, 50, image=hands[0].cards_in_hand[i].photo)
root.mainloop()
# # frame1 = Frame(root, relief="groove")
# # frame1.grid(row=0, column=0)
# # button1 = Button(frame1, text="Up1")
# # button1.grid(row=0, column=0, columnspan=2, sticky="WE")
# # button2 = Button(frame1, text="Up2")
# # button2.grid(row=0, column=1, columnspan=2, sticky="WE")
# # button3 = Button(frame1, text="Down3")
# # button4 = Button(frame1, text="Down4")
# # button5 = Button(frame1, text="Down5")
# # button3.grid(row=1, column=0)
# # button4.grid(row=1, column=1)
# # button5.grid(row=1, column=2)

# root.mainloop()