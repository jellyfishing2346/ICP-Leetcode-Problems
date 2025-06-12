class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        char_count = {}
        for ch in s:
            char_count[ch] = char_count.get(ch, 0) + 1

        for j, ch in enumerate(s):
            if char_count[ch] == 1:
                return j
        return -1
        

