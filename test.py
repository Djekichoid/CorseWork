import unittest as u
from bj import *


class HandClassTest(u.TestCase):
    def test_deal(self):
        hand1 = Hand(0, 0)
        deck = generate_deck()
        hand1.deal()
        self.assertEqual(len(hand1.cards_in_hand), 2)
        self.assertEqual(len(deck), 50)

    def test_generate_deck(self):
        deck = generate_deck()
        self.assertEqual(len(deck), 52)

    def test_hit(self):
        hand1 = Hand(0, 0)
        deck = generate_deck()
        hand1.hit()
        self.assertEqual(len(hand1.cards_in_hand), 1)
        self.assertEqual(len(deck), 51)

    def test_count_card_values(self):
        hand1 = Hand(0, 0)
        deck = generate_deck()
        for i in deck:
            if i.card_sign.__eq__("A"):
                hand1.cards_in_hand.append(i)
                deck.remove(i)
                break
        hand1.count_card_values()
        self.assertEqual(hand1.first_value, 1)
        self.assertEqual(hand1.second_value, 11)
        for i in deck:
            if i.card_sign.__eq__("8"):
                hand1.cards_in_hand.append(i)
                deck.remove(i)
                break
        hand1.count_card_values()
        self.assertEqual(hand1.first_value, 9)
        self.assertEqual(hand1.second_value, 19)
        hand2 = Hand(0, 0)
        deck = generate_deck()
        for i in deck:
            if i.card_sign.__eq__("8"):
                hand2.cards_in_hand.append(i)
                deck.remove(i)
                break
        hand2.count_card_values()
        self.assertEqual(hand2.first_value, 8)
        self.assertEqual(hand2.second_value, 8)
        for i in deck:
            if i.card_sign.__eq__("A"):
                hand2.cards_in_hand.append(i)
                deck.remove(i)
                break
        hand2.count_card_values()
        self.assertEqual(hand2.first_value, 9)
        self.assertEqual(hand2.second_value, 19)
        hand3 = Hand(0, 0)
        deck = generate_deck()
        for i in deck:
            if i.card_sign.__eq__("K"):
                hand3.cards_in_hand.append(i)
                deck.remove(i)
                break
        hand3.count_card_values()
        self.assertEqual(hand3.first_value, 10)
        self.assertEqual(hand3.second_value, 10)
        for i in deck:
            if i.card_sign.__eq__("A"):
                hand3.cards_in_hand.append(i)
                deck.remove(i)
                break
        hand3.count_card_values()
        self.assertEqual(hand3.first_value, 21)
        self.assertEqual(hand3.second_value, 21)
