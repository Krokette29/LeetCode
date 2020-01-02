class Solution(object):
    """
    Given a string, find the length of the longest substring without repeating characters.

    Example 1:

    Input: "abcabcbb"
    Output: 3
    Explanation: The answer is "abc", with the length of 3.

    Example 2:

    Input: "bbbbb"
    Output: 1
    Explanation: The answer is "b", with the length of 1.

    Example 3:

    Input: "pwwkew"
    Output: 3
    Explanation: The answer is "wke", with the length of 3.
                 Note that the answer must be a substring, "pwke" is a subsequence and not a substring.
    """

    def checkRepeat(self, substring: str) -> bool:

        mySet = []

        for i in substring:
            if i in mySet:
                return False
            else:
                mySet.append(i)

        return True

    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        My solution. Using lots of time when executing large repeated strings. Almost like brute-force.
        TLE (Time Limit Exceed) on LeetCode.

        Time: O(n^3)
        Space: O(min(n, m))     # for checkRepeat, m is the size of charset
        """

        total_length = len(s)

        for windowSize in reversed(range(1, total_length + 1)):
            for i in range(total_length - windowSize + 1):
                res = self.checkRepeat(s[i:i + windowSize])

                if res:
                    return windowSize

        return 0

    def solution1(self, s: str) -> int:
        """
        Brute Force

        Check all the substring one by one to see if it has no duplicate character.
        Almost like my solution.
        TLE.

        Time: O(n^3)
        Space: O(min(n, m))
        """
        return 0

    def solution2(self, s: str) -> int:
        """
        Sliding Window
        """




def main():
    solution = Solution()

    input = "pwwkew"
    res = solution.lengthOfLongestSubstring(input)
    print(res)


if __name__ == '__main__':
    main()
