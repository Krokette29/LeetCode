class Solution:
	"""
	Given a 32-bit signed integer, reverse digits of an integer.

	Example 1:

	Input: 123
	Output: 321

	Example 2:

	Input: -123
	Output: -321

	Example 3:

	Input: 120
	Output: 21

	Note:
	Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−231,  231 − 1]. 
	For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.
	"""

	def reverse(self, x: int) -> int:
		# """
		# My solution. Using string to make an invertion.

		# Time: O(n)/O(log(x)) (x contains about log(x) numbers)
		# Space: O(n)/O(log(x)) (for storing the string variables)
		# """
		x_str = str(x)
		res_str = ''

		# Case 1: negative number
		if x_str[0] == '-':
			x_str = x_str[1:]
			for i in range(len(x_str)):
				res_str = x_str[i] + res_str
				res = -int(res_str)

		# Case 2: positive number
		else:
			for i in range(len(x_str)):
				res_str = x_str[i] + res_str
				res = int(res_str)

		return 0 if res < -2**31 or res > 2**31-1 else res

	def reverse_solution1(self, x: int) -> int:
		"""
		Solution 1: not using string, directly invert the number

		Time: O(log(x))
		Space: O(1)
		"""
		pop = 0		# store the last digit number
		res = 0

		while x:
			pop = x - int(x/10) * 10		# x // 10 cannot be used in negative numbers
			x = int(x/10)
			res = res * 10 + pop

		return 0 if res < -2**31 or res > 2**31-1 else res



def main():
    solution = Solution()

    input = 1234

    res = solution.reverse_solution1(input)
    print(res)


if __name__ == '__main__':
    main()
