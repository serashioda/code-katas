"""Implementation of the autocomplete module."""


class AutoCompleter():
    """Auto completer class."""

    def __init__(self, vocabulary, max_completions=4):
        """Instantiate with vocabulary and max_compete params."""
        self.vocabulary = vocabulary
        self.max_completions = max_completions

    def complete(self, term):
        """Auto complete method."""
        suggested_words = []
        n = len(term)
        for word in self.vocabulary:
            if word[:n] == term:
                suggested_words.append(word)
                if len(suggested_words) >= self.max_completions:
                    return suggested_words
        return suggested_words
