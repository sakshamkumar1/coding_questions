class Solution():
    def canJump(self, nums: list[int]) -> bool:
        jumps = nums[0]
        n = len(nums)
        i = 0
        while i < n-1:
            if jumps == 0:
                return False
            if nums[i+1] < nums[i]:
                i += 1
                jumps -= 1
            elif nums[i + 1] == nums[i]:
                if nums[i+1] == nums[i] == 0:
                    jumps -= 1
                    i += 1
                else:
                    i += 1
            else:
                if jumps - 1 < nums[i+1]:
                    jumps = nums[i + 1]
                else:
                    jumps -= 1
                i += 1
        if i == n-1:
            return True

def main():
    solution = Solution()
    arr = [8,2,4,4,4,9,5,2,5,8,8,0,8,6,9,1,1,6,3,5,1,2,6,6,0,4,8,6,0,3,2,8,7,6,5,1,7,0,3,4,8,3,5,9,0,4,0,1,0,5,9,2,0,7,0,2,1,0,8,2,5,1,2,3,9,7,4,7,0,0,1,8,5,6,7,5,1,9,9,3,5,0,7,5]
    print(solution.canJump(arr))

if __name__ == '__main__':
    main()


