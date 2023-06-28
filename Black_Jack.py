import random
# Game rules
print("Game Rules:")
print("- The deck is unlimited in size.")
print("- There are no jokers.")
print("- The Jack/Queen/King all count as 10.")
print("- The Ace can count as 11 or 1.")
print("- The computer is the dealer.")
print("--------------------------------------------------")
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def adjust_ace_value(card_list):
    if 11 in card_list and sum(card_list) > 21:
        card_list.remove(11)
        card_list.append(1)
    return sum(card_list)

def my_play_game():
    cards_sel = random.choice(cards)
    cards_sel1 = random.choice(cards)
    my_list = [cards_sel, cards_sel1]
    summ = adjust_ace_value(my_list)
    print(f"Your deck contains {my_list} and the total is {summ}\n")
    cards_sel_c = random.choice(cards)
    cards_sel1_c = random.choice(cards)
    comp_list = [cards_sel_c, cards_sel1_c]
    sumc = adjust_ace_value(comp_list)
    print("First card of the computer is", cards_sel_c)

    should_continue = True

    while should_continue:
        if input("Enter 'y' if you want to draw another card, or 'n' to stop:\n ").lower() == "y":
            cards_sel3 = random.choice(cards)
            my_list.append(cards_sel3)
            summ = adjust_ace_value(my_list)
            print(f"Your cards are {my_list} and the total is {summ}\n")
            cards_sel3_c = random.choice(cards)
            comp_list.append(cards_sel3_c)
            sumc = adjust_ace_value(comp_list)

            if summ >= 22:
                print(f"You lost! It's a bust. Your cards are {my_list}, the total is {summ}\n")
                print(f"The computer won, and its cards are {comp_list}, the total is {sumc}\nThank you")
                should_continue = False
            elif sumc >= 22:
                print(f"You won! The computer lost. It's a bust.\n Your cards are {my_list}, the total is {summ}\n")
                print(f"The computer's cards are {comp_list}, the total is {sumc}\nThank you")
                should_continue = False
            elif summ==21 or sumc==21:
              if summ==21: 
                print(f"you won and its Black Jack for you, Your cards are {my_list}, the total is {summ}\n")
                print(f"The computer lost, and its cards are {comp_list}, the total is {sumc}\nThank you")
                should_continue = False
              else:
                print(f"you lost and its Black Jack for computer, Your cards are {my_list}, the total is {summ}\n")
                print(f"The computer won, and its cards are {comp_list}, the total is {sumc}\nThank you")
                should_continue = False
            else:
                print("It's a draw")
                print(f"\nYour cards are {my_list}, the total is {summ}\n")
                print(f"The computer cards are {comp_list}, the total is {sumc}\nThank you")
                should_continue = False
        elif sumc > summ:
            print(f"You lost! Your cards are {my_list}, the total is {summ}\n")
            print(f"The computer won, and its cards are {comp_list}, the total is {sumc}\nThank you")
            should_continue = False
        elif summ > sumc:
            print(f"You won! Your cards are {my_list}, the total is {summ}\n")
            print(f"The computer lost, and its cards are {comp_list}, the total is {sumc}\nThank you")
            should_continue = False

if input("Enter 'y' if you want to play, or 'n' to exit\n ").lower() == "y":
    my_play_game()
else:
    print("Thank you")
