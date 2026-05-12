class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
    #anagrams are letter contains exact same letters, sort letters and compare?
    #sort letters in string and join, compare if two strings are equal
        sorted_s = "".join(sorted(s))
        sorted_t = "".join(sorted(t))
        return sorted_t == sorted_s