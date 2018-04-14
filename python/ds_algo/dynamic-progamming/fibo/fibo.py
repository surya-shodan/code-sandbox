import time


BASIC_CTR = 0
def fibo_basic(n):
    # global BASIC_CTR
    # BASIC_CTR += 1
    if n == 1: return 1
    elif n <= 0: return 0
    else:
        return fibo_basic(n - 1) + fibo_basic(n - 2)

UNKNOWN = -1
CACHED_CTR = 0
def fibo_cached(n, hash_t):
    # global CACHED_CTR
    # CACHED_CTR += 1
    # print(hash_t)
    # time.sleep(0.2)
    # CACHED_CTR += 1
    if hash_t[n] == UNKNOWN:
        hash_t[n] = fibo_cached(n-1, hash_t) + fibo_cached(n-2, hash_t)
    return hash_t[n]

def fibo_dp(n):
    list_f = [0, 1]
    if n <= 0: return 0
    for i in range(2, n+1):
        list_f.append(list_f[-1] + list_f[-2])
    return list_f[-1]


def main():
    n = 10

    for i in xrange(n+1):
        print('{number} : {fibo_i}'.format(number = i, fibo_i = fibo_basic(i)))
    print("BASIC CALLS :", BASIC_CTR)

    hash_t = dict()
    hash_t[0] = 0
    hash_t[1] = 1
    for i in range(2, n+1):
       hash_t[i] = UNKNOWN
    print(fibo_cached(n, hash_t))
    print("CACHED CALLS :", CACHED_CTR)

    """
    DP RUNNER
    """
    print('\nDP Runner\n')
    n = 10
    for i in xrange(n+1):
        print('{number} : {fibo_i}'.format(number = i, fibo_i = fibo_dp(i)))


if __name__ == '__main__':
    main()
