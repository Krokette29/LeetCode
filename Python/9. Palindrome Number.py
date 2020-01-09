class Solution:
	"""
	Determine whether an integer is a palindrome. An integer is a palindrome when it reads the same backward as forward.

	Example 1:

	Input: 121
	Output: true

	Example 2:

	Input: -121
	Output: false
	Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.

	Example 3:

	Input: 10
	Output: false
	Explanation: Reads 01 from right to left. Therefore it is not a palindrome.

	Follow up:

	Coud you solve it without converting the integer to a string?
	"""

	def isPalindrome1(self, x: int) -> bool:
		"""
		My solution, using string

		Time: O(n)
		Space: O(n)
		"""
		x_str = str(x)
		x_str_rev = ''

		for i in range(len(x_str)):
			x_str_rev = x_str[i] + x_str_rev

		return True if x_str_rev == x_str else False

	def isPalindrome(self, x: int) -> bool:
		"""
		My solution, not using string

		Time: O(n)/O(log10(x))
		Space: O(1)
		"""
		if x < 0:
			return False

		tmp = x
		x_rev = 0
		while tmp:
			pop = tmp % 10
			tmp = tmp // 10
			x_rev = x_rev * 10 + pop

		return True if x_rev == x else False

	def isPalindrome_solution1(self, x: int) -> bool:
		"""
		Solution 1, only search half of the length

		Time: 
		"""
		# the case x % 10 == 0 will cause a fail in the following algorithm
		# in these two cases (negative or 0 at the end), the number is definitely not palindrome
		if x < 0 or (x % 10 == 0 and x != 0):
			return False

		x_rev = 0
		# loop until we revert the half of the original number
		while x > x_rev:
			x_rev = x_rev * 10 + x % 10
			x = x // 10

		# two cases, length even or odd
		return x == x_rev or x == x_rev // 10


def main():
    solution = Solution()

    input = 123321

    res = solution.isPalindrome_solution1(input)
    print(res)


if __name__ == '__main__':
    main()
