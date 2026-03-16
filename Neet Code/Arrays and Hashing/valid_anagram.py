'''
Given two strings s and t, return true if the two strings are anagrams of each other, otherwise return false.

An anagram is a string that contains the exact same characters as another string, but the order of the characters can be different.

Example 1:
Input: s = "racecar", t = "carrace"
Output: true

Example 2:
Input: s = "jar", t = "jam"
Output: false

Constraints: s and t consist of lowercase English letters.
'''

class Solution:
    def isAnagram(self,s:str, t:str)-> bool:
        if len(s) != len(t):
            return False
        
        s_counts = {}
        t_counts = {}
        
        # s and t must be same length so can iterate over array once
        for i in range(len(s)):
            s_counts[s[i]] = s_counts.get(s[i],0) + 1
            t_counts[t[i]] = t_counts.get(t[i],0) + 1

        return s_counts == t_counts



print(Solution().isAnagram(s='racecar',t='carrace'))
print(Solution().isAnagram(s='racecar',t='carracd'))
print(Solution().isAnagram(s='racecardd',t='ddracecar'))
