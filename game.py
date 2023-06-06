from bj import *
from tkinter import *
from tkinter import messagebox as m
import math
import time as t

widgets = []
hand_number = 0
bid = 0


def var_get():
    global hand_number
    hand_number = var.get()


def var_check():
    temp = 0
    for i in range(1, len(hands)):
        if hands[i].status.__eq__("Inactive"):
            temp += 1
    if temp == len(hands) - 1:
        dealer_play()
    else:
        for i in range(1, len(hands)):
            if hands[i].status.__eq__("Active"):
                var.set(i)


def check_values():
    temp = hands[hand_number].first_value
    temp1 = hands[hand_number].second_value
    if temp == 21 or temp1 == 21:
        hands[hand_number].status = "Inactive"
        widgets[hand_number * 3 + 1]["text"] = "21"
        hold()
    elif temp > 21:
        widgets[hand_number * 3 + 1]["text"] = str(temp)
        hold()
        if len(hands) == 2:
            dealer_play()
        else:
            var_check()
    elif temp != temp1:
        widgets[hand_number * 3 + 1]["text"] = str(temp) + "(" + str(temp1) + ")"
    elif temp == temp1:
        widgets[hand_number * 3 + 1]["text"] = str(temp)


def start_game():
    hands.append(Hand(0, 0))
    hands.append(Hand(0, 0))
    hands[1].actual_bid = bid
    generate_deck()
    hands[0].deal()
    hands[1].deal()
    show_cards_from_deal()


def show_cards_from_deal():
    global widgets
    widgets.append(Canvas(frame_dealer, relief="groove", width=400, height=96, bg="#00B343", borderwidth=0))
    widgets.append(
        Label(frame_dealer, font="Arial 14", text=str(hands[0].cards_in_hand[0].value) + "+?", relief="groove", width=6,
              height=1, bg="yellow"))
    widgets.append(Canvas(frame_player, relief="groove", width=196, height=250, bg="#00B343", borderwidth=0))
    widgets.append(Radiobutton(frame_player, variable=var, bg="#00b343", value=1))
    widgets.append(Label(frame_player, font="Arial 14", relief="groove", width=6, height=1, bg="yellow"))
    widgets[0].grid(row=1, column=0, sticky="S")
    widgets[1].grid(row=0, column=0, sticky="S")
    widgets[2].grid(row=1, column=0, sticky="N", padx=5)
    widgets[3].grid(row=2, column=0, sticky="N")
    widgets[4].grid(row=0, column=0, sticky="S")
    widgets[0].create_image(40, 50, image=hands[0].cards_in_hand[0].photo)
    widgets[0].create_image(80, 50, image=back)
    for i in range(len(hands[1].cards_in_hand)):
        z = math.floor(i / 4)
        widgets[2].create_image(40 + 40 * (i - 4 * z), 50 + 75 * z, image=hands[1].cards_in_hand[i].photo)
    var.set(1)
    var_get()
    check_values()


def bid_button():
    global bid, balance
    try:
        bid = int(entry_of_bid.get())
        if bid > balance or bid < 0:
            raise ValueError
        button_hit["state"] = ACTIVE
        button_split["state"] = ACTIVE
        button_double["state"] = ACTIVE
        button_hold["state"] = ACTIVE
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
    widgets[hand_number * 3 - 1].create_image(40 + 40 * (len(hands[hand_number].cards_in_hand) - 1 - 4 * z),
                                              50 + 75 * z, image=hands[hand_number].cards_in_hand[-1].photo)


def hold():
    var_get()
    hands[hand_number].status = "Inactive"
    widgets[hand_number * 3]["state"] = DISABLED
    widgets[hand_number * 3 + 1]["text"] = hands[hand_number].second_value
    var_check()


