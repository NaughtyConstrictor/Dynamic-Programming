# Problem Statement -
# Correctly determine the fewest number of coins to be given to a customer 
# such that the sum of the coins' value would equal the correct 
# amount of change.

# For example
# An input of 15 with [1, 5, 10, 25, 100] 
# should return one nickel (5) and one dime (10) or [5, 10]
# An input of 40 with [1, 5, 10, 25, 100] 
# should return one nickel (5) and one dime (10) and one quarter (25) or 
# [5, 10, 25]

from __future__ import annotations
from typing import TypeVar
 
 
T = TypeVar("T")
_CompactItem = tuple[T, int]
 
 
class _CompactList:
    """Helper class for efficient memory management of sequences with
   repeated items.
   """
 
    def __init__(self, items: list[_CompactItem] | None = None) -> None:
        """Initializes the instances items and length.
       
       Items should be a list of tuples `(item, count)`.
       """
        if items is None:
            items = []
        self._items = items
        self._length = sum(count for _, count in self._items)
   
    def __len__(self) -> int:
        """Returns the length of the list (sum of the items' counts)."""
        return self._length
 
    def __add__(self, item: _CompactItem) -> _CompactList:
        """Returns a new list with `item` appended to its end."""
        result = _CompactList(self._items + [item])
        result._length = len(self) + item[1]
        return result
   
    def __radd__(self, item: _CompactItem) -> _CompactList:
        """Returns a new list with `item` appended to its start."""
        result = _CompactList([item] + self._items)
        result._length = len(self) + item[1]
        return result
   
    def expand(self) -> list[T]:
        """Returns the expanded form of the list."""
        expanded = []
        for item, count in self._items:
            expanded.extend([item] * count)
        return expanded
 
 
def find_fewest_coins(coins: list[int], target: int) -> list[int]:
    """Returns a list with the fewest number of coins whose sum is equal
   to target.
 
   Parameters
   ----------
   coins : list[int]
       A list of available coins.
 
   target : int
       The target sum such that `sum(find_fewest_coins(coins, target)) == target`
       (if possible).
 
   Returns
   -------
   list[int]
       Returns the list of coins satisfying the problem conditions.
 
   Raises
   ------
   ValueError
       If the target is negative.
       If the target sum can't be obtained with the given coins.
   """
    if target < 0:
        raise ValueError("target can't be negative")
       
    coins = sorted(coins, reverse=True)
    cache = {}
    def _find_fewest_coins(_coins, _target):
        if _target in cache:
            return cache[_target]
        if _target == 0:
            return _CompactList()
 
        shortest = None
        for i, coin in enumerate(_coins):
            q = _target // coin
            new_coins = _coins[i + 1:]
            for j in range(q, 0, -1):
                sub_shortest = _find_fewest_coins(new_coins, _target - j * coin)
                if sub_shortest is not None:
                    candidate = sub_shortest + (coin, j)
                    if (shortest is None) or (len(candidate) < len(shortest)):
                        shortest = candidate
 
        cache[_target] = shortest
        return shortest
 
    answer = _find_fewest_coins(coins, target)
    cache.clear()
    if answer is None:
        raise ValueError("can't make target with given coins")
   
    return answer.expand()
 