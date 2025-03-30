from typing import List

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i = 0
        j = 0
        idx_fill = 0
        temp_nums_1 = nums1.copy()
        while idx_fill < m+n:
            if i < m and j < n:
                if temp_nums_1[i] <= nums2[j]:
                    nums1[idx_fill] = temp_nums_1[i]
                    idx_fill += 1
                    i += 1
                else:
                    nums1[idx_fill] = nums2[j]
                    idx_fill += 1
                    j += 1
            elif i < m:
                nums1[idx_fill] = temp_nums_1[i]
                idx_fill += 1
                i += 1
            elif j < n:
                nums1[idx_fill] = nums2[j]
                idx_fill += 1
                j += 1
        print(nums1)

def main():
    solution = Solution()
    solution.merge(nums1=[1,2,3,0,0,0], m=3, nums2=[2,5,6], n=3)

if __name__ == '__main__':
    main()