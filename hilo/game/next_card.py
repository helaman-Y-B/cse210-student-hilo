import random


class Dealer_card:
    """Dealer_card class is used to 'Throw' a card
        so that the game can start, continue and end the game."""
    """Attributes:
                card and cards"""

    def __init__(self):
        """The class constructor.

        Args: 
            self (Dealer_card): an instance of Dealer_card."""
        # self.cards is the list of the 13 possible cards that the dealer can throw.
        self.cards = ["2", "3", "4", "5", "6",
                      "7", "8", "9", "10", "J", "Q", "K", "A"]
        self.card = ""

    def can_continue(self):
        """The can_continue method determines whether or not the Dealer can throw again. 

        It returns a boolean value that is true if the dice have at least a five, or a one, 
        or the num_throws is greater than zero. Otherwise, it returns false."""

        # If there is no value in self.card, the game will continue
        if self.card != "":
            keep_playing = True
        else:
            keep_playing = False

    def get_points(self):
        """The get_points method calculates and returns the total points for the current game. 
        It goes from 1 point up until 13 points"""
        # if the card is number '2', the get_points will add 1 point
        # if the card is the letter 'A', the get_points will add 13 points
        score = 0

        return score

    def throw_card(self):
        """The throw_card method randomly choose a value from a list called 'cards'. """
        # Randomly choose a card from the cards list
        card = random.choice(self.cards)
        self.card = card
