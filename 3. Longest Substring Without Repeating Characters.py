class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """

        answer_list = []
        max_len = 0

        for i in s:
            if i not in answer_list:
                answer_list.append(i)
                if len(answer_list) > max_len:
                    max_len = len(answer_list)
            else:
                answer_list = [i]

        return max_len


ss = Solution()

s = "dvdf"

print(ss.lengthOfLongestSubstring(s))
# Output: 3