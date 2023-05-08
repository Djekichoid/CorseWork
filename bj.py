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
        self.card_values_sum = 0

    def get_hand_number(self):
        return self.sequence_number

    def get_values(self):
        return [self.first_value, self.second_value]

    def count_card_values(self):
        sum = 0
        for i in self.cards_in_hand:
            sum += i.get_value()
        self.card_values_sum = sum

    def hit(self, deck):
        temp = deck[random.randint(0, len(deck))]
        self.cards_in_hand.append(temp)
        deck.remove(temp)
        self.count_card_values()


''' Start game button '''
def start_game():
    global balance
    balance = 25000


''' Deck generation button '''
def generate_deck():
    card_suits = ["spades", "clubs", "hearts", "diamonds"]
    card_values = [[1, 11], 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card_signs = ["A", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "J", "Q", "K"]
    for i in card_suits:
        for j in range(len(card_signs)):
            deck.append(Card(i, card_values[j], card_signs[j]))


''' Count your card values '''
def count_values(hand):
    summ = 0
    for i in hand:
        summ += i.get_card()
    return summ


''' First deal '''
# def deal():
#     global player_hands_amount, player_cards_values, dealer_cards_values
#     player_hands_amount = 1
#     for i in range(2):
#         temp = deck[random.randint(0, len(deck))]
#         player_hand.append(temp)
#         deck.remove(temp)
#         temp = deck[random.randint(0, len(deck))]
#         dealer_hand.append(temp)
#         deck.remove(temp)
#     player_cards_values = count_values(player_hand)
#     dealer_cards_values = count_values(dealer_hand)

''' Take one card '''
# def hit(hand):
#     temp = deck[random.randint(0, len(deck))]
#     hand.append(temp)
#     deck.remove(temp)
#     player_cards_values = count_values(player_hand)
#     dealer_cards_values = count_values(dealer_hand)

''' Hold '''
# def hold():
#     pass

''' Split your deck '''
# def split_cards(hand_of_player):
#     global second_player_hand, third_player_hand, fourth_player_hand
#     player_hands_amount += 1
#     if player_hands_amount == 2:
#         second_player_hand = []
#         temp = hand_of_player[random.randint(0, len(hand_of_player))]
#         second_player_hand.append(temp)
#         hand_of_player.remove(temp)
#         hit(hand_of_player)
#         hit(second_player_hand)
#     elif player_hands_amount == 3:
#         third_player_hand = []
#         temp = hand_of_player[random.randint(0, len(hand_of_player))]
#         third_player_hand.append(temp)
#         hand_of_player.remove(temp)
#         hit(hand_of_player)
#         hit(third_player_hand)
#     else:
#         fourth_player_hand = []
#         temp = hand_of_player[random.randint(0, len(hand_of_player))]
#         fourth_player_hand.append(temp)
#         hand_of_player.remove(temp)
#         hit(hand_of_player)
#         hit(fourth_player_hand)

deck = []