class Solution:
    """
    Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

    Example 1:

    Input: "babad"
    Output: "bab"
    Note: "aba" is also a valid answer.

    Example 2:

    Input: "cbbd"
    Output: "bb"
    """

    def __checkPalindrome(self, s: str, i_left: int, i_right: int) -> (int, str):
        while i_left > 0 and i_right < len(s) - 1:
            if s[i_left - 1] == s[i_right + 1]:
                i_left -= 1
                i_right += 1
            else:
                break

        length = i_right - i_left + 1
        string = s[i_left:i_right + 1]

        return length, string

    def longestPalindrome(self, s: str) -> str:
        """
        My solution. Using "Expand Around Center".

        Time: O(n)
        Space: O(1)
        """
        max_str = '' if len(s) == 0 else s[0]
        max_length = len(max_str)

        for i in range(len(s) - 1):
            # center with one char
            if s[i] == s[i + 1]:
                i_left, i_right = i, i + 1
                length, string = self.__checkPalindrome(s, i_left, i_right)

                if length > max_length:
                    max_length, max_str = length, string

            # center with two chars
            i_left, i_right = i, i
            length, string = self.__checkPalindrome(s, i_left, i_right)

            if length > max_length:
                max_length, max_str = length, string

        return max_str


def main():
    solution = Solution()

    input = "babad"

    res = solution.longestPalindrome(input)
    print(res)


if __name__ == '__main__':
    main()
