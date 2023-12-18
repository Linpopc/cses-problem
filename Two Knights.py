

def count (k):
    kk = k**2
    return kk*(kk-1)//2 - 4 * (k-1) * (k-2)


def main():
    n = int(input())
    for k in range (1,n+1):
        print(count(k))


if __name__ == "__main__":
    main()