class Solution:
    def jump(self, nums: list[int]) -> int:
        n = len(nums)
        i = 0
        jumps = 0
        while i < n-1:
            currSteps = nums[i]
            maxJ = currSteps
            tempJumps = nums[i+currSteps]
            idx = i + currSteps
            for j in range(i+1, i+currSteps+1):
                temp = nums[j] + (j - i)
                if temp >= maxJ:
                    idx = j
                    tempJumps = nums[j]
                    maxJ = temp
            currSteps = nums[idx]
            jumps += 1
            i = idx
        return jumps

def main():
    solution = Solution()
    arr = [2,3,1,1,4]
    print(solution.jump(arr))

if __name__ == '__main__':
    main()