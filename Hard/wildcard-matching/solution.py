class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        s_idx, p_idx = 0, 0
        star_idx, match_idx = -1, 0
        
        while s_idx < len(s):
            # Characters match or '?' matches any single character
            if p_idx < len(p) and (p[p_idx] == s[s_idx] or p[p_idx] == '?'):
                s_idx += 1
                p_idx += 1
            # Found a '*' in pattern
            elif p_idx < len(p) and p[p_idx] == '*':
                star_idx = p_idx
                match_idx = s_idx
                p_idx += 1
            # Backtrack to the last '*' if mismatch occurs
            elif star_idx != -1:
                p_idx = star_idx + 1
                match_idx += 1
                s_idx = match_idx
            # Mismatch and no '*' to backtrack
            else:
                return False
        
        # Check remaining characters in pattern, which must all be '*'
        while p_idx < len(p) and p[p_idx] == '*':
            p_idx += 1
            
        return p_idx == len(p)