from game.next_card import Dealer_card


class Dealer:
    def __init__(self):
        """The class constructor.

        Args:
            self (Dealer): an instance of Dealer.
        """
        # keep_playing is = to True, so that the game can start
        self.keep_playing = True
        # calls the Dealer_card class.
        self.next_card = Dealer_card()
        # declare old card variable to store the current card to compare it on the later part
        self.old_card = 0

    def start_game(self):
        """Starts the game loop to control the sequence of play.

        Args:
            self (Dealer): an instance of Dealer.
        """
        self.init_card = self.next_card.throw_card()
        while self.keep_playing:
            """Functions to start the game"""
            # Calls the functions, making the game start
            self.output()

    def updates(self, respon):
        """Updates the important game information for each round of play. In 
        this case, that means updating the score.

        Args:
            self (Dealer): an instance of Dealer.
        """
        # calls the get_points function, and store  the points into a value called score
        points = self.next_card.get_points(self.init_card, respon)
        self.score = points

    def output(self):
        """Outputs the important game information for each round of play. In 
        this case, that means the card that were showed and the score.

        Args:
            self (Dealer): an instance of Dealer.
        """
        # Print the current card and the current score.
        #current_card = self.next_card.throw_card()
        print(f"\nThe Dealer Throw: {self.init_card}")
        next_card = self.next_card.throw_card()

        # ~ print(next_card)

        if self.next_card.can_continue():
            # The user will choose, if the card will be higher or lower then the last card.
            choice = input("Will it be Heigher or Lower? [H/L] ").lower

            self.updates(choice)
            print(f"Your current score is: {self.score}")

            print(f"Next Card: {next_card}")

        self.init_card = next_card
