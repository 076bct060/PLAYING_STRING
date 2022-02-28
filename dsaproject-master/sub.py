def generatesub(a):
    b = []
    n = len(a)
    e = pow(2,n)
    i = 1
    while i < e:
        j = 0
        sub = ""
        while j < n:
            if i & (1 << j):
                sub = sub + a[j]
            j = j+1
        b.append(sub)
        i = i+1
    return b


a = input("Enter a string: ")
print("The substrings of the given string are :")
d = generatesub(a)
print(d)

# searching for a substring
ans = input("Do you want to search for a substring,enter yes or no: ")
ans = ans.upper()
if ans == "YES":
    c = input("Enter the substring to be searched: ")
    if c in d:
        print("The substring is present.")
    else:
        print("The substring is not present.")
else:
    exit(0)

