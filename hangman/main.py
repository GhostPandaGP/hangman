"""Game Hangman.

Computer thinks of a random word and you tries to guess
it by suggesting letters within a certain number of guesses.
"""
import random


class Hangman:
    """This class implements the game hangman.

    Class Hangman get world and give interface for process game
    Use method run that start
    """

    def __init__(self, word: str):
        """Set the transmitted word as secret.

        :param word: str
        """
        self.word = word
        self.hidden_word = "*" * len(word)
        self.total_attempt = 5
        self.number_attempt = 0
        self.game_process = 0

    @staticmethod
    def check_format_answer(answer: str) -> bool:
        """Check format answer.

        Returns True if one characters are alphabet letters (a-z)
        :param answer: str
        :return: bool
        """
        return answer.isalpha() and len(answer) == 1

    @staticmethod
    def get_answer() -> str:
        """Welcome user.

         It make welcome and gets the value from the user.
        :return: str
        """
        print("Guess a letter:")
        return input()

    def get_wrong_message(self) -> str:
        """Return a output line.

        Use this method when the user was wrong.
        :return: str
        """
        return f"Missed, mistake {self.number_attempt} " \
               f"out of {self.total_attempt}\n\n" \
               f"The word: {self.hidden_word}\n"

    def get_correct_message(self) -> str:
        """Return a output line.

        Use this method when the user was correct.
        :return: str
        """
        return f"Hit!\n\n" \
               f"The word: {self.hidden_word}\n"

    def check_answer(self, answer: str):
        """Validate answer user.

        Get the user's response and outputs the response as appropriate.
        :param answer: char
        :return: None
        """
        if not self.check_format_answer(answer):
            print("Wrong format! Please input one char!")
            return

        if answer in self.word:
            self.hidden_word = "".join([
                answer
                if self.word[i] == answer
                else x
                for i, x in enumerate(self.hidden_word)])
            print(self.get_correct_message())
        else:
            self.number_attempt += 1
            print(self.get_wrong_message())

        if self.hidden_word == self.word:
            self.game_process = 0
            print("You won!")
        if self.number_attempt == self.total_attempt:
            self.game_process = 0
            print("You lost!")

    def run(self):
        """Start game.

        Use this method that start game.
        :return:
        """
        self.game_process = 1
        while self.game_process:
            answer = self.get_answer()
            self.check_answer(answer)


def generate_random_word() -> str:
    """Generate word.

    This function generate random word from a given list.
    :return:
    """
    secret_word = ["root", "handsomely", "incandescent", "field",
                   "prose", "hat", "teeny", "pets", "cry",
                   "wandering", "identify", "guitar"]
    return secret_word[random.randint(0, len(secret_word))]


if __name__ == '__main__':
    game = Hangman(generate_random_word())
    game.run()
