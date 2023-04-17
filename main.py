import functions
import variables


while variables.playing:
    functions.game()
    retry = input("Would you like to play again? Type 'y' or 'n' \n")
    functions.clear_hands()
    if retry == 'n':
        functions.clear()
        print("Thank you for playing.")
        variables.playing = False
