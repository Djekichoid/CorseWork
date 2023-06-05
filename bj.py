from tkinter import PhotoImage
import random


class Card:

    def __init__(self, card_suit, value, card_sign):
        self.card_suit = card_suit
        self.value = value
        self.card_sign = card_sign
        self.photo = PhotoImage(file="images\\" + self.card_suit + "\\" + card_sign + ".png")


class Hand:

    def __init__(self, first_value, second_value):
        self.first_value = first_value
        self.second_value = second_value
        self.cards_in_hand = []
        self.actual_bid = 0
        self.status = "Active"

    def get_values(self):
        return [self.first_value, self.second_value]

    def count_card_values(self):
        i = self.cards_in_hand[-1]
        self.first_value += i.value
        self.second_value += i.value
        if i.card_sign.__eq__("A"):
            temp = self.second_value + 10
            if temp > 21:
                pass
            elif temp == 21:
                self.first_value = self.second_value = 21
            else:
                self.second_value = temp
        if self.first_value < 21 < self.second_value:
            self.second_value = self.first_value
        if self.first_value == 21 or self.second_value == 21:
            self.first_value = 21
            self.second_value = 21

    def hit(self):
        temp = deck[random.randint(0, len(deck) - 1)]
        self.cards_in_hand.append(temp)
        deck.remove(temp)
        self.count_card_values()

    def deal(self):
        for i in range(2):
            self.hit()


def generate_deck():
    card_suits = ["spades", "clubs", "hearts", "diamonds"]
    card_values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card_signs = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
    for i in card_suits:
        for j in range(len(card_signs)):
            deck.append(Card(i, card_values[j], card_signs[j]))


hands_counter = 0
deck = []
hands = []
