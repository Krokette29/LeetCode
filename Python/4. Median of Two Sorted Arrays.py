class Solution:
    """
    There are two sorted arrays nums1 and nums2 of size m and n respectively.

    Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).

    You may assume nums1 and nums2 cannot be both empty.

    Example 1:

    nums1 = [1, 3]
    nums2 = [2]

    The median is 2.0

    Example 2:

    nums1 = [1, 2]
    nums2 = [3, 4]

    The median is (2 + 3)/2 = 2.5
    """

    def findMedianSortedArrays(self, nums1: [int], nums2: [int]) -> float:
        """
        Using sorted() in Python.
        """
        nums = nums1 + nums2
        nums = sorted(nums)

        if len(nums) % 2 == 1:
            return nums[(len(nums) + 1) // 2 - 1]
        else:
            return (nums[len(nums) // 2] + nums[len(nums) // 2 - 1]) / 2

    def findMedianSortedArrays2(self, nums1: [int], nums2: [int]) -> float:
        """
        Create a sorted array by adding the minimum of each list.

        Time: O(m+n)
        Space: O(m+n)
        """
        # create a sorted array
        sorted_array = []
        while nums1 or nums2:
            if not nums1:
                sorted_array.append(nums2[0])
                del nums2[0]
            elif not nums2:
                sorted_array.append(nums1[0])
                del nums1[0]
            else:
                if nums1[0] < nums2[0]:
                    sorted_array.append(nums1[0])
                    del nums1[0]
                else:
                    sorted_array.append(nums2[0])
                    del nums2[0]

        # return the median
        if len(sorted_array) % 2 == 1:
            return sorted_array[len(sorted_array) // 2]
        else:
            return (sorted_array[len(sorted_array) // 2 - 1] + sorted_array[len(sorted_array) // 2]) / 2

    def solution1(self, nums1: [int], nums2: [int]) -> float:
        """
        Binary Search

        Time: O(log(min(m+n)))
        Space: O(1)
        """
        m, n = len(nums1), len(nums2)
        # otherwise taking half of the array will exceed the length of the other array
        if m > n:
            m, n, nums1, nums2 = n, m, nums2, nums1

        i_min, i_max = 0, len(nums1)
        half_length = (m + n) // 2

        # loop until two pointers be equal (in fact i_min will not greater than i_max)
        while i_min <= i_max:
            # update i_middle and j_middle
            i_middle = (i_min + i_max) // 2
            j_middle = half_length - i_middle

            # if i_middle = 0 means all numbers in nums1 belong to the right part, no need for updating middle pointers
            if i_middle > 0 and nums1[i_middle - 1] > nums2[j_middle]:
                i_max = i_middle - 1

            # if i_middle = m means all numbers in nums1 belong to the left part, no need for updating middle pointers
            elif i_middle < m and nums1[i_middle] < nums2[j_middle - 1]:
                i_min = i_middle + 1

            else:
                # first calculate right_min
                # because the length of the right part could be 1 more thant left part, then just return right_min
                # be careful about the boundary cases (i_middle or j_middle on the rightmost position)
                if i_middle == m:
                    right_min = nums2[j_middle]
                elif j_middle == n:
                    right_min = nums1[i_middle]
                else:
                    right_min = min(nums1[i_middle], nums2[j_middle])
                if (m + n) % 2 == 1:
                    return right_min

                # if (m + n) % 2 == 0, then we need also left_max
                # also be careful about the two boundary cases
                if i_middle == 0:
                    left_max = nums2[j_middle - 1]
                elif j_middle == 0:
                    left_max = nums1[i_middle - 1]
                else:
                    left_max = max(nums1[i_middle - 1], nums2[j_middle - 1])
                return (left_max + right_min) / 2


def main():
    solution = Solution()

    nums1 = [1, 2, 3]
    nums2 = [4, 5, 6]

    res = solution.solution1(nums1, nums2)
    print(res)


if __name__ == '__main__':
    main()
