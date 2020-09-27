"""Test module hangman."""
import pytest
from hangman import check_format_answer, generate_random_word, \
    get_wrong_message, get_correct_message, check_answer


def test_check_format_answer():
    """Test check_format_answer."""
    assert check_format_answer("a"), \
        "Check format answer don't see one char like correct answer."
    assert not check_format_answer("5"), \
        "Check format answer don't check numbers."


def test_generate_random_word() -> None:
    """Test generate_random_word."""
    assert isinstance(generate_random_word(), str), \
        "Generate word is not string."
    assert generate_random_word().isalpha(), \
        "There are extraneous characters."


def test_get_wrong_message():
    """Test get_wrong_message."""
    assert isinstance(get_wrong_message(0, 5, "wo**"), str), \
        "Wrong message is not string."


def test_get_correct_message():
    """Test get_correct_message."""
    assert isinstance(get_correct_message("wo**"), str), \
        "Correct message is not string."


def test_check_answer():
    """Test check_answer."""
    assert check_answer("word", "wo**", "r") == "wor*", \
        "Incorrect check answer for existed char"
    assert check_answer("word", "wo**", "x") == "wo**", \
        "Incorrect check answer for not existed char"
