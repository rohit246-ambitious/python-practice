'''
Given an array of positive integers nums and a positive integer target, return the minimal length of a subarray whose sum is greater than or equal to target. If there is no such subarray, return 0 instead.

 

Example 1:

Input: target = 7, nums = [2,3,1,2,4,3]
Output: 2
Explanation: The subarray [4,3] has the minimal length under the problem constraint.

Example 2:
Input: target = 4, nums = [1,4,4]
Output: 1

Example 3:
Input: target = 11, nums = [1,1,1,1,1,1,1,1]
Output: 0
 

Constraints:

1 <= target <= 109
1 <= nums.length <= 105
1 <= nums[i] <= 104
 
'''

class Solution:
    def maxSubarraySum(self, nums, target):
        n = len(nums)
        high = 0
        low = 0
        result = float('inf')
        window_sum = 0              # ✅ renamed

        while high < n:
            window_sum += nums[high]

            while window_sum >= target:
                length = high - low + 1
                result = min(result, length)
                window_sum -= nums[low]
                low += 1

            high += 1

        return result if result != float('inf') else 0  # ✅ edge case
        
        
obj = Solution()
arr = [2,3,1,2,4,3]
val =  7
print(obj.maxSubarraySum(arr,val))