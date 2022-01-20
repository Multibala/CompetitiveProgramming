import sys
import math

SI = lambda: sys.stdin.readline().rstrip("\r\n")
MI = lambda: map(int,SI().split())
II = lambda: int(SI())
LI = lambda: list(MI())
lcm = lambda x,y:abs(x*y)//math.gcd(x,y)
FA = lambda size,value: [value for _ in range(size)] # get filled array







