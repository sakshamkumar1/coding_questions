def solve(n, nums):
    # Write your code here
    pairs = 0
    sum_arr = [0] * n
    for i in range(n):
        number = nums[i]
        sum_num = 0
        while number > 0:
            sum_num += number % 10
            number = number // 10
        sum_arr[i] = sum_num

    freq_arr = [0] * (max(nums)+1)
    for ele in sum_arr:
        freq_arr[ele] += 1

    for i in range(len(freq_arr)):
        if freq_arr[i] > 1:
            pairs += int((freq_arr[i] * (freq_arr[i] - 1)) / 2)

    return pairs


n = int(input())
nums = list(map(int, input().split()))

out_ = solve(n, nums)
print(out_)
