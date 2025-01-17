import random

def dealCards():
    """Deals two cards to the player."""
    cards = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'A', 'J', 'Q', 'K']
    hand = [random.choice(cards), random.choice(cards)]
    return hand

def hitCards(hand):
    """Adds one card to the player's hand."""
    cards = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'A', 'J', 'Q', 'K']
    hand.append(random.choice(cards))

def calculateScore(hand):
    """Calculates the score of the hand."""
    score = 0
    ace_count = 0
    for card in hand:
        if isinstance(card, int):
            score += card
        elif card in ['J', 'Q', 'K']:
            score += 10
        elif card == 'A':
            ace_count += 1
            score += 11  # Assume Ace is 11 initially

    # Adjust for Aces if the score is over 21
    while score > 21 and ace_count > 0:
        score -= 10
        ace_count -= 1

    return score

def blackjack():
    """Main game loop."""
    start = True
    while start:
        userInput = input("Would you like to start a game of Blackjack (y/n): ")
        if userInput.lower() == 'y':
            hand = dealCards()
            print(f"Your cards are: {hand}, current score: {calculateScore(hand)}")

            while True:
                userHit = input("Would you like to HIT (H) or STAY (S): ").lower()
                if userHit == 'h':
                    hitCards(hand)
                    print(f"Your cards are now: {hand}, current score: {calculateScore(hand)}")
                    if calculateScore(hand) > 21:
                        print("You went over 21! You lose.")
                        break
                elif userHit == 's':
                    print(f"You stayed with: {hand}, final score: {calculateScore(hand)}")
                    break
                else:
                    print("Invalid input. Please enter 'H' or 'S'.")
        else:
            start = False
            print("Thanks for playing!")

blackjack()
