

def weird(n):
    if n == 1:
        return
    if n%2 == 0:
        print(n//2)
        weird(n//2)
    else:
        print(n*3+1)
        weird(n*3+1)


def main():
    n = int(input())
    print(n)
    weird(n)


if __name__ == "__main__":
    main()