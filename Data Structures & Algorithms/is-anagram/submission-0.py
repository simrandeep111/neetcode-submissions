class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hashmap={}
        for i in range(len(s)):
            hashmap[s[i]] = hashmap.get(s[i], 0) + 1

        for j in range(len(t)):
            hashmap[t[j]] = hashmap.get(t[j], 0) - 1

        for value in hashmap.values():
            if value != 0:
                return False

        return True
                