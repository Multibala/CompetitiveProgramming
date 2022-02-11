from re import L
import sys
import math
from collections import defaultdict, deque
import random
 
# Multi 
 
out  = lambda x,end='\n' : sys.stdout.write(str(x)+end)
SI   = lambda: sys.stdin.readline().rstrip("\r\n")
MI   = lambda: map(int,SI().split())
II   = lambda: int(SI())
LI   = lambda: list(MI())
lcm  = lambda x,y:abs(x * y) // math.gcd(x,y)
FA   = lambda size,value: [value for _ in range(size)]
FCT  = lambda x:eval('*'.join([str(i) for i in range(1,x+1)])) if x>1 else 1
INF  = float("inf")


n = II()
empl = FA(n,0)
rs = LI()
meetings = []
cov = set()
mts = defaultdict(list)
for i in range(n):
    temp = LI()[1:]
    
    for j in range(len(temp)):
        mts[temp[j]].append(i)
        if rs[i] == 1:
            cov.add(temp[j])
    meetings.append(temp)
mts = sorted(mts.items())
for k,val in mts:
    if k in cov:
        for v in val:
            if rs[v] == 1:
                continue
            rs[v] = 1
            for a in meetings[v]:
                cov.add(a)

print(*rs)
