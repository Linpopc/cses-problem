def equalSum(n):
    factSum = (n + n**2) // 2
    if factSum%2:
        return
    target = factSum//2
    left, right = [],[]
    for num in range (n,0,-1):
        if num <=target:
            left.append(num)
            target -= num
        else:
            right.append(num)
    return left, right

def main():
    n = int(input())
    sets = equalSum(n)
    if sets:
        print("YES")
        left, right = sets
        print(len(left))
        print(*left)

        print(len(right))
        print(*right)
    else:
        print("NO")


if __name__ == "__main__":
    main()