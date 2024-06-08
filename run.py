# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high
import random
from docs.animals import animal_list
from docs.cars import car_brands
from docs.countries import country_list
from docs.gallows import hangman_display


def hangman_title():
    """
    Game title as the header
    """
    print(
        """

    _   _                                               
    | | | |                                              
    | |_| |  __ _  _ __    __ _  _ __ ___    __ _  _ __  
    |  _  | / _` || '_ \  / _` || '_ ` _ \  / _` || '_ \ 
    | | | || (_| || | | || (_| || | | | | || (_| || | | |
    \_| |_/ \__,_||_| |_| \__, ||_| |_| |_| \__,_||_| |_|
                        __/ |                         
                        |___/                          
    """
    )