def split():
    global widgets, balance, bid
    var_get()
    if len(hands[hand_number].cards_in_hand) == 2:
        if hands[hand_number].cards_in_hand[0].value == hands[hand_number].cards_in_hand[1].value:
            pass
        else:
            m.showwarning(message="You can't do this!!")
            return
    else:
        m.showwarning(message="You can't do this!!")
        return
    if balance < hands[hand_number].actual_bid:
        m.showwarning(message="You can't do this!!")
        return
    hands.append(Hand(0, 0))
    hands[-1].actual_bid = bid
    balance -= bid
    balance_label["text"] = "Balance:" + str(balance)
    widgets[hand_number * 3 - 1].destroy()
    widgets.remove(widgets[hand_number * 3 - 1])
    widgets.insert(hand_number * 3 - 1,
                   Canvas(frame_player, relief="groove", width=196, height=250, bg="#00B343", borderwidth=0))
    widgets[hand_number * 3 - 1].grid(row=1, column=hand_number - 1, sticky="N", padx=5)
    widgets.append(Canvas(frame_player, relief="groove", width=196, height=250, bg="#00B343", borderwidth=0))
    widgets.append(Radiobutton(frame_player, variable=var, bg="#00b343", value=len(hands) - 1))
    widgets.append(Label(frame_player, font="Arial 14", relief="groove", width=6, height=1, bg="yellow"))
    widgets[len(widgets) - 3].grid(row=1, column=len(hands) - 2, sticky="N", padx=5)
    widgets[len(widgets) - 2].grid(row=2, column=len(hands) - 2, sticky="N")
    widgets[len(widgets) - 1].grid(row=0, column=len(hands) - 2, sticky="S")
    hands[-1].cards_in_hand.append(hands[hand_number].cards_in_hand.pop(1))
    hands[hand_number].first_value = 0
    hands[-1].first_value = 0
    hands[hand_number].second_value = 0
    hands[-1].second_value = 0
    hands[hand_number].count_card_values()
    hands[-1].count_card_values()
    hands[-1].hit()
    hands[hand_number].hit()
    for i in range(len(hands[hand_number].cards_in_hand)):
        z = math.floor(i / 4)
        widgets[hand_number * 3 - 1].create_image(40 + 40 * (i - 4 * z), 50 + 75 * z,
                                                  image=hands[hand_number].cards_in_hand[i].photo)
    check_values()
    for i in range(len(hands[-1].cards_in_hand)):
        z = math.floor(i / 4)
        widgets[len(widgets) - 3].create_image(40 + 40 * (i - 4 * z), 50 + 75 * z,
                                               image=hands[-1].cards_in_hand[i].photo)
    var.set(len(hands) - 1)
    var_get()
    check_values()
    button_split["state"] = DISABLED


def double_button():
    global balance
    var_get()
    if len(hands[hand_number].cards_in_hand) == 2:
        if balance < hands[hand_number].actual_bid:
            m.showwarning(message="You can't do this")
            return
    else:
        m.showwarning(message="You can't do this")
        return
    hands[hand_number].actual_bid += bid
    balance -= bid
    balance_label["text"] = "Balance:" + str(balance)

    hands[hand_number].hit()
    widgets[hand_number * 3]["state"] = DISABLED
    hands[hand_number].status = "Inactive"
    show_card()
    check_values()
    var_check()


