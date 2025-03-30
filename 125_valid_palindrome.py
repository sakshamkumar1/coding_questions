class Solution:
    def isPalindrome(self, s: str) -> bool:
        arr = []
        for ele in s:
            if ord(ele) >= 65 and ord(ele) <= 90:
                arr.append(chr(ord(ele) + 32))
            elif ord(ele) >= 97 and ord(ele) <= 122:
                arr.append(ele)
            elif ord(ele) >= 48 and ord(ele) <= 57:
                arr.append(ele)
            else:
                continue
        if len(arr) == 0 or len(arr) == 1:
            return True
        else:
            leftPt = 0
            rightPt = len(arr) - 1
            while leftPt < rightPt:
                if arr[leftPt] != arr[rightPt]:
                    return False
                leftPt += 1
                rightPt -= 1
            return True

def main():
    solution = Solution()
    s = "A man, a plan, a canal: Panama"
    print(solution.isPalindrome(s))

if __name__ == '__main__':
    main()