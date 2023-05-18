# import tkinter as tk
import random


class Card:

    def __init__(self, card_suit, value, card_sign):
        self.card_suit = card_suit
        self.value = value
        self.card_sign = card_sign

    def get_value(self):
        return self.value

    def get_sign(self):
        return self.card_sign

    def get_suit(self):
        return self.card_suit


class Hand:

    def __init__(self, sequence_number, first_value, second_value):
        self.sequence_number = sequence_number
        self.first_value = first_value
        self.second_value = second_value
        self.cards_in_hand = []
        # self.card_values_sum = 0

    def get_hand_number(self):
        return self.sequence_number

    def get_values(self):
        return [self.first_value, self.second_value]

    def count_card_values(self):
        i = self.cards_in_hand[len(self.cards_in_hand) - 1]
        self.first_value += i.get_value()
        self.second_value += i.get_value()
        if i.get_sign().__eq__("A"):
            temp = self.second_value + 10
            if temp > 21:
                print("You lost")
                pass
            elif temp==21:
                self.first_value=self.second_value=21
            else:
                self.second_value=temp
        if self.first_value<21 and self.second_value>21:
            self.second_value=self.first_value
        if self.first_value==21 or self.second_value==21:
            self.first_value = 21
            self.second_value = 21
            print("You win")
        elif self.first_value>21 or (self.first_value>21 and self.second_value>21):
            print("You lost")

    def hit(self):
        temp = deck[random.randint(0, len(deck)-1)]
        self.cards_in_hand.append(temp)
        deck.remove(temp)
        self.count_card_values()

    def deal(self):
        for i in range(2):
            self.hit()

    def split_hand(self):
        hands.append(Hand(len(hands)+1, 0, 0))
        hands[-1].cards_in_hand.append(self.cards_in_hand.pop(1))
        self.hit()
        hands[-1].hit()


def split_check(hand):
    if len(hand.cards_in_hand) == 2 and hand.cards_in_hand[0].get_value() == hand.cards_in_hand[1].get_value():
        """ Activate split button for selected hand"""
        pass


''' Start game button '''
def start_game():
    hands.append(Hand(1, 0, 0))
    generate_deck()


''' Deck generation button '''
def generate_deck():
    card_suits = ["spades", "clubs", "hearts", "diamonds"]
    card_values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card_signs = ["A", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "J", "Q", "K"]
    for i in card_suits:
        for j in range(len(card_signs)):
            deck.append(Card(i, card_values[j], card_signs[j]))

''' Hold '''
# def hold():
#     pass

hands_counter = 0
deck = []
hands = []
player_bid = 0
