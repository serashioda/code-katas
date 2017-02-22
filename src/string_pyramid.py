"""Implementation of the string_pyramid."""

def watch_pyramid_from_the_side(characters):
    """Display side of pyramid."""

    characters = characters[::-1]
    c = len(characters)
    rows = []

    for i in range(c):
        empty_space = c - (i + 1)
        num_repeat = (i * 2) + 1
        rows.append(' ' * empty_space + characters[i] * num_repeat + ' ' * empty_space)
    return '\n'.join(rows)


def watch_pyramid_from_above(characters):
    """Display pyramid from above."""
