import random


class Solution:
    """
    Given an array of integers, return indices of the two numbers such that they add up to a specific target.
    You may assume that each input would have exactly one solution, and you may not use the same element twice.

    Example:

    Given nums = [2, 7, 11, 15], target = 9,

    Because nums[0] + nums[1] = 2 + 7 = 9,
    return [0, 1].
    """

    def twoSum(self, nums: [int], target: int) -> [int]:
        """
        Using two-pass hash table. My first try in LeetCode.

        Time: O(n)
        Space: O(n)     # cause we need a hash table to store the numbers and indexes
        """
        dict = {}

        # first pass: use a dictionary/hash table to store the numbers and their indexes
        for i in range(len(nums)):
            dict[nums[i]] = i

        # second pass: O(1) loop up in the hash table
        for i in range(len(nums)):
            if target-nums[i] in dict.keys() and dict[target-nums[i]] != i:     # watch out for checking the index
                return [i, dict[target-nums[i]]]

        print("No two sum solution!")
        return None

    def twoSum_solution1(self, nums: [int], target: int) -> [int]:
        """
        Brute Force

        Time: O(n^2)
        Space: O(1)
        """
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]

        print("No two sum solutions!")
        return None

    def twoSum_solution2(self, nums: [int], target: int) -> [int]:
        """
        Two-pass Hash Table

        Time: O(n)
        Space: O(n)
        """
        dict = {}

        # first pass
        for i in range(len(nums)):
            dict[nums[i]] = i

        # second pass
        for i in range(len(nums)):
            complementary = target - nums[i]
            if complementary in dict.keys() and dict[complementary] != i:
                return [i, dict[complementary]]

        print("No two sum solutions!")
        return None

    def twoSum_solution3(self, nums: [int], target: int) -> [int]:
        """
        One-pass Hash Table

        Check the answer during the creation of hash table.

        Time: O(n)
        Space: O(n)
        """
        dict = {}

        for i in range(len(nums)):
            # check the solution first, and no need for checking the index
            complementary = target - nums[i]
            if complementary in dict.keys():
                return [dict[complementary], i]     # the existing value is before the checking value

            # otherwise add the number into the hash table
            dict[nums[i]] = i

        print("No two sum solution!")
        return None


def main():
    mySolution = Solution()

    nums = [random.randint(1, 20) for i in range(random.randint(5, 10))]
    target = random.randint(1, 20)

    print("nums: %s" % nums)
    print("target: %s" % target)
    print(mySolution.twoSum(nums, target))
    print(mySolution.twoSum_solution1(nums, target))
    print(mySolution.twoSum_solution2(nums, target))
    print(mySolution.twoSum_solution3(nums, target))


if __name__ == '__main__':
    main()
