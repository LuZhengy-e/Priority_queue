import os
import sys
from collections import Iterable
from copy import deepcopy
from Compare.compare import StandardCompare


class Priority_queue:
    def __init__(self, arr=None, Compare=StandardCompare):
        if arr is not None:
            if not isinstance(arr, Iterable):
                raise TypeError("Input must be iterable")
            self._arr = deepcopy(arr)
        else:
            self._arr = []
        self._compare = Compare()
        self._build_maxheap()

    def _swap(self, i, j):
        assert i < len(self._arr) and j < len(self._arr), "Index out of range"
        self._arr[i], self._arr[j] = self._arr[j], self._arr[i]

    def _shift_down(self, i):
        left = 2 * i + 1
        right = 2 * i + 2
        largest = i

        if left < len(self._arr) and self._compare(self._arr[largest], self._arr[left]):
            largest = left

        if right < len(self._arr) and self._compare(self._arr[largest], self._arr[right]):
            largest = right

        if largest != i:
            self._swap(i, largest)
            self._shift_down(largest)

    def _shift_up(self, i):
        fa = (i - 1) // 2
        smallest = i

        if fa >= 0 and self._compare(self._arr[fa], self._arr[smallest]):
            smallest = fa

        if smallest != i:
            self._swap(i, smallest)
            self._shift_up(smallest)

    def _build_maxheap(self):
        for i in range(len(self._arr) // 2, -1, -1):
            self._shift_down(i)

    def push(self, obj):
        i = len(self._arr)
        self._arr.append(obj)

        self._shift_up(i)

    def pop(self):
        assert len(self._arr) > 0, "Index out of range"

        self._swap(0, len(self._arr) - 1)
        ans = self._arr.pop()

        self._shift_down(0)

        return ans

    def top(self):
        assert len(self._arr) > 0, "Index out of range"

        return self._arr[0]

    def change(self, obj, new_obj):
        idx = 0
        for old in self._arr:
            if old == obj:
                self._arr[idx] = new_obj
                self._shift_up(idx)
                self._shift_down(idx)
                break

            idx += 1

        if idx == len(self._arr):
            raise IndexError(f"{obj} not in this queue")

    def __len__(self):
        return len(self._arr)
