# import tkinter as tk
import random


class Card:

    def __init__(self, card_suit, value, card_sign):
        self.card_suit = card_suit
        self.value = value
        self.card_sign = card_sign

    def get_card(self):
        return self.value

    def get_name(self):
        print(self.card_sign)

    def get_suit(self):
        print(self.card_suit)


def start_game():
    global balance
    balance = 25000


def generate_deck():
    card_suits = ["spades", "clubs", "hearts", "diamonds"]
    card_values = [[1, 11], 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card_signs = ["A", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "J", "Q", "K"]
    for i in card_suits:
        for j in range(len(card_signs)):
            deck.append(Card(i, card_values[j], card_signs[j]))


def count_values(hand):
    summ = 0
    for i in hand:
        summ += i.get_card
    return summ


def deal():
    global player_hands_amount, player_cards_values, dealer_cards_values
    player_hands_amount = 1
    for i in range(2):
        temp = deck[random.randint(0, len(deck))]
        player_hand.append(temp)
        deck.remove(temp)
        temp = deck[random.randint(0, len(deck))]
        dealer_hand.append(temp)
        deck.remove(temp)
    player_cards_values = count_values(player_hand)
    dealer_cards_values = count_values(dealer_hand)


def hit(hand):
    temp = deck[random.randint(0, len(deck))]
    hand.append(temp)
    deck.remove(temp)
    player_cards_values = count_values(player_hand)
    dealer_cards_values = count_values(dealer_hand)


def hold():
    pass


def split_cards(hand_of_player):
    global second_player_hand, third_player_hand, fourth_player_hand
    player_hands_amount += 1
    if player_hands_amount == 2:
        second_player_hand = []
        temp = hand_of_player[random.randint(0, len(hand_of_player))]
        second_player_hand.append(temp)
        hand_of_player.remove(temp)
        hit(hand_of_player)
        hit(second_player_hand)
    elif player_hands_amount == 3:
        third_player_hand = []
        temp = hand_of_player[random.randint(0, len(hand_of_player))]
        third_player_hand.append(temp)
        hand_of_player.remove(temp)
        hit(hand_of_player)
        hit(third_player_hand)
    else:
        fourth_player_hand = []
        temp = hand_of_player[random.randint(0, len(hand_of_player))]
        fourth_player_hand.append(temp)
        hand_of_player.remove(temp)
        hit(hand_of_player)
        hit(fourth_player_hand)


def ya_makaka():pass

deck = []
player_hand = []
dealer_hand = []
generate_deck()
deal()
print(len(deck))
print(player_hand)