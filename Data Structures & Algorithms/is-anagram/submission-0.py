from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Returns True if character counts match perfectly
        return Counter(s) == Counter(t)
