class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        i = 0
        k = len(nums)
        while i < len(nums)-1:
            if nums[i] == nums[i+1]:
                del nums[i+1]
                k -= 1
            else:
                i += 1

        print(nums)
        return k

def main():
    solution = Solution()
    arr = [1, 1, 2]
    print(solution.removeDuplicates(arr))

if __name__ == '__main__':
    main()