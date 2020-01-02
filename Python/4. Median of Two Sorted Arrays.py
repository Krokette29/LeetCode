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


def main():
    solution = Solution()

    nums1 = [1, 2]
    nums2 = [3, 4]

    res = solution.findMedianSortedArrays2(nums1, nums2)
    print(res)


if __name__ == '__main__':
    main()
