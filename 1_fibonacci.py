# Using memoization
def fib(n):
    if n in fib.cache:
        return fib.cache[n]
    if n <= 2:
        fib.cache[n] = 1
    else:
        fib.cache[n] =  fib(n - 1) + fib(n - 2)
    return fib.cache[n]
fib.cache = {}

# Or using functools.cache
import functools
@functools.cache
def fib(n):
    if n <= 2:
        return 1
    return fib(n - 1) + fib(n - 2)


# If we wanted the memoization to be attached to each function call 
# from the top level (from the user, not including recursive calls)
# and not be shared between all calls
def fib(n):
    cache = {}
    def _fib(_n):
        if _n in cache:
            return cache[_n]
        if _n <= 2:
            return 1
        cache[_n] = _fib(_n - 1) + _fib(_n - 2)
        return cache[_n]
    result = _fib(n)
    cache.clear() # optional since `cache` is no longer available 
                  # after exiting the function
    return result


if __name__ == "__main__":
    print(fib(6))
    print(fib(7))
    print(fib(8))
    print(fib(50))
