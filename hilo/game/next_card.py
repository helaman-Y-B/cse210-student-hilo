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

        self.cards = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
        self.card = 0

        # declared player response to get higher or lower inputs
        self.score = 0


    def can_continue(self):
        """The can_continue method determines whether or not the Dealer can throw again. 

        It returns a boolean value that is true if the dice have at least a five, or a one, 
        or the num_throws is greater than zero. Otherwise, it returns false."""

        # If there is no value in self.card, the game will continue
        if self.card != "":
            keep_playing = True
        else:
            keep_playing = False

        return keep_playing

    def get_points(self, last_card, response):
        """The get_points method calculates and returns the total points for the current game. 
        It goes from 1 point up until 13 points"""
        # if the card is number '2', the get_points will add 1 point
        # if the card is the letter 'A', the get_points will add 13 points

        current_card = self.card
        thrown_card = last_card
        res = response

        if res == "l":
            if current_card < thrown_card:

                self.score += 100
            elif current_card > thrown_card:

                self.score -= 75

        elif res == "h":
            if current_card > thrown_card:

                self.score += 100

            elif current_card < thrown_card:
                self.score -= 75

        else:
            self.score = 0

        score = self.score

        return score


    def throw_card(self):
        """The throw_card method randomly choose a value from a list called 'cards'. 

        Args:
            self (Dealer_card): an instance of Dealer_card. 
        Return:
            card: return the randomly choosen card and use as playing cards"""
        
        # Randomly choose a card from the cards list
        card = random.choice(self.cards)

        self.card = card

        return card

