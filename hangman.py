import random


class Hangman:

    def __init__(self, word):
        self.word = word
        self.hidden_word = "*" * len(word)
        self.total_attempt = 5
        self.number_attempt = 0
        self.game_process = 0

    @staticmethod
    def check_format_answer(answer: str) -> bool:
        return answer.isalpha() and len(answer) == 1

    @staticmethod
    def get_answer() -> str:
        print("Guess a letter:")
        return input()

    def show_wrong_message(self) -> None:
        print(f"Missed, mistake {self.number_attempt} out of {self.total_attempt}\n\n"
              f"The word: {self.hidden_word}\n")

    def show_correct_message(self) -> None:
        print(f"Hit!\n\n"
              f"The word: {self.hidden_word}\n")

    def check_answer(self, answer: str):

        if not self.check_format_answer(answer):
            print(f"Wrong format! Please input one char!")
            return False

        if answer in self.word:
            self.hidden_word = "".join([answer if self.word[i] == answer else x for i, x in enumerate(self.hidden_word)])
            self.show_correct_message()
        else:
            self.number_attempt += 1
            self.show_wrong_message()

        if self.hidden_word == self.word:
            self.game_process = 0
            print("You won!")
        if self.number_attempt == self.total_attempt:
            self.game_process = 0
            print("You lost!")

    def run(self):
        self.game_process = 1
        while self.game_process:
            answer = self.get_answer()
            self.check_answer(answer)


if __name__ == '__main__':
    secret_word = ["root", "handsomely", "incandescent", "field", "prose", "hat", "teeny", "pets", "cry",
                   "wandering", "identify", "guitar"]
    game = Hangman(secret_word[random.randint(0, len(secret_word))])
    game.run()
