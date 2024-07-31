import random

# Constants for card values
CARD_VALUES = {
    '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10,
    'J': 10, 'Q': 10, 'K': 10, 'A': 11
}


# Create a deck of cards
def create_deck():
    suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
    ranks = list(CARD_VALUES.keys())
    deck = [{'rank': rank, 'suit': suit} for suit in suits for rank in ranks]
    random.shuffle(deck)
    return deck


# Calculate the value of a hand
def calculate_hand_value(hand):
    value = sum(CARD_VALUES[card['rank']] for card in hand)
    num_aces = sum(1 for card in hand if card['rank'] == 'A')
    # Adjust for aces if value is over 21
    while value > 21 and num_aces:
        value -= 10
        num_aces -= 1
    return value


# Deal a card from the deck
def deal_card(deck):
    return deck.pop()


# Display the hand
def display_hand(hand, name):
    cards = [f"{card['rank']} of {card['suit']}" for card in hand]
    print(f"{name}'s hand: {', '.join(cards)}")


# Main game loop
def play_blackjack():
    deck = create_deck()
    player_hand = [deal_card(deck), deal_card(deck)]
    dealer_hand = [deal_card(deck), deal_card(deck)]

    print("Welcome to Blackjack!")

    # Player's turn
    while True:
        display_hand(player_hand, "Player")
        if calculate_hand_value(player_hand) == 21:
            print("Blackjack! You win!")
            return
        elif calculate_hand_value(player_hand) > 21:
            print("Bust! You lose!")
            return
        action = input("Do you want to 'hit' or 'stand'? ").lower()
        if action == 'hit':
            player_hand.append(deal_card(deck))
        elif action == 'stand':
            break
        else:
            print("Invalid input, please enter 'hit' or 'stand'.")

    # Dealer's turn
    while calculate_hand_value(dealer_hand) < 17:
        dealer_hand.append(deal_card(deck))

    display_hand(player_hand, "Player")
    display_hand(dealer_hand, "Dealer")

    # Determine the winner
    player_value = calculate_hand_value(player_hand)
    dealer_value = calculate_hand_value(dealer_hand)

    if dealer_value > 21 or player_value > dealer_value:
        print("You win!")
    elif player_value < dealer_value:
        print("Dealer wins!")
    else:
        print("It's a tie!")


# Run the game
play_blackjack()
