"""Implementation of the Kata Proper Parenthetics."""


def parenthetics(uni_string):
    """Take unicode string as input and return value."""
    stack = Stack()
    charac_array = list(uni_string)
    for charac in charac_array:
        if charac == '(':
            stack.push(charac)
        elif charac == ')':
            if stack.size() == 0:
                return -1
            else:
                stack.pop()
    if stack.size() == 0:
        return 0
    elif stack.size() > 0:
        return 1


class Stack(object):
    """Create stack of parenthetics."""

    def __init__(self):
        """Create a new stack, from LinkedList using composition."""
        self._linkedlist = LinkedList()

    def push(self, value):
        """Push a new value on top of the stack."""
        self._linkedlist.push(value)

    def size(self):
        """Return side of a."""
        return self._linkedlist.size()

    def pop(self):
        """Pop the first value of the stack."""
        return self._linkedlist.pop()


"""Python implementation of a linked list."""


class Node():
    """Instantiate a Node."""

    def __init__(self, value=None, next=None):
        """Instantiate a node with value and next params."""
        self.value = value
        self.next = next


class LinkedList():
    """Instantiate a Linked List."""

    def __init__(self):
        """Instantiate an empty Linked list."""
        self.head = None

    def push(self, val):
        """Push a new node as the head of the linked list."""
        new_node = Node(val, self.head)
        self.head = new_node

    def pop(self):
        """Pop first value off linked list and return value."""
        # if self.head is None:
        if self.head is not None:
            pop_head = self.head.value
            self.head = self.head.next
            return pop_head
        else:
            raise IndexError('cannot pop from empty list')

    def size(self):
        """Return the length of the linked list."""
        if self.head is not None:
            size = 1
            curr = self.head
            while curr.next is not None:
                size += 1
                curr = curr.next
            return size
        return 0
