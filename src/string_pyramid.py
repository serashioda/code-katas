"""Implementation of the string pyramid."""


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
    c = len(characters)
    rows = []

    for i in range(c):
        num_repeat = (c - (i + 1)) * 2 + 1
        pre_pend = ''
        post_pend = ''
        if i > 0:
            pre_pend = characters[:i]
            post_pend = characters[0:i][::-1]
        rows.append(pre_pend + characters[i] * num_repeat + post_pend)

    for row in rows[::-1][1:]:
        rows.append(row)
    return '\n'.join(rows)
