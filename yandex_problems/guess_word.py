
import sys
import math
from collections import defaultdict, deque,Counter
import random
from functools import lru_cache 


 
# Multi 
 
out  = lambda x,end='\n' : sys.stdout.write(str(x)+end)
SI   = lambda: sys.stdin.readline().rstrip("\r\n")
MI   = lambda: map(int,SI().split())
II   = lambda: int(SI())
LI   = lambda: list(MI())
lcm  = lambda x,y:abs(x * y) // math.gcd(x,y)
FCT  = lambda x:eval('*'.join([str(i) for i in range(1,x+1)])) if x>1 else 1
INF  = float("inf")


def binary_search(n,arr):
    start = 0
    end = len(arr) - 1
    while start<=end:
        mid = (start+end) // 2
        if arr[mid] > n:
            end = mid - 1
        elif arr[mid] <n:
            start = mid + 1
        else :
            return mid
    return -1


def isPrime(n):
    for i in range(2,int(n**(1/2))+1):
        if n%i == 0:
            return False
    return True

a = SI()
b = SI()
cnt = Counter(a)
ans = ['' for _ in range(len(a))]
for i in range(len(a)):
    if a[i] == b[i]:
        ans[i] = 'correct'
        cnt[a[i]] -=1
for i in range(len(a)):
    if ans[i] == 'correct':
        continue
    if cnt[b[i]] > 0:
        cnt[b[i]] -=1
        ans[i] = 'present'
    else:
        ans[i]='absent'
print(*ans,sep='\n')


    