def dealer_play():
    global balance, frame_player, frame_dealer, button_bid, button_hit, button_hold, button_split, button_double, entry_of_bid, widgets, hands, hand_number, root
    dealer_cards_reveal()

    if hands[0].first_value >= 17 or hands[0].first_value == 21:
        hands[0].second_value = hands[0].first_value
    elif hands[0].second_value >= 17 or hands[0].second_value == 21:
        hands[0].first_value = hands[0].second_value


    else:
        while True:
            hands[0].hit()
            show_dealer_cards()
            temp = hands[0].first_value
            temp1 = hands[0].second_value
            if temp >= 17 or 21 >= temp1 >= 17:
                break
        if temp == 21 or temp1 == 21:
            hands[0].first_value = 21
            hands[0].second_value = 21
        elif temp < 17 <= temp1:
            hands[0].first_value = temp1
        elif temp >= 17 > temp1:
            hands[0].second_value = temp
    widgets[1]["text"] = str(hands[0].first_value)
    for i in range(1, len(hands)):
        if hands[i].second_value > 21:
            continue
        elif hands[0].first_value > 21:
            balance += hands[i].actual_bid * 2
            break
        else:
            if hands[i].second_value == hands[0].first_value:
                balance += hands[i].actual_bid
                continue
            elif 21 - hands[0].first_value > 21 - hands[i].second_value:
                balance += hands[i].actual_bid * 2
                continue
            else:
                pass
    balance_label["text"] = "Balance:" + str(balance)
    m.showinfo(message="Your current balance is:" + str(balance))
    t.sleep(1)

    if balance == 0:
        root.quit()

    widgets = []
    hand_number = 0

    hands = []
    frame_player.destroy()
    frame_dealer.destroy()
    frame_dealer = Frame(root, relief="groove", width=1000, height=100, bg="#00B343")
    frame_dealer.grid(row=1, column=0)
    root.rowconfigure(0, weight=20)

    frame_player = Frame(root, relief="groove", width=196, height=250, bg="#00B343")
    frame_player.grid(row=2, column=0)
    root.rowconfigure(1, weight=10)

    button_split["state"] = DISABLED
    button_double["state"] = DISABLED
    button_hold["state"] = DISABLED
    button_hit["state"] = DISABLED
    button_bid = Button(frame_buttons, text="BID", font="Arial 14", width=22, bg="limegreen", command=bid_button)
    button_bid.grid(row=1, column=3, sticky="WES")

    entry_of_bid = Entry(frame_buttons, font="Arial 25", width=15, relief="groove", bg="#00b343")
    entry_of_bid.grid(row=0, column=3, sticky="WES")


def dealer_cards_reveal():
    global widgets
    widgets[0].destroy()
    widgets.remove(widgets[0])
    widgets.insert(0, Canvas(frame_dealer, relief="groove", width=400, height=96, bg="#00B343", borderwidth=0))
    widgets[0].grid(row=1, column=0, sticky="S")
    widgets[0].create_image(40, 50, image=hands[0].cards_in_hand[0].photo)
    widgets[0].create_image(80, 50, image=hands[0].cards_in_hand[1].photo)


def show_dealer_cards():
    temp = len(hands[0].cards_in_hand)
    widgets[0].create_image(40 + 40 * (temp - 1), 50, image=hands[0].cards_in_hand[-1].photo)


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

button_split = Button(frame_buttons, text="SPLIT", font="Arial 14", width=22, bg="limegreen", state=DISABLED,
                      command=split)
button_split.grid(row=1, column=0, sticky="WES")

button_double = Button(frame_buttons, text="DOUBLE", font="Arial 14", width=22, bg="limegreen", state=DISABLED,
                       command=double_button)
button_double.grid(row=1, column=1, sticky="WES")

button_hit = Button(frame_buttons, text="HIT", font="Arial 14", width=22, bg="limegreen", state=DISABLED,
                    command=hit_button)
button_hit.grid(row=1, column=2, sticky="S")

button_hold = Button(frame_buttons, text="HOLD", font="Arial 14", width=22, bg="limegreen", state=DISABLED,
                     command=hold)
button_hold.grid(row=1, column=3, sticky="WES")

button_bid = Button(frame_buttons, text="BID", font="Arial 14", width=22, bg="limegreen", command=bid_button)
button_bid.grid(row=1, column=3, sticky="WES")

entry_of_bid = Entry(frame_buttons, font="Arial 25", width=15, relief="groove", bg="#00b343")
entry_of_bid.grid(row=0, column=3, sticky="WES")

back = PhotoImage(file="images\\card_back.png")
root.mainloop()
