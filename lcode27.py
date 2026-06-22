'''392. Is Subsequence'''

'''Given two strings s and t, return true if s is a subsequence of t, or false otherwise.

A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters.

 

Example 1:

Input: s = "abc", t = "aabbcc"
Output: true
Example 2:

Input: s = "axc", t = "aabbcc"
Output: falses'''



class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i = 0

        for ch in t:
            if i < len(s) and ch == s[i]:
                i += 1

        return i == len(s)