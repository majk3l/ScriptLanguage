
def hand_rank(hand):
    hand_rank_list = []  # TODO: Create list of cards ranks. Use list comprehension.
    hand_color_list = [] # TODO: Create list of cards suits. Use list comprehension.

    # Histogram of ranks tells us if there is more than once occurence of card rank.
    # We need this to establish what hand do we have.
    # TODO: use histogram() from previous lab.
    hand_rank_histogram = histogram(hand_rank_list)
    # Histogram of suits, if 5 in hand_color_histogram.values() == True
    # than all of the cards are in the same suit
    hand_color_histogram = histogram(hand_color_list)
    # We want to find if the hand contains five cards of sequential rank
    # TODO: implement function is_rank_sequence(hand) which returns true if so
    is_hand_rank_sequence = is_rank_sequence(hand) 

    hand_strength = 0 # returned value, you need to set this
    # ------ lets check player's hand:
    # --- Royal flush: 5 cards of sequential rank, all of the same suit, Ace is the highest
    if( (5 in hand_color_histogram.values()) and ( 'A' in hand_rank_list ) and is_hand_rank_sequence):
        hand_strength = 10
    # --- straight flush: 5 cards of sequential rank, all of the same suit
    elif( ( 5 in hand_color_histogram.values()) and is_hand_rank_sequence):
        hand_strength =  9
    # TODO: check rest of possible hand ranks 
    #       set the hand_strength variable:
    #        - four of a kind: four cards of the same rank and one card of another rank
    #        - full house: three cards of one rank and two cards of another rank
    #        - flush: five cards all of the same suit, not all of sequential rank
    #        - straight: five cards of sequential rank, not all of the same suit
    #        - three of a kind: three cards of the same rank and two cards of two other ranks
    #        - two pair: two cards of the same rank, two cards of another rank and one card of a third rank
    #        - One pair: two cards of the same rank and three cards of three other ranks
    #        - high card: five cards not all of sequential rank or of the same suit, and none of which are of the same rank
    return(hand_strength)
