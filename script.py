def solve(n, nums):
    # Write your code here
    pairs = 0
    for i in range(n - 1):
        for j in range(i + 1, n):
            num_1 = list(str(nums[i]))
            for k in range(len(num_1)):
                num_1[i] = int(num_1[i])
            sum_1 = sum(num_1)
            num_2 = list(str(nums[i]))
            for k in range(len(num_2)):
                num_2[k] = int(num_2[k])
            sum_2 = sum(num_2)
            if sum_1 == sum_2:
                pairs += 1

    return pairs


n = int(input())
nums = list(map(int, input().split()))

out_ = solve(n, nums)
print(out_)
