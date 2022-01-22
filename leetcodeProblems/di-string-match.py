class Solution:
    def diStringMatch(self, s: str) -> List[int]:
        ans = [i for i in range(len(s)+1)]
        l,r = 0,0
        for i in range(len(s)):
            if s[i] =='D':
                if r == 0:
                    l = i
                    r = l
                r += 1
            if s[i] == 'I' and r>0 or (i+1 == len(s) and s[i] =='D'):
                ans[l:r + 1] = ans[r:l:-1] + [ans[l]]
                r = 0
            
        
        return ans
        
        