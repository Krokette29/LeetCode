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
        Space: O(min(m, n))     # for checkRepeat, m is the size of charset
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
        Space: O(min(m, n))
        """
        return 0

    def solution2(self, s: str) -> int:
        """
        Sliding Window

        Use a queue. Loop over all chars in the string.
        If the char is not in the queue, append it. Otherwise pop the queue.

        Time: O(n)
        Space: O(min(m, n))     # for queue
        """
        queue = []
        max_length = 0
        index = 0

        # loop over all chars in the string
        while index < len(s):
            char = s[index]

            # if char not in the queue, append it
            if char not in queue:
                queue.append(char)
                index += 1

            # otherwise check the result, add pop the queue
            else:
                if len(queue) > max_length:
                    max_length = len(queue)
                del queue[0]

        return max_length if max_length > len(queue) else len(queue)

    def solution3(self, s: str) -> int:
        """
        Sliding Window Optimized using Hash Table/Dictionary

        Like the sliding window. If found repeated char, start index jumps to the next index of the last repeated char.

        Time: O(n)          # half as solution 2
        Space: O(min(m, n))
        """
        dict = {}       # key: char, value: last index
        max_length = 0
        start_index = 0

        for end_index in range(len(s)):
            char = s[end_index]

            # if found repeated char, update the start index
            if char in dict.keys():
                start_index = max(dict[char] + 1, start_index)

            length = end_index - start_index + 1    # current length
            max_length = max(length, max_length)    # maximum length
            dict[char] = end_index                  # update dictionary

        return max_length


def main():
    solution = Solution()

    input = "dvdf"
    res = solution.solution3(input)
    print(res)


if __name__ == '__main__':
    main()
