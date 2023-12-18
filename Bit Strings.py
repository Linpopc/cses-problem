def countBit(n):
    mod = 10**9 + 7
    return 2**n % mod

def main():
    n = int(input())
    print(countBit(n))


if __name__ == "__main__":
    main()