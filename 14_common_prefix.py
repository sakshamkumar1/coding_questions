class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        minLen = 201
        minLenWord = None
        for ele in strs:
            if len(ele) < minLen:
                minLen = len(ele)
                minLenWord = ele
        prefix = []
        for i in range(len(minLenWord)):
            flag = 0
            for ele in strs:
                if minLenWord[i] != ele[i]:
                    flag = 1
                    return ''.join(prefix)
            prefix.append(minLenWord[i])
        return ''.join(prefix)

def main():
    arr = ["flower","flow","flight"]
    solution = Solution()
    print(solution.longestCommonPrefix(arr))

if __name__ == '__main__':
    main()