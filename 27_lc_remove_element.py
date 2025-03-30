class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        i = 0
        count = 0
        while i < len(nums):
            if nums[i] == val:
                del nums[i]
                count += 1
                i -= 1
            i += 1
        print(nums, count)

def main():
    solution = Solution()
    solution.removeElement([0,1,2,2,3,0,4,2], 2)

if __name__ == '__main__':
    main()