# Problem Statement - 
# there's a 2D grid of dimensions m x n , you are at the top left corner, 
# find in how many ways you can reach the bottom right when you can only 
# move down or right.

def grid_traveler(m, n):
    cache = {}
    def _grid_traveler(_m, _n):
        if (_m, _n) in cache:
            return cache[(_m, _n)]
        if _m <= 0 or _n <= 0:
            return 0
        if _m == 1 or _n == 1:
            return 1
        cache[(_m, _n)] = _grid_traveler(_m - 1, _n) + _grid_traveler(_m, _n - 1)
        return cache[(_m, _n)]
    result = _grid_traveler(m, n)
    cache.clear()
    return result

if __name__ == "__main__":
    print(grid_traveler(1, 3))
    print(grid_traveler(2, 1))
    print(grid_traveler(2, 3))
    print(grid_traveler(5, 4))
    print(grid_traveler(18, 18))
    print(grid_traveler(53, 98))
    