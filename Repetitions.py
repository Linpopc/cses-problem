
def long_sub(dna):
    max_sub = 0
    count = 1
    ch = dna[0]
    for i in range (1,len(dna)):
        if ch == dna[i]:
            count+=1
        else:
            ch = dna[i]
            max_sub = max(max_sub, count)
            count = 1
    return max(max_sub, count)

def main():
    s = str(input())
    res = long_sub(s)
    print(res)


if __name__ == "__main__":
    main()