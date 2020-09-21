from hangman.main import Hangman
from hangman.main import generate_random_word


def test_check_format_answer():
    hangman = Hangman
    assert hangman.check_format_answer("a"), "Check format answer don't see one char like correct answer"
    # assert not hangman.check_format_answer(5), "Check format answer don't check numbers"
    # assert not hangman.check_format_answer(None), "Check format answer don't work with value None"


def test_generate_random_word() -> None:
    assert type(generate_random_word()) is str, "Generate word is not string"
    assert generate_random_word().isalpha(), "there are extraneous characters"


def test_get_wrong_message() -> None:
    hangman = Hangman
    assert type(hangman.get_wrong_message()) is str, "Not correct format out"


def test_get_correct_message() -> None:
    hangman = Hangman
    assert type(hangman.get_correct_message()) is str, "Not correct format out"
