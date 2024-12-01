from itertools import product



def maximize_expression(K, M, lists):
    # twoj kod tutaj
    pass 



if __name__ == "__main__":
    K, M = map(int, input().rstrip().split())

    lists = [list(map(int, input().rstrip().split()[1:])) for _ in range(K)]

    result = maximize_expression(K, M, lists)
    print(result)
