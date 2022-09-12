
# Deck 
from typing import List
from collections import Counter
import numpy as np

def flatten_list(nested_list:List[list]) -> None:
    return [item for sublist in nested_list for item in sublist]

class Deck:
    def __init__(self, seed:int=42) -> None:
        np.random.seed(seed)
        self.suits = ["H", "D", "S", "C"]
        self._init_deck
    
    def _suit(self, suit):
        return [f"{suit}-{i}" for i in range(2, 15)]

    @property
    def _init_deck(self):
        self.deck = flatten_list([self._suit(suit_name) for suit_name in self.suits])

    def _get_suits_in_hand(self, hand:List[str]):
        return [card.split("-")[0] for card in hand]
    
    def _get_values_in_hand(self, hand:List[str]):
        return np.array([int(card.split("-")[1]) for card in hand])
    
    def _draw_cards(self, number_of_cards:int):
        cards_drawn = np.random.choice(self.deck, number_of_cards, replace=False)
        #remove cards from deck
        _ = [self.deck.remove(card) for card in cards_drawn]
        return cards_drawn.tolist()
    
    @property
    def _shuffle_deck(self):
        # shuffle remaining cards
        np.random.shuffle(self.deck)


class Pitch(Deck):
    def __init__(self) -> None:
        super().__init__()
        self.cards_in_hand = 6
        self.jack_value = 11
    
    def play_game(self):
        succes_full_game = False
        if self.second_hand:
            if self.first_hand:
                if self.third_hand:
                    if self.fourth_hand:
                        succes_full_game = True
        return succes_full_game        

    def first_hand(self):
        #None dealer's first hand
        first_hand = self._draw_cards(self.cards_in_hand)

    def second_hand(self):
        """ Dealer's first hand
        Conditions:
            * card_value > 11 [any single card of queen, king, ace]
            * len(low_suit) > 2 [two of any low suit]
        >>> p = Pitch()
        >>> second_hand = p._draw_cards(number_of_cards=6)
        >>> not any( p._get_values_in_hand(second_hand) > 11)
        """
        second_hand = self._draw_cards(self.cards_in_hand)
        suits_in_hand = p._get_suits_in_hand(hand)
        _, suit_count = np.unique(suits_in_hand, return_counts=True)
        values_in_hand = p._get_values_in_hand(second_hand)
        if not any( values_in_hand > 11):
            if not any(suit_count > 2):
                return True
        return False

    def third_hand(self):
        pass

    def fourth_hand(self):
        pass

p = Pitch()
p._draw_cards(5)
p.deck
p._init_deck
p._shuffle_deck
