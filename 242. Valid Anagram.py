from typing import Counter
from collections import defaultdict
class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        # return Counter(s) == Counter(t)
        # return list(s).sort() == list(t).sort()
        # return True if len(s) == len(t) and set(s) == set(t) else False
        if len(s) != len(t):
            return False
        else:
            hashmap_a = defaultdict(int)
            hashmap_b = defaultdict(int)
            for i in range(len(s)):
                hashmap_a[s[i]] += 1
                hashmap_b[t[i]] += 1
        
        return hashmap_a == hashmap_b
        
        

x = Solution()
s = 'anagram'
t = 'nagaram'

s2 = 'aacc'
s3 = 'acaa'
print(x.isAnagram(s2, s3))
print(x.isAnagram(t, s))