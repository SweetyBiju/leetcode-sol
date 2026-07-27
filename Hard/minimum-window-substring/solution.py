from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t:
            return ""
        
        t_count = Counter(t)
        required = len(t_count)
        
        left = 0
        formed = 0
        window_count = Counter()
        
        # ans format: (window_length, left, right)
        ans = (float('inf'), None, None)
        
        for right in range(len(s)):
            char = s[right]
            window_count[char] += 1
            
            if char in t_count and window_count[char] == t_count[char]:
                formed += 1
            
            while left <= right and formed == required:
                char = s[left]
                
                if right - left + 1 < ans[0]:
                    ans = (right - left + 1, left, right)
                
                window_count[char] -= 1
                if char in t_count and window_count[char] < t_count[char]:
                    formed -= 1
                
                left += 1
        
        return "" if ans[0] == float('inf') else s[ans[1]:ans[2] + 1]