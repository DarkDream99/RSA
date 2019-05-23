class Node(object):
    def __init__(self, value=None):
        self._value = value
        self._next_node = None

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, new_value):
        self._value = new_value

    @property
    def next_node(self):
        return self._next_node

    def add_next(self, node):
        self._next_node = node

    def is_leaf(self):
        return self._next_node is None
