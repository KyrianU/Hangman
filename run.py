import random
import string
from os import system, name
from docs.words import words
from colorama import Fore, init
from ascii_art import trophy, thanks, lets_go, loser
from docs.gallows import hangman_display

init()
# Initialises Colorama


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
    """)


hangman_title()


def get_random_words(words):
    """
    Generate random words from the
    imported list
    """
    word = random.choice(words)
    while "-" in word or " " in words:
        word = random.choice(words)
    return word.upper()


def user_name():
    """
    Requires user to input their
    user name
    """

    while True:
        name = input('Please enter your username: \n')
        if name.isalpha():
            print(f'{Fore.BLUE}Welcome to the game {name},All the best!{Fore.RESET} \n')
            lets_go()
            play_game()
            break
        else:
            print(f'{Fore.RED}User name invalid, please use only letters{Fore.RESET}')
        return name


def menu():
    """
    Displays the menu choices
    """

    menu_options = True
    while menu_options:
        print(f'{Fore.BLUE}Press 1 to start the game{Fore.RESET}')
        print(f'{Fore.YELLOW}Press 2 for the rules of the game{Fore.RESET}')
        print(f'{Fore.RED}Press 3 to exit the game{Fore.RESET}')
        option = input('Please choose one of the following options: \n')
        if option == '1':
            menu_options = False
            clear_screen()
            user_name()
            play_game()
        elif option == '2':
            menu_options = False
            clear_screen()
            rules()
        elif option == '3':
            menu_options = False
            print('Thanks for playing, we hope to see you soon...')
            exit()
        else:
            print(f'{Fore.RED}Sorry,{option} is not a valid option, please choose between 1,2 or 3{Fore.RESET}')
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
            thanks()
            enter()
            clear_screen()
            hangman_title()
            menu()
        else:
            print("Invalid choice, please choose between 'Y' or 'N' \n")


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
        The rules are very simple, you are given a random word, to
        which you have 6 attempts at guessing it correctly. 
        Eeach unsuccesful guesses will add a new 
        body part to the gallows. After 6 unsuccesful
        attempts the player will be hunged and the game will be 
        over. To be the winner, the player has to guess the
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
    word = get_random_words(words).upper()
    answer = "_" * len(word)
    letters_in_words = set(word)
    guessed_letters = set()
    lives = 6
    print(answer)
    alpha = set(string.ascii_uppercase)
    print(f'guesses left: {lives}')

    while len(letters_in_words) and lives > 0:
        word_completion = [letter if letter in guessed_letters
                           else " _ " for letter in word]
        print("Guessed letters: ", " ".join(guessed_letters))
        print(f'Lives remaining: {lives}')
        print('answer: ', ''.join(word_completion))
        print(hangman_display(lives))
        guess = input('Please pick a letter: \n').upper()

        if guess in alpha - guessed_letters:
            guessed_letters.add(guess)
            if guess in letters_in_words:
                letters_in_words.remove(guess)
                print(f'{Fore.GREEN} Well done! {guess} is in the word.{Fore.RESET}')
            else:
                lives -= 1
                print(f'{Fore.RED}{guess} is not in the secret word{Fore.RESET}')
        elif guess in guessed_letters:
            print(f'{Fore.RED}You have already tried {guess}{Fore.RESET}')
        else:
            print('Invalid character selected, please choose letters only')

    if lives == 0:
        print(hangman_display(lives))
        loser()
        print(f'{Fore.RED}Unfortunately you have been hanged. The secret word was {word}{Fore.RESET}')
        game_end()
    else:
        print(f'{Fore.GREEN}Congratulations! The correct word was {word}{Fore.RESET}')
        trophy()
        game_end()
        clear_screen()


def clear_screen():
    """
    Clears Terminal
    """
    # taken from https://www.geeksforgeeks.org/clear-screen-python/
    # for windows
    if name == 'nt':
        _ = system('cls')

    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')


if __name__== "__main__":
    """
    Start Game
    """
    menu()