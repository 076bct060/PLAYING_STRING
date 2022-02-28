def bubblesort(l):
   for iter_num in range(len(l)-1,0,-1):
      for idx in range(iter_num):
         if l[idx]>l[idx+1]:
            temp = l[idx]
            l[idx] = l[idx+1]
            l[idx+1] = temp
   return l


a = input("Enter first string: ")
b = input("Enter second string: ")
a = a.upper()
b = b.upper()
a = a.split(" ")
b = b.split(" ")
c = "".join(a)
d = "".join(b)
t = list(c)
u = list(d)
e = bubblesort(t)
f = bubblesort(u)
if e == f:
    print("The strings are anagrams.")
else:
    print("The strings are not anagrams.")
