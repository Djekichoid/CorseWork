from bj import *
from tkinter import *
from tkinter import messagebox as m
import math

widgets = []
hand_number = 0


def chicha():
    return 0


def var_get():
    global hand_number
    hand_number = var.get()


def var_check():
    temp = 0
    for i in range(1, len(hands)):
        if hands[i].status.__eq__("Inactive"):
            temp += 1
        if temp == len(hands):
            pass


def check_values():
    temp = hands[hand_number].first_value
    temp1 = hands[hand_number].second_value
    if temp == 21 or temp1 == 21:
        hands[hand_number].status = "Inactive"
        hold()
    elif temp > 21:
        hands[hand_number].status = "Inactive"
        hold()


def start_game():
    hands.append(Hand(0, 0, 0))
    hands.append(Hand(1, 0, 0))
    hands[1].actual_bid = bid
    generate_deck()
    hands[0].deal()
    hands[1].deal()
    show_cards_from_deal()


def show_cards_from_deal():
    global widgets
    widgets.append(Canvas(frame_dealer, relief="groove", width=400, height=96, bg="#00B343", borderwidth=0))
    widgets.append(Canvas(frame_player, relief="groove", width=196, height=250, bg="#00B343", borderwidth=0))
    widgets.append(Radiobutton(frame_player, variable=var, bg="#00b343", value=1))
    widgets[0].grid(row=0, column=0, sticky="S")
    widgets[1].grid(row=0, column=0, sticky="N", padx=5)
    widgets[2].grid(row=1, column=0, sticky="N")
    widgets[0].create_image(40, 50, image=hands[0].cards_in_hand[0].photo)
    widgets[0].create_image(80, 50, image=back)
    for i in range(len(hands[1].cards_in_hand)):
        z = math.floor(i / 4)
        widgets[1].create_image(40 + 40 * (i - 4 * z), 50 + 75 * z, image=hands[1].cards_in_hand[i].photo)
    print(hands[1].first_value)
    print(hands[1].second_value)


def bid():
    global bid, balance
    try:
        bid = int(entry_of_bid.get())
        if bid > balance or bid < 0:
            raise ValueError
        balance -= bid
        button_bid.destroy()
        entry_of_bid.destroy()
        balance_label["text"] = "Balance:" + str(balance)
        start_game()
    except ValueError:
        m.showwarning(message="Wrong bid")


def hit_button():
    var_get()
    hands[hand_number].hit()
    show_card()
    check_values()


def show_card():
    z = math.floor((len(hands[hand_number].cards_in_hand) - 1) / 4)
    widgets[hand_number * 2 - 1].create_image(40 + 40 * (len(hands[hand_number].cards_in_hand) - 1 - 4 * z),
                                              50 + 75 * z, image=hands[1].cards_in_hand[-1].photo)


def hold():
    var_get()
    widgets[hand_number * 2]["state"] = DISABLED


balance = 25000
root = Tk()
root.geometry("1007x760")
root.resizable(height=False, width=False)
root.configure(bg="#00b343")
root.title("BlackJack")
background = PhotoImage(file=r"images/background.png")
backg = Label(root, width=1000, height=750, image=background, bg="#00b343")
backg.grid(row=0, column=0, rowspan=3)

var = IntVar()
var.set(1)

balance_label = Label(root, bg="#00b343", font="Arial 25", width=13, text="Balance:" + str(balance), relief="sunken",
                      borderwidth=3)
balance_label.grid(row=0, column=0, sticky="WN")

frame_dealer = Frame(root, relief="groove", width=1000, height=100, bg="#00B343")
frame_dealer.grid(row=1, column=0)
root.rowconfigure(0, weight=20)

frame_player = Frame(root, relief="groove", width=196, height=250, bg="#00B343")
frame_player.grid(row=2, column=0)
root.rowconfigure(1, weight=10)

frame_buttons = Frame(root, relief="groove", width=1000, height=100, bg="#00B343")
frame_buttons.grid(row=3, column=0, sticky="WES")
root.rowconfigure(2, weight=1)

button_split = Button(frame_buttons, text="SPLIT", font="Arial 14", width=22, bg="limegreen", command=chicha)
button_split.grid(row=1, column=0, sticky="WES")

button_double = Button(frame_buttons, text="DOUBLE", font="Arial 14", width=22, bg="limegreen", command=chicha)
button_double.grid(row=1, column=1, sticky="WES")

button_hit = Button(frame_buttons, text="HIT", font="Arial 14", width=22, bg="limegreen", command=hit_button)
button_hit.grid(row=1, column=2, sticky="S")

button_hold = Button(frame_buttons, text="HOLD", font="Arial 14", width=22, bg="limegreen", command=chicha)
button_hold.grid(row=1, column=3, sticky="WES")

button_bid = Button(frame_buttons, text="BID", font="Arial 14", width=22, bg="limegreen", command=bid)
button_bid.grid(row=1, column=3, sticky="WES")

entry_of_bid = Entry(frame_buttons, font="Arial 25", width=15, relief="groove", bg="#00b343")
entry_of_bid.grid(row=0, column=3, sticky="WES")

back = PhotoImage(file="images\\card_back.png")
# generate_deck()
# hands.append(Hand(1, 0, 0))
# canvas_hand1 = Canvas(frame_player, relief="groove", width=196, height=250, bg="#00B343", borderwidth=0)
# canvas_hand1.grid(row=0, column=0, padx=5)
# for i in deck:
#     hands[0].cards_in_hand.append(i)
# m.showinfo(message="sljdnf")
# for i in range(12):
#     m.showinfo(message="sljdnf")
#     z = math.floor((i) / 4)
#     canvas_hand1.create_image(40 + 40 * (i - 4 * z), 50 + 75 * z, image=hands[0].cards_in_hand[i].photo)
# canvas_hand2 = Canvas(frame_player, relief="groove", width=196, height=250, bg="#00B343", borderwidth=0)
# canvas_hand2.grid(row=0, column=1, padx=5)
# for i in range(12):
#     m.showinfo(message="sljdnf")
#     z = math.floor((i) / 4)
#     canvas_hand2.create_image(40 + 40 * (i - 4 * z), 50 + 75 * z, image=hands[0].cards_in_hand[i].photo)
# canvas_hand3 = Canvas(frame_player, relief="groove", width=196, height=250, bg="#00B343", borderwidth=0)
# canvas_hand3.grid(row=0, column=2, padx=5)
# for i in range(12):
#     m.showinfo(message="sljdnf")
#     z = math.floor((i) / 4)
#     canvas_hand3.create_image(40 + 40 * (i - 4 * z), 50 + 75 * z, image=hands[0].cards_in_hand[i].photo)
# canvas_hand4 = Canvas(frame_player, relief="groove", width=196, height=250, bg="#00B343", borderwidth=0)
# canvas_hand4.grid(row=0, column=3, padx=5)
# for i in range(12):
#     m.showinfo(message="sljdnf")
#     z = math.floor((i) / 4)
#     canvas_hand4.create_image(40 + 40 * (i - 4 * z), 50 + 75 * z, image=hands[0].cards_in_hand[i].photo)
# canvas_hand5 = Canvas(frame_dealer, relief="groove", width=400, height=96, bg="#00B343", borderwidth=0)
# canvas_hand5.grid(row=0, column=0, sticky="S")
# for i in range(9):
#     m.showinfo(message="sljdnf")
#     z = math.floor((i) / 4)
#     canvas_hand5.create_image(40 + 40 * i, 50, image=hands[0].cards_in_hand[i].photo)
root.mainloop()
