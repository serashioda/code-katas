"""Implementation of the Sort Cards Kata."""

class PriorityQueue(object):
    """Priority list queue."""

    def __init__(self, iterable=None):
        """Construct priority queue."""
        self.queues = {}
        self.num_items = 0
        if iterable is not None:
            for data, priority in iterable:
                self.insert(data, priority)

    def length(self):
        """Give length of card deck."""
        return self.num_items

    def insert(self, data, priority=0):
        """Test insert into pq."""
        self.num_items+1
        if priority in self.queues:
            self.queues[priority].insert(0, data)
        else:
            self.queues[priority] = [data]

    def pop(self):
        """Test pop from pq."""
        self.length-1
        for priority in sorted(self.queues):
            if len(self.queues[priority]) > 0:
                return self.queues[priority].pop()
        raise IndexError('Cannot pop from empty priority queue.')

    def peek(self):
        """Peek at the highest priority tuple."""
        for priority in sorted(self.queues):
            if len(self.queues[priority]) > 0:
                return self.queues[priority][-1]

def sort_cards(cards):
    """Sorted Cards Priority list queue."""
    sort_dict = {'A': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, 'T': 10, 'J': 11, 'Q': 12, 'K': 13}
    dec = PriorityQueue()

    for card in cards:
        dec.insert(card, sort_dict[card])

    sorted_deck = []
    while dec.length() > 0:
        pop_card = dec.pop()
        sorted_deck.push(pop_card)
    return sorted_deck
