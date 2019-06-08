import time
start = time.time()
palindrome = []
def maxi(x):
    for x in range(900,x):
        for y in range(900,x):
            if str(x*y)==str(x*y)[::-1]:
                palindrome.append(x*y)
maxi(1000)
print(max(palindrome))
end = time.time()
print(end - start)
