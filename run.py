import random
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

def get_random_words(secret_word):
    """
    Generate random words from the
    imported list
    """
    word = random.choice(secret_word)
    while "-" in word or " " in words:
        word = random.choice(secret_word)
    return word.upper()

def user_name():
    """
    Requires user to input their
    user name
    """

    while True:
        user_name = input('Please enter your username: \n')
        if name.isalpha():
            print('Welcome to the game{user_name}, All the best! \n')
            play_game()
            break
        else:
            print('User name invalid, please use only letters')




def play_game():
    """
    Starts the game for the user.
    A random word will be picked out
    from the word category selected.
    The player will then guess how many 
    letters are in the word.
    """
    secret_word, category_name = get_word_category()
    secret_word = "_" * len(word)
    letters_in_secret_word = set(word)
    guessed_letters = set(word)
    lives = 6 
    print(secret_word)
    




