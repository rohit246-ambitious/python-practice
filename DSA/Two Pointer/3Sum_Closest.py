'''

Given an integer array nums of length n and an integer target, find three integers at distinct indices in nums such that the sum is closest to target.

Return the sum of the three integers.

You may assume that each input would have exactly one solution.

Example 1:

Input: nums = [-1,2,1,-4], target = 1
Output: 2
Explanation: The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
Example 2:

Input: nums = [0,0,0], target = 1
Output: 0
Explanation: The sum that is closest to the target is 0. (0 + 0 + 0 = 0).
 

'''

class Solution:
    def threeSumClosest(self, nums:list, target:int):
        nums.sort()
        n=len(nums)
        closestSum = float('inf')
        for i in range(0,n-2):
            left = i+1
            right = n-1
            while left < right:
                sumVal = nums[i] + nums[left] + nums[right] 
                diff = abs(sumVal-target)
                if sumVal == target:
                    return sumVal
                    
                if closestSum == float('inf') or diff < abs(closestSum - target):
                    closestSum = sumVal
                
                if sumVal < target:
                    left+=1
                else:
                    right-=1
            
        return closestSum
    
    def threeSumClosestOptimized(self, nums: list[int], target: int) -> int:
        nums.sort()
        n = len(nums)
        res = nums[0] + nums[1] + nums[2]  

        for i in range(n-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue

            left, right = i+1, n-1

            min_sum = nums[i] + nums[i+1] + nums[i+2]
            if min_sum >= target:
                if abs(min_sum - target) < abs(res - target):
                    res = min_sum
                break
            
            max_sum = nums[i] + nums[-1] + nums[-2]
            if max_sum <= target: 
                if abs(max_sum - target) < abs(res - target):
                    res = max_sum
                continue

            while left < right:
                s = nums[i] + nums[left] + nums[right]
                if abs(s-target) < abs(res-target):
                    res = s

                if s < target:
                    left += 1
                    while left < right and nums[left] == nums[left-1]:
                        left += 1
                elif s > target:
                    right -= 1
                    while left < right and nums[right] == nums[right+1]:
                        right -= 1
                else:
                    return target  

        return res
    
obj = Solution()
arr = [-1,2,1,-4]
target = 1
print(obj.threeSumClosest(arr, target))
print(obj.threeSumClosestOptimized(arr, target))