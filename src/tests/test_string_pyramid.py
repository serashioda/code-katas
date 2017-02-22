"""Test string pyramid implementations."""

from string_pyramid import (
    watch_pyramid_from_the_side,
    watch_pyramid_from_above,
    count_visible_characters_of_the_pyramid,
    count_all_characters_of_the_pyramid
)


def test_side_empty():
    """Test watch_from_the_side works on empty string."""
    assert watch_pyramid_from_the_side('') == ''


def test_side_none():
    """Test watch_from_the_side works on None."""
    assert watch_pyramid_from_the_side(None) is None


def test_above_empty():
    """Test watch_from_the_side works on empty string."""
    assert watch_pyramid_from_above('') == ''


def test_above_none():
    """Test watch_from_the_side works on None."""
    assert watch_pyramid_from_above(None) is None


def test_count_visible_empty():
    """Test count_visible_characters_of_the_pyramid works on empty string."""
    assert count_visible_characters_of_the_pyramid('') == -1


def test_count_all_empty():
    """Test count_all_characters_of_the_pyramid works on empty string."""
    assert count_all_characters_of_the_pyramid('') == -1


def test_count_visible_none():
    """Test count_visible_characters_of_the_pyramid works on none."""
    assert count_visible_characters_of_the_pyramid('') == -1


def test_count_all_none():
    """Test count_all_characters_of_the_pyramid works on none."""
    assert count_all_characters_of_the_pyramid('') == -1


def test_pyramid_from_side_handles_two_characters():
    """Test watch_pyramid_from_the_side can handl 2 character case."""
    assert watch_pyramid_from_the_side('*#') == ' # \n***'


def test_pyramid_from_above_handles_two_characters():
    """Test watch_pyramid_from_above can handl 2 character case."""
    assert watch_pyramid_from_above('*#') == '***\n*#*\n***'
