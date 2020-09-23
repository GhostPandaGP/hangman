from hangman.main import Hangman
from hangman.main import generate_random_word


def test_check_format_answer():
    hangman = Hangman
    assert hangman.check_format_answer("a"), \
        "Check format answer don't see one char like correct answer."
    assert not hangman.check_format_answer("5"), \
        "Check format answer don't check numbers."


def test_generate_random_word() -> None:
    assert isinstance(generate_random_word(), str), \
        "Generate word is not string."
    assert generate_random_word().isalpha(), \
        "There are extraneous characters."
