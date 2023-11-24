# Problem Statement -
# Write a function `how_sum(target, numbers)` that takes in a target sum
# and a list of numbers as argument.
# The function should return a list containing any combination of 
# elements that add up to exactly the target sum. If there's no combination
# that adds up to the target sum then return an list.


def how_sum(target, numbers):
    combination = []
    cache = set()
    def _how_sum(_target, _numbers):
        if _target in cache:
            return False
        if _target == 0:
            return True
        if not _numbers:
            return False
        for i, number in enumerate(_numbers):
            q = _target // number
            temp = _numbers[i + 1:]
            for j in range(q, 0, -1):
                if _how_sum(_target - j * number, temp):
                    combination.extend([number] * j)
                    return True
        
        cache.add(_target)
        return False
    
    _how_sum(target, numbers)
    cache.clear()
    return combination

# or
def how_sum(target, numbers):
    cache = set()
    def _how_sum(_target, _numbers):
        if _target in cache:
            return None
        if _target == 0:
            return []
        if not _numbers:
            return None
        for i, number in enumerate(_numbers):
            q = _target // number
            temp = _numbers[i + 1:]
            for j in range(q, 0, -1):
                result = _how_sum(_target - j * number, temp)
                if result is not None:
                    return result + [number] * j
        
        cache.add(_target)
        return None
    
    result = _how_sum(target, numbers)
    cache.clear()
    return result



if __name__ == "__main__":
    print(how_sum(0, [1, 2, 3, 4]))
    print(how_sum(7, [2, 3]))
    print(how_sum(7, [5, 3, 4, 7]))
    print(how_sum(7, [2, 4]))
    print(how_sum(8, [2, 3, 5]))
    print(how_sum(300, [7, 14]))
    print(how_sum(115123, [10, 12, 5, 2, 4, 34, 3]))
    