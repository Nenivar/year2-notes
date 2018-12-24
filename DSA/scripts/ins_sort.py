def ins_sort(l: []) -> []:
    for j in range(1, len(l)):
        k = l[j]
        i = j - 1
        while i > 0 and l[i] > k:
            l[i + 1] = l[i]
            i = i - 1
        l[i + 1] = k
        print(l)
    return l

print(ins_sort([5,2,4,6,1,3]))