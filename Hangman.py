from os import system


MAX_TRIES = 6
GREEN = '\033[92m'
RED = '\033[91m'
END = '\033[0m'


def printing_opening_page():
    """prints the opening screen of the hangman game"""

    hangman_ascii_art = ("""      _    _                                         
     | |  | |                                        
     | |__| | __ _ _ __   __ _ _ __ ___   __ _ _ __  
     |  __  |/ _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
     | |  | | (_| | | | | (_| | | | | | | (_| | | | |
     |_|  |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                          __/ |                      
                         |___/\n        
    """)

    print(hangman_ascii_art)


def clear():
    """clears the screen after printing"""
    _ = system('cls')


def check_valid_input(letter_guessed, old_letters_guessed):
    """Checks if the string is a proper guess, and if it was guessed before
    :param letter_guessed: the letter that the user guessed.
    :type letter_guessed: str
    :param old_letters_guessed: the list of the proper guesses of the user that was guessed.
    :type old_letters_guessed: list
    :return: returns true or false if the string fits to be a guess
    :rtype: bool
    """

    letter_guessed_small = letter_guessed.lower()
    abc_check = letter_guessed_small.isalpha()
    length = len(letter_guessed_small)

    if abc_check and length == 1 and letter_guessed_small not in old_letters_guessed:
        return True
    else:
        return False


def try_update_letter_guessed(letter_guessed, old_letters_guessed):
    """Checks if the string is a proper guess, and if it was guessed before
    :param letter_guessed: the letter that the user guessed.
    :type letter_guessed: str
    :param old_letters_guessed: the list of the proper guesses of the user that was guessed.
    :type old_letters_guessed: list
    """
    letter_guessed_small = letter_guessed.lower()
    is_check_good = check_valid_input(letter_guessed, old_letters_guessed)
    if is_check_good is False:
        sorted_list = sorted(old_letters_guessed)
        print(" -> ".join(sorted_list))
    else:
        old_letters_guessed.append(letter_guessed_small)


def show_hidden_word(secret_word, old_letters_guessed):
    """presents the letters from old_letter_guessed that in the string secret_word at the right location
    :param secret_word: the word that was chosen.
    :type secret_word: str
    :param old_letters_guessed: the list of the guesses that the user guessed.
    :type old_letters_guessed: list
    :return: returns the word with "_" in places that were not guessed
    :rtype: str
    """
    length_secret = len(secret_word)
    index1 = 0
    while index1 < length_secret:

        if secret_word[index1] not in old_letters_guessed:
            secret_word = secret_word.replace(secret_word[index1], "_")

        index1 += 1

    new_word = " ".join(secret_word)

    return new_word


def check_win(secret_word, old_letters_guessed):
    """checks if the user won the game
    :param secret_word: the word that was chosen.
    :type secret_word: str
    :param old_letters_guessed: the list of the guesses that the user guessed.
    :type old_letters_guessed: list
    :return: returns the result of the game in it's current stage
    :rtype: bool
    """
    character = "_"
    revealed_letters = show_hidden_word(secret_word, old_letters_guessed)

    if character in revealed_letters:
        return False
    else:
        return True


def return_hangman_status(num_of_tries):
    """prints the hangman status according to the number of wrong tries
    :param num_of_tries: number of wrong tries.
    :type num_of_tries: int
    :return: returns the current status of the hangman
    :rtype: str
    """
    picture_0 = "x-------x"
    picture_1 = ("    x-------x\n"
                 "    |\n"
                 "    |\n"
                 "    |\n"
                 "    |\n"
                 "    |")

    picture_2 = ("    x-------x\n"
                 "    |       |\n"
                 "    |       0\n"
                 "    |\n"
                 "    |\n"
                 "    |")

    picture_3 = ("    x-------x\n"
                 "    |       |\n"
                 "    |       0\n"
                 "    |       |\n"
                 "    |\n"
                 "    |")

    picture_4 = ("    x-------x\n"
                 "    |       |\n"
                 "    |       0\n"
                 "    |      /|\\\n"
                 "    |\n"
                 "    |")

    picture_5 = ("    x-------x\n"
                 "    |       |\n"
                 "    |       0\n"
                 "    |      /|\\\n"
                 "    |      /\n"
                 "    |")

    picture_6 = ("    x-------x\n"
                 "    |       |\n"
                 "    |       0\n"
                 "    |      /|\\\n"
                 "    |      / \\\n"
                 "    |")

    hangman_dictionary = {0: picture_0, 1: picture_1, 2: picture_2, 3: picture_3, 4: picture_4, 5: picture_5,
                          6: picture_6}
    return hangman_dictionary[num_of_tries]


def choose_word(file_path, index):
    """chooses a word for the game according to a number
    :param file_path: the path of the file that contains the words.
    :type file_path: str
    :param index: the place of the wod in the file.
    :type index: int
    :return: returns the word in the place of the index
    :rtype: str
    """
    file = open(file_path, "r")
    words_list = file.read().split(" ")
    num_of_words = len(words_list)
    if index > 0:
        if index > num_of_words:
            number_of_times = index % num_of_words
            word_location = number_of_times - 1
        elif index <= num_of_words:
            word_location = index - 1
    file.close()
    return words_list[word_location]


def is_game_over(num_of_tries, secret_word, old_letters_guessed):
    check_victory = check_win(secret_word, old_letters_guessed)

    if (check_victory is True) or (num_of_tries >= MAX_TRIES):
        return True
    else:
        return False


def main():
    printing_opening_page()
    file_path = input("Enter file path:")
    word_index = int(input("Enter index:"))
    secret_word = choose_word(file_path, word_index)
    clear()
    print("Let’s start!")
    old_letters_guessed = []
    num_of_tries = 0
    print(return_hangman_status(num_of_tries))
    print(show_hidden_word(secret_word, old_letters_guessed))
    game_status = is_game_over(num_of_tries, secret_word, old_letters_guessed)

    while game_status is False:

        letter_guessed = input("Guess a letter:")
        is_letter = check_valid_input(letter_guessed, old_letters_guessed)
        clear()
        if is_letter is True:
            if (letter_guessed in secret_word) and (letter_guessed not in old_letters_guessed):
                try_update_letter_guessed(letter_guessed, old_letters_guessed)
                print(GREEN + return_hangman_status(num_of_tries) + END)
                show_word = show_hidden_word(secret_word, old_letters_guessed)
                print("\n")
                print(show_word)
            else:
                num_of_tries += 1
                print(RED + ":(\n" + END)
                print(RED + return_hangman_status(num_of_tries) + END)
                print("\n\n")
                show_word = show_hidden_word(secret_word, old_letters_guessed)
                try_update_letter_guessed(letter_guessed, old_letters_guessed)
                print(show_word)

        else:
            if letter_guessed.lower() in old_letters_guessed:
                print(RED + "X")
                try_update_letter_guessed(letter_guessed, old_letters_guessed)
                print(END)
            else:
                print(RED + "X" + END)
        game_status = is_game_over(num_of_tries, secret_word, old_letters_guessed)
    check_if_user_win = check_win(secret_word, old_letters_guessed)

    if check_if_user_win is True:
        print(GREEN + "WIN")
    else:
        print(RED + "LOSE")


if __name__ == "__main__":
    main()

