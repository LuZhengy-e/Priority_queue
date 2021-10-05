"""
@author: Lu Zhengye
@data: 2021.10.05
@func: Compare function
"""
from collections import Iterable


class BaseCompare:
    def __call__(self, _lhs, _rhs):
        raise NotImplementedError


class StandardCompare(BaseCompare):
    def __call__(self, _lhs, _rhs):
        try:
            return _lhs < _rhs

        except TypeError:
            raise TypeError("Not define '<' function of two objects")


class ArrayCompare(BaseCompare):
    def __call__(self, _lhs, _rhs):
        assert isinstance(_lhs, Iterable) and isinstance(_rhs, Iterable), \
            "Object must be iterable"

        try:
            if len(_rhs) == 0:
                return False

            if len(_lhs) == 0:
                return True

            i = 0
            while i < len(_lhs) and i < len(_rhs):
                if _lhs[i] < _rhs[i]:
                    return True

                elif _lhs[i] > _rhs[i]:
                    return False

                else:
                    i += 1

            if len(_rhs) == i:
                return False

            if len(_lhs) == i:
                return True

        except TypeError:
            raise TypeError("Not define '<' function of two objects")


if __name__ == '__main__':
    a = ["+"]
    b = [1]
    c = ArrayCompare()
    print(c(a, b))
