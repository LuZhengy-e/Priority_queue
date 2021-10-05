import logging

logging.basicConfig(level=logging.DEBUG)

from Compare.compare import ArrayCompare
from priority_queue import Priority_queue

# test1
logging.info("---------test1-----------")
a = [1, 2, 3, 4, 5, 5, 5, 7, 8, 8, 8]
queue = Priority_queue(a)
for i in range(len(queue)):
    print(queue.pop())

logging.info("--------test2---------")
a = [1, 2, 3, 4, 5, 5, 5, 7, 8, 8, 8]
queue = Priority_queue()
for s in a:
    queue.push(s)
    print(queue.top())

logging.info("----------test3----------")
a = [1, 2, 3, 4, 5, 6]
queue = Priority_queue(a)
queue.change(3, 8)
print(queue.top())
for i in range(len(queue)):
    print(queue.pop())

logging.info("-----------test4---------")
a = [(1, 2, 3), (1, 2), (2, 1, 3), (2, 2), (4, 1), (0, 2), (0, 1, 2), (0, 1)]
queue = Priority_queue(a, Compare=ArrayCompare)
for i in range(len(queue)):
    print(queue.pop())

# test5
logging.info("--------test5---------")
a = [(1, 2), (1, 3), (2, 1), (2, 2), (4, 1), (0, 2), (0, 1)]


class Node:
    def __init__(self, key, val):
        self.first = key
        self.second = val

    def __eq__(self, other):
        return self.first == other.first and self.second == other.second

    def __lt__(self, other):
        if self.first < other.first:
            return True

        elif self.first > other.first:
            return False

        else:
            return self.second < other.second


queue = Priority_queue()
for k, v in a:
    queue.push(Node(k, v))
    print(queue.top().first, queue.top().second)
