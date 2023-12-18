def numSpiral(x,y):
    if x > y:
        if x%2:
            return x**2 - (y-1)
        else:
            return (x-1)**2 + y
    else:
        if y%2:
            return (y-1)**2 + x
        else:
            return y**2 - (x-1)

def main():
    n = int(input())
    for i in range (n):
        y, x = map(int,input().split())
        print(numSpiral(x,y))

if __name__ == "__main__":
    main()