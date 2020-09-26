"""Game Hangman.

Computer thinks of a random word and you tries to guess
it by suggesting letters within a certain number of guesses.
"""
from random import randint


def check_format_answer(answer: str) -> bool:
    """Check format answer.

    Returns True if one characters are alphabet letters (a-z)
    :param answer: str
    :return: bool
    """
    return answer.isalpha() and len(answer) == 1


def get_answer() -> str:
    """Welcome user.

     It make welcome and gets the value from the user.
    :return: str
    """
    print("Guess a letter:")
    return input()


def get_wrong_message(
    current_attempt: int,
    total_attempt: int,
    hidden_word: str
) -> str:
    """Return a output line.

    Use this method when the user was wrong.
    :param current_attempt: int
    :param total_attempt: int
    :param hidden_word: str
    :return:
    """
    return f"Missed, mistake {current_attempt} " \
           f"out of {total_attempt}\n\n" \
           f"The word: {hidden_word}\n"


def get_correct_message(hidden_word: str) -> str:
    """Return a output line.

    Use this method when the user was correct.
    :param hidden_word: str
    :return:
    """
    return f"Hit!\n\n" \
           f"The word: {hidden_word}\n"


def check_answer(
    word: str,
    hidden_word: str,
    char: str
) -> str:
    """Validate answer user.

    Get the user's response and outputs the response as appropriate.
    if char in word than return hidden word.
    :param word: str
    :param hidden_word: str
    :param char: str(1)
    :return:
    """
    if not check_format_answer(char):
        print("Wrong format! Please input one char!")
        return hidden_word

    return "".join([
        char
        if word[i] == char
        else x
        for i, x in enumerate(hidden_word)]) if char in word \
        else hidden_word


def play_hangman(word: str, total_attempt: int):
    """Start game.

    Use this function that start game.
    :param word:
    :param total_attempt:
    :return:
    """
    current_attempt = 0
    hidden_word = "*" * len(word)
    while True:
        char = get_answer()
        tmp_hidden_word = check_answer(word, hidden_word, char)
        if tmp_hidden_word == hidden_word:
            current_attempt += 1
            print(get_wrong_message(current_attempt,
                                    total_attempt, hidden_word))
        else:
            hidden_word = tmp_hidden_word
            print(get_correct_message(hidden_word))

        if hidden_word == word:
            print("You won!")
            break
        if current_attempt == total_attempt:
            print("You lost!")
            break


def generate_random_word() -> str:
    """Generate word.

    This function generate random word from a given list.
    :return:
    """
    secret_word = ["root", "handsomely", "incandescent", "field",
                   "prose", "hat", "teeny", "pets", "cry",
                   "wandering", "identify", "guitar"]
    return secret_word[randint(0, len(secret_word) - 1)]


if __name__ == '__main__':
    word_in = generate_random_word()
    TOTAL_ATTEMPT_IN = 5
    play_hangman(word_in, TOTAL_ATTEMPT_IN)
