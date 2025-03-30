class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # reverse(n-k, n-1)
        # reverse(0, n-k-1)
        # reverse(0, n-1)

        n = len(nums)
        self.reverse(nums, n-k, n-1)
        self.reverse(nums, 0, n-k-1)
        self.reverse(nums, 0, n-1)
        print(nums)

    def reverse(self, arr, i, j):
        while i < j:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
            j -= 1

def main():
    solution = Solution()
    arr = [-1,-100,3,99]
    k = 2
    solution.rotate(arr, k)

if __name__ == '__main__':
    main()