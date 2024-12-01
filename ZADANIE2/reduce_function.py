from fractions import Fraction
from functools import reduce


def product(fracs):
# twoj kod tutaj
    pass 


if __name__ == "__main__":
    fracs = []
    for _ in range(int(input())):
        fracs.append(Fraction(*map(int, input().split())))
    result = product(fracs)
    print(*result)
