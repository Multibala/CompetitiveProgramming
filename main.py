
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

n = II()
vac = defaultdict(int)
names = []
for _ in range(n):
    a = SI().split(',')
    vac[a[0]] = int(a[1])
    

mm = defaultdict(list)
k = II()
for i in range(k):
    a = SI().split(',')
    mm[a[1]].append((int(a[2]),-int(a[3]),i,a[0]))


for v in vac:
    mm[v].sort(reverse=True)
    k = 0
    while vac[v]:
        names.append(mm[v][k][3])
        vac[v] -= 1
        k += 1

names.sort()

print(*names,sep='\n')


                    






    