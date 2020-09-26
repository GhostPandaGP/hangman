"""Test module hangman."""
from hangman import check_format_answer, generate_random_word, \
    get_wrong_message, get_correct_message, check_answer
import pytest
from unittest import mock


@pytest.fixture
def words():
    """Fix value words."""
    return {"full": "word", "hidden": "wo**"}


def test_check_format_answer():
    """Test check_format_answer."""
    assert check_format_answer("a"), \
        "Check format answer don't see one char like correct answer."
    assert not check_format_answer("5"), \
        "Check format answer don't check numbers."


@mock.patch("hangman.randint", return_value=11, autospec=True)
def test_generate_random_word_max(mock_randint) -> None:
    """Test generate_random_word on last value."""
    assert generate_random_word(), "Error in end value for generate"


def test_generate_random_word() -> None:
    """Test generate_random_word."""
    assert isinstance(generate_random_word(), str), \
        "Generate word is not string."
    assert generate_random_word().isalpha(), \
        "There are extraneous characters."


def test_get_wrong_message(words):
    """Test get_wrong_message."""
    assert isinstance(get_wrong_message(0, 5, words["hidden"]), str), \
        "Wrong message is not string."


def test_get_correct_message(words):
    """Test get_correct_message."""
    assert isinstance(get_correct_message(words["hidden"]), str), \
        "Correct message is not string."


def test_check_answer(words):
    """Test check_answer."""
    assert check_answer(words["full"], words["hidden"], "r") == "wor*", \
        "Incorrect check answer for existed char"
    assert check_answer(words["full"], words["hidden"], "x") == "wo**", \
        "Incorrect check answer for not existed char"