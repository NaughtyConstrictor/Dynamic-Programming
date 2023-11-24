# Problem Statement -
# Write a function `best_sum(target, numbers)` that takes in a target sum
# and a list of numbers as argument.
# The function should return a list containing the shortest combination of 
# elements that add up to exactly the target sum. 
# If there's a tie for the shortest combination you may return any one of 
# the shortest.

def best_sum(target, numbers):
    cache = {}
    def _best_sum(_target, _numbers):
        if _target in cache:
            return cache[_target]
        if _target == 0:
            return []
        
        shortest = None
        for i, number in enumerate(_numbers):
            q = _target // number
            new_numbers = _numbers[i + 1:]
            for j in range(q, 0, -1):
                answer = _best_sum(_target - j * number, new_numbers)
                if answer is not None:
                    candidate = answer + [number] * j
                    if (shortest is None) or len(candidate) < len(shortest):
                        shortest = candidate
        cache[_target] = shortest
        return shortest
    
    return _best_sum(target, numbers)


if __name__ == "__main__":
    print(best_sum(0, [1, 2, 3, 4]))
    print(best_sum(7, [2, 3]))
    print(best_sum(7, [5, 3, 4, 7]))
    print(best_sum(7, [2, 4]))
    print(best_sum(8, [2, 3, 5]))
    print(best_sum(8, [1, 4, 5]))
    print(best_sum(300, [7, 14]))
    print(best_sum(100, [1, 2, 5, 25]))
    print(best_sum(99, [1, 2, 5, 25]))
   


class _CompactList:
    def __init__(self, items=None):
        if items is None:
            items = [] 
        self._items = items
        self._length = 0
    
    def __len__(self):
        return self.length

    def __add__(self, item):
        result = _CompactList(self._items + [item])
        result._length += item[1]
        return result
    
    def __radd__(self, item):
        self + item
    
    def expand(self):
        expanded = []
        for item, count in self._items:
            expanded.extend([item] * count)
        return expanded


def find_fewest_coins(coins, target):
    if target < 0:
        raise ValueError("target can't be negative")
        
    coins = sorted(coins, reverse=True)
    cache = {}
    def _find_fewest_coins(_coins, _target):
        if _target in cache:
            return cache[_target]
        if _target == 0:
            return _CompactList

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
    