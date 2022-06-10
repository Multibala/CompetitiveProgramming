
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

def mfs(dir,r,c,mp):
    if r>=0 and c>=0 and r<len(mp) and c<len(mp[0]):

        if mp[r][c] == '.':
            mp[r][c] = dir
            return True
    
    return False

def move(r,c,mp):

    moves = [[r,c]]
    temp = []
    while len(moves):
        for m in moves:
            r,c = m[0],m[1]
            if mfs('L',r,c - 1,mp):
                temp.append([r,c-1])
            if mfs('R',r,c + 1,mp):
                temp.append([r,c+1])
            if mfs('D',r + 1,c,mp):
                temp.append([r+1,c])
            if mfs('U',r - 1,c,mp):
                temp.append([r-1,c])
        moves = temp.copy()
        temp.clear()






n,m = MI()
mp = []
x0,y0 = -1,-1
for i in range(n):
    a = list(SI())
    if 'S' in a:
        x0 = a.index('S')
        y0 = i
    mp.append(a)

boll = True
move(y0,x0,mp)

    
for m in mp:
    print(*m,sep='')

                
                    






    