class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        arrlen = len(numbers)
        i = 0
        j = arrlen-1
        while i < j:
            sum = numbers[i] + numbers[j]
            if sum == target:
                return [i+1, j+1]
            elif sum > target:
                j-=1
            else:
                i+=1
        return []
        
        
obj = Solution()
numberList = [2,7,11,15]
target = 9
print(obj.twoSum(numberList,target))
        