
def missing(n,nums):
    fact_sum_nums = (n+n**2)//2
    sum_nums = sum(nums)
    return fact_sum_nums - sum_nums

def main():
    n = int(input())
    nums = list(map(int,input().split()))
    res = missing(n,nums)
    print(res)


if __name__ == "__main__":
    main()