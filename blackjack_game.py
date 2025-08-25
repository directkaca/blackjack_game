import random
import art_4

total_card = [
    "Ace Card", "2 Card", "3 Card", "4 Card", "5 Card", "6 Card",
    "7 Card", "8 Card", "9 Card", "10 Card",
    "J Card", "Q Card", "K Card"
]

blackgame_status = True

def shuffle_card():
    return random.choice(list(total_card))

def hand_points(cards):
    total = 0
    aces = 0
    for c in cards:
        rank = c.split()[0]
        if rank == "Ace":
            total += 11
            aces += 1
        elif rank in ("J", "Q", "K", "10"):
            total += 10
        else:
            total += int(rank)
    while total > 21 and aces > 0:
        total -= 10
        aces -= 1
    return total

def show_dealer(dealer_cards, reveal=False):
    if not dealer_cards:
        print("Dealer card: (no cards)\n")
        return
    if reveal or len(dealer_cards) == 1:
        print(f"Dealer card: {dealer_cards}\n")
    else:
        print(f"Dealer card: [{dealer_cards[0]}, ??]\n")

print(art_4.intro_art)
print("\nWelcome to Blackjack game")
while True:
    play_or_not_play = input("Do you want to play the game? type 'y' or 'n'\n >> ").lower()
    if play_or_not_play == 'y':
        break
    elif play_or_not_play == 'n':
        blackgame_status = False
        break
    else:
        print("Your input is invalid, please try again\n")


while blackgame_status:
    dealer_status = True
    user_status = True

    user_card = []
    dealer_card = []

    print("\nYou and dealer got two random card")

    draw_card = shuffle_card()
    user_card.append(draw_card)
    draw_card = shuffle_card()
    user_card.append(draw_card)

    user_point = hand_points(user_card)

    print(f"Your card are {user_card}")
    print(f"Your points are {user_point}\n")
    
    draw_card = shuffle_card()
    dealer_card.append(draw_card)
    draw_card = shuffle_card()
    dealer_card.append(draw_card)

    show_dealer(dealer_card, reveal = False)
    dealer_point = hand_points(dealer_card)

    if user_point == 21 and dealer_point == 21:
        print("You got Draw")
        user_status = False
        dealer_status = False

    elif user_point == 21:
        print("You got blackjack win, congrats")
        user_status = False
        dealer_status = False

    while user_status:
        user_choice_for_continue = input("Do you want to hit or pass? type 'h' for hit & type 'p' for pass\n >> ").lower()
        if user_choice_for_continue == "h":
            draw_card = shuffle_card()
            user_card.append(draw_card)
            user_point = hand_points(user_card)
            
            print(f"Your card are {user_card}")
            print(f"Your points are {user_point}\n")

            if user_point == 21:
                print("You got blackjack win, congrats")
                break

            if user_point > 21:
                print(f"You got bust, you have {user_point} points, dealer win")
                dealer_status = False
                break

        elif user_choice_for_continue == "p":
            print("\nRevealing dealer card")
            show_dealer(dealer_card, reveal=True)
            dealer_point = hand_points(dealer_card)
            break
                
    while dealer_status:
        dealer_point = hand_points(dealer_card)

        if dealer_point < 17:
            draw_card = shuffle_card()
            dealer_card.append(draw_card)
            dealer_point = hand_points(dealer_card)
            print(f"Dealer card: {dealer_card}")
            print(f"Dealer points: {dealer_point}\n")
            continue

        if dealer_point > 21:
            print(f"Dealer got bust, dealer has {dealer_point} points, you win")
            break

        elif dealer_point == user_point:
            print("You have draw")
            break

        elif user_point > dealer_point:
            print("You win")
            break

        else:
            print("Dealer Win")
            break

    while True:
        user_will_continue = input("\nDo you want to play again? type 'y' to reset and type 'q' to quit\n >> ").lower()
        if user_will_continue == "y":
            break
        elif user_will_continue == 'q':
            blackgame_status = False
            break
        else:
            print("Your input is invalid, please try again\n")


