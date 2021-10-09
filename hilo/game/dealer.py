from game.next_card import Dealer_card


class Dealer:
    def __init__(self):
        """The class constructor.

        Args:
            self (Dealer): an instance of Dealer.
        """
        # keep_playing is = to True, so that the game can start
        self.keep_playing = True
        # The user score
        self.score = 300
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
            self.output(self.init_card)
            self.updates()

    def get_input(self):
        """Gets the inputs at the beginning of each round of play. In this case,
        that means the Dealer will show a new card.

        Args:
            self (Dealer): an instance of Dealer.
        """
        # Here is where the card will be stored, to be able to use it at the end of this file.
        self.next_card.throw_card()
        self.old_card = self.next_card.throw_card()
        

    def updates(self):
        """Updates the important game information for each round of play. In 
        this case, that means updating the score.

        Args:
            self (Dealer): an instance of Dealer.
        """
        # calls the get_points function, and store  the points into a value called score
        points = self.next_card.get_points()
        self.score += points

    def output(self, init_card):
        """Outputs the important game information for each round of play. In 
        this case, that means the card that were showed and the score.

        Args:
            self (Dealer): an instance of Dealer.
        """
        # Print the current card and the current score.
        #current_card = self.next_card.throw_card()
        next_card = self.next_card.throw_card()
        
        #print(current_card)
        # ~ print(next_card)
        print(f"\nThe Dealer Throw: {init_card}")

        if self.next_card.can_continue():
            # The user will choose, if the card will be higher or lower then the last card.
            choice = input("Will it be Heigher or Lower? [H/L] ").lower
            self.next_card.player_response = choice

        print(f"Next Card: {next_card}")

        print(f"Your current score is: {self.score}")
        self.init_card = next_card
