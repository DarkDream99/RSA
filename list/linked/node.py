class Node(object):
    def __init__(self, value):
        self._value = value
        self._next_node = None

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, new_value):
        self._value = new_value

    def add_next(self, node):
        self._next_node = node
