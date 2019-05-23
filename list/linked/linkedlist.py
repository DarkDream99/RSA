from typing import List

from list.linked.node import Node


class LinkedList(object):

    def __init__(self, value_list: List):
        if len(value_list) == 0:
            self._root = Node()
            self._last = self._root
        else:
            self._root = Node(value_list[0])
            self._last = self._root

            for i in range(1, len(value_list)):
                self._last.add_next(Node(value_list[i]))
                self._last = self._last.next_node

    def add(self, value):
        new_node = Node(value)
        self._last.add_next(new_node)
        self._last = new_node

    def __iter__(self):
        curr_node = self._root

        while not curr_node.is_leaf():
            yield curr_node.value
            curr_node = curr_node.next_node
