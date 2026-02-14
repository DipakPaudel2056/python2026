def lengthOfLongestSubstring( s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) == 0:
            return 0
        if len(s) == 1:
            return 1
        left =  0
        maxlength = 0
        res = set()
        n = len(s)
        for right in range(n):
            if s[right] not in res:
                res.add(s[right])
                maxlength = max(maxlength,right-left+1)
            else:
                while s[right] in res:
                    res.remove(s[left])
                    left += 1
                res.add(s[right])
        return maxlength
        
        
#leetcode 3 3. Longest Substring Without Repeating Characters
print(lengthOfLongestSubstring("abcabcbb"))