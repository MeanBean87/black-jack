import random
import art
import variables
from replit import clear


def draw_cards(hand):
    random_index = random.sample(range(len(variables.cards)), 2)
    for index in random_index:
        hand.append(variables.cards[index])


def hit_cards(hand):
    random_index = random.sample(range(len(variables.cards)), 1)
    for index in random_index:
        hand.append(variables.cards[index])


def score(toggle_show_dealer):
    if not toggle_show_dealer:
        print(f"\n    Your cards {variables.players_hand}, current score: {sum(variables.players_hand)}")
        print(f"    Dealer's first card is: {variables.dealers_hand[0]}\n")
    else:
        print(f"\n    Your cards: {variables.players_hand}, current score: {sum(variables.players_hand)}")
        print(f"    Dealers cards: {variables.dealers_hand}, current score: {sum(variables.dealers_hand)}\n")


def endgame():
    while sum(variables.dealers_hand) < 17:
        hit_cards(variables.dealers_hand)
        ace_check(variables.dealers_hand)
    if sum(variables.dealers_hand) == sum(variables.players_hand):
        score(True)
        print("    ****It's a Draw***\n")
    elif sum(variables.dealers_hand) > 21:
        score(True)
        print("    ***Dealer Busted***")
        print("    ******You win******\n")
    elif sum(variables.dealers_hand) < sum(variables.players_hand):
        score(True)
        print("    ******You win******\n")
    else:
        score(True)
        print("    ******You Lose*****\n")


def ace_check(hand):
    ace = 11
    hand_weight = sum(hand)
    if hand_weight > 21:
        if ace in hand:
            index = hand.index(ace)
            hand[index] = 1


def clear_hands():
    variables.dealers_hand.clear()
    variables.players_hand.clear()
    clear()


def game():
    print(art.logo)
    draw_cards(variables.dealers_hand)
    draw_cards(variables.players_hand)
    score(False)
    bust = False
    while not bust:
        hit = input("Type 'y' to hit, type 'n' to stay: ").lower()
        if hit == 'y':
            hit_cards(variables.players_hand)
            ace_check(variables.players_hand)
            if sum(variables.players_hand) > 21:
                bust = True
                score(True)
                print(f"You're score is {sum(variables.players_hand)} you're over 21. You Busted.\n")
            else:
                score(False)
                bust = False
        elif hit == 'n':
            endgame()
            break
