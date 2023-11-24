# Problem Statement -
# Given an array of non-negative integers and a value sum, 
# return a boolean indicating whether it is possible 
# to generate the target sum using numbers from the array.


# with memoization
def can_sum(target, numbers):
    cache = set()
    def _can_sum(_target):
        if _target in cache:
            return False

        if _target == 0:
            return True
        
        for number in numbers:
            q = _target // number
            for j in range(q, 0, -1):
                result = _can_sum(_target - j * number)
                if result:
                    return True
        cache.add(_target)
        return False
    
    result = _can_sum(target)
    cache.clear()
    return result


# # without memoization
# def can_sum(target, numbers):
#     if target == 0:
#         return True
    
#     for number in numbers:
#         q = target // number
#         for j in range(q, 0, -1):
#             result = can_sum(target - j * number, numbers)
#             if result:
#                 return True
#     return False

# # or 
# def can_sum(target, numbers):
#     if target == 0:
#         return True
    
#     if not numbers:
#         return False

#     for i, number in enumerate(numbers):
#         q = target // number
#         temp = numbers[i + 1:]
#         for j in range(q, 0, -1):
#             result = can_sum(target - j * number, temp)
#             if result:
#                 return True
#     return False


if __name__ == "__main__":
    print(can_sum(7, [2, 3]))
    print(can_sum(7, [5, 3, 4, 7]))
    print(can_sum(7, [2, 4]))
    print(can_sum(8, [2, 3, 5]))
    print(can_sum(300, [7, 14]))
    print(can_sum(115123, [3, 34, 4, 12, 5, 2]))
    