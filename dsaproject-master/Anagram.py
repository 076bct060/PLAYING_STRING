def anagramCode(l1,l2):
    def mergeSort(arr):
        if len(arr) > 1:
            mid = len(arr) // 2
            L = arr[:mid]
            R = arr[mid:]
            mergeSort(L)
            mergeSort(R)
            i = j = k = 0
            while i < len(L) and j < len(R):
                if L[i] < R[j]:
                    arr[k] = L[i]
                    i += 1
                else:
                    arr[k] = R[j]
                    j += 1
                k += 1
            while i < len(L):
                arr[k] = L[i]
                i += 1
                k += 1

            while j < len(R):
                arr[k] = R[j]
                j += 1
                k += 1

    a = l1.upper()
    b = l2.upper()
    a = a.split(" ")
    b = b.split(" ")
    c = "".join(a)
    d = "".join(b)
    t = list(c)
    u = list(d)
    e = mergeSort(t)
    f = mergeSort(u)
    if e == f:
        return True
    return False