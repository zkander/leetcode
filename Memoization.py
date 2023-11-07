
from functools import cache


# uncomment @cache to work
# @cache
def traveler(m, n):
    if (n == 1 and m == 1):
        return 1
    if (n == 0 or m == 0):
        return 0
    return traveler(m-1, n) + traveler(m, n-1)


print(traveler(18, 18))
