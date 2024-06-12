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

def get_random_words(secret_word):
    """
    Generate random words from the
    imported list
    """
    word = random.choice(secret_word)
    while "-" in word or " " in words:
        word = random.choice(secret_word)
    return word.upper()





