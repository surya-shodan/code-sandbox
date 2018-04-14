import time


def get_fibo(position):

    if position == 1:
        return 1
    elif position == 0:
        return 0
    else:
        sum = get_fibo(position - 1) + get_fibo(position - 2)
        return sum
def main():
    print(get_fibo(10))

if __name__ == '__main__':
    main()
