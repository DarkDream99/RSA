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

        self._curr_node = self._root
        self._index = 0

    def add(self, value):
        new_node = Node(value)
        self._last.add_next(new_node)
        self._last = new_node

    def get_by_index(self, index):
        if index > self._index:
            while index > self._index:
                self._curr_node = self._curr_node.next_node
                self._index += 1
        elif index < self._index:
            self._curr_node = self._root
            self._index = 0
            while index > self._index:
                self._curr_node = self._curr_node.next_node
                self._index += 1

        return self._curr_node.value

    def update_from_current(self, values: List[tuple]):
        curr_node = self._curr_node
        index = self._index

        for value in values:
            ind = value[0]
            new_value = value[1]
            while index != ind and not curr_node.is_leaf():
                curr_node = curr_node.next_node
                index += 1
            curr_node.value = new_value

    def __iter__(self):
        self._curr_node = self._root
        self._index = 0

        while not self._curr_node.is_leaf():
            yield self._curr_node.value
            self._curr_node = self._curr_node.next_node
            self._index += 1
