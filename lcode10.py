'''58. Length of Last Word'''

'''Given a string s consisting of words and spaces, return the length of the last word in the string.

A word is a maximal substring consisting of non-space characters only.

 

Example 1:

Input: s = "Hello World"
Output: 5
Explanation: The last word is "World" with length 5.
Example 2:

Input: s = "   fly me   to   the moon  "
Output: 4
Explanation: The last word is "moon" with length 4.
Example 3:

Input: s = "luffy is still joyboy"
Output: 6
Explanation: The last word is "joyboy" with length 6.'''




class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        c=-1
        s=s.rstrip()
        if(len(s)<=2):
            return 1
        else:
            for i in range(len(s)-1,-1,-1):
                c+=1
                if(s[-1] == " "):
                    k=3
                    for j in range(len(s)-2,0,-1):
                        k+=1
                        if(s[i] == " " and i != len(s)-1 or i == 0):
                            return k
                elif(s[i] == " " and i != len(s)-1):
                    return c
            return c+1