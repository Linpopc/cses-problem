
def count_of_moves(nums):
    count = 0
    for i in range(1,len(nums)):
        if nums[i] < nums[i-1]:
            dif = nums[i-1] - nums[i]
            nums[i] = nums[i-1]
            count += dif
    return count

def main():
    n = int(input())
    nums = list(map(int,input().split()))
    res = count_of_moves(nums)
    print(res)


if __name__ == "__main__":
    main()