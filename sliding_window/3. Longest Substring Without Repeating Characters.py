class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        ptr1 = 0
        ptr2 = 1
        max_len = 1
        while ptr2 < len(s):
            if s[ptr2] not in s[ptr1:ptr2]:
                ptr2 += 1
            else:
                if (ptr2 - ptr1) > max_len:
                    max_len = ptr2-ptr1
                ptr1_new = s.index(s[ptr2], ptr1)
                ptr1 = ptr1_new + 1
                ptr2 += 1
                
        if (ptr2 - ptr1) > max_len:
            max_len = ptr2-ptr1
        return max_len

s = Solution()
string = "cdd"
print(s.lengthOfLongestSubstring(string))

"""
pretty easy problem
just need to figure out the end case a little better
"""