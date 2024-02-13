def pali(s):
    return s == s[::-1]


s = str(input("enter:"))
ans = pali(s)
if ans:
    print("yes")
else:
    print("no")
pali(s)
