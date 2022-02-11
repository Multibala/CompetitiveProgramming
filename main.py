from re import L
import sys
import math
from collections import deque
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



print("YERBOL")

    
