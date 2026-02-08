# Given two non-empty strings s1 and s2, consisting only of lowercase English letters, determine whether they are anagrams of each other or not.
# Two strings are considered anagrams if they contain the same characters with exactly the same frequencies, regardless of their order.

# Examples:

# Input: s1 = "geeks" s2 = "kseeg"
# Output: true 
# Explanation: Both the string have same characters with same frequency. So, they are anagrams.

class Solution:
    def areAnagrams(self, s1, s2):
        if len(s2) != len(s1):
            return False
        hash = {}
        for i in range(len(s2)):
            hash[s1[i]] = hash.get(s1[i],0)+1
            hash[s2[i]] = hash.get(s2[i],0)-1
        
        for val in hash.values():
            if val != 0:
                return False
        
        return True
        
                    
                