import random
import string
from colorama import fore, init
from docs.animals import animal_list
from docs.cars import car_brands
from docs.countries import country_list
from docs.gallows import hangman_display


def hangman_title():
    """
    Game title as the header
    """
    print("""

    _   _                                               
    | | | |                                              
    | |_| |  __ _  _ __    __ _  _ __ ___    __ _  _ __  
    |  _  | / _` || '_ \\\\  / _` || '_ ` _ \\  / _` || '_ \\ 
    | | | || (_| || | | || (_| || | | | | || (_| || | | |
    \\_| |_/ \\__,_||_| |_| \\__, ||_| |_| |_| \\__,_||_| |_|
                        __/ |                         
                        |___/                          
    """
    )

hangman_title()

def get_word_category():
    """
    Select a category from the following 3
    categories
    """
    print("\n Please choose between the following options: \n")
    print("  ---- ANIMALS ---- CARS ---- COUNTRIES ---- \n")
    user_choice = input("").lower()

    print(f"\n You chose {user_choice}, Good luck! \n")

    if user_choice == "cars":
        return car_brands, "cars"
    elif user_choice == "animals":
        return animal_list, "animals"
    elif user_choice == "countries":
        return country_list, "countries"
    else:
        print(f"This option is not valid! Please try again")
    return get_word_category()

def get_random_words(secret_word):
    """
    Generate random words from the
    imported list
    """
    return random.choice(secret_word).upper()

def user_name():
    """
    Requires user to input their
    user name
    """

    while True:
        name = input('Please enter your username: \n')
        if name.isalpha():
            print('Welcome to the game {name}, All the best! \n')
            play_game()
            break
        else:
            print('User name invalid, please use only letters')

def menu():
    """
    Displays the menu choices
    """
    hangman_title()
    menu_options = True
    while menu_options:
        print('Press 1 to start the game')
        print('Press 2 for the rules of the game')
        print('Press 3 to exit the game')
        option = input('Please choose one of the following options: \n')
        if option == '1':
            menu_options = False
            user_name()
            get_word_category()
            play_game()
        elif option == '2':
            menu_options = False
            play_game()
        elif option == '3':
            menu_options = False
            print('Thanks for playing, we hope to see you soon...')
            exit()
        else:
            print(f'sorry,{option}is not a valid option, please choose between 1,2 or 3')
            menu()


def game_end():
    """
    This is the end of the game option screen.
    The user will have the option of either
    playing the game again, or quit the game
    and be redirected to the main menu
    """
    while True:
        print('Would you like to play again?')
        play_again = input("Press 'Y' for Yes or 'N' for No \n")

        if play_again == 'Y':
            play_game()
            break
        elif play_again == 'N':
            print('Thank you for playing. Hope to see you soon... \n')
            enter()
            menu()
        else:
            print("Invalid choice, please chhose between 'Y' or 'N' \n")


def enter():
    """
    This function is for the sole purpose for
    option 2 of the menu function and 'N'
    option in the game_end function. Once the user
    press enter, It will take them back to the main
    menu
    """
    input('Press Enter to be redirected to the Menu')


def rules():
    """
    displays the rule of the
    game
    """
    print(
        """
        Welcome to the game of Hangman!
        The rules are very simple, You have the choice of 3 word categories 
        from cars, countries and animals. Once you choose your category, you
        will then be given a random word, each unsuccesful guesses will a new body
        part to the gallows. After 6 unsuccesful attempts the player will be hunged
        and the game will be over. To be the winner, the player has to guess the
        full word within the allocated 6 guesses

        All the best!
        """
    )
    print('\n')
    menu()


def play_game():
    """
    Starts the game for the user.
    A random word will be picked out
    from the word category selected.
    The player will then guess how many 
    letters are in the word.
    """
    secret_word, category_name = get_word_category()
    answer = random_word(secret_word)
    guessed_letters = set()
    lives = 6 
    print(f"secret word: {secret_word}")
    alpha = set(string.ascii_uppercase)
    print(f'guesses left: {lives}')

    while len(letters_in_secret_word) and lives > 0:
        word_completion = [letter if letter in guessed_letters
                            else " _ " for letter in secret_word]
        print("Guessed letters: ", " ".join(guessed_letters))
        print(f'Lives remaining: {lives}')
        print('Hidden word: ', ''.join(word_completion))
        print(hangman_display(lives))
        guess = input ('Please pick a letter: \n').upper()

        if guess in alpha - guessed_letters:
            guessed_letters.add(guess)
            if guess in letters_in_secret_word:
                letters_in_secret_word.remove(guess)
                print('')
            else:
                lives -= 1
                print(f'{guess} is not in the secret word')
        elif guess in guessed_letters:
            print(f'You have already tried{guess}')
        else:
            print('Invalid character selected, please choose letters only')

    if lives == 0:
        print(hangman_display(lives))
        print(f'Unfortunately you have been hanged. The secret word was{word}')
        game_end()
    else:
        print(f'Congratulations! The correct word was{word}')
    

if __name__== "__main__":
    """
    Start Game
    """
    menu()