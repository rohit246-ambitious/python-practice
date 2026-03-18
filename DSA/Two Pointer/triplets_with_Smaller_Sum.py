'''
Given an array arr[] of distinct integers of size n and a value sum, the task is to find the count of triplets (i, j, k), having (i<j<k) with the sum of (arr[i] + arr[j] + arr[k]) smaller than the given value sum.

Examples :

Input: n = 4, sum = 2, arr[] = {-2, 0, 1, 3}
Output:  2
Explanation: Below are triplets with sum less than 2 (-2, 0, 1) and (-2, 0, 3). 


Input: n = 5, sum = 12, arr[] = {5, 1, 3, 4, 7}
Output: 4
Explanation: Below are triplets with sum less than 12 (1, 3, 4), (5, 1, 3), (1, 3, 7) and (5, 1, 4).

'''

class Solution:
    def countTriplets(self, n, sum, arr):
        #code here
        arr.sort()
        ans = 0
        for i in range(0, n-2):
            left = i+1
            right = n-1
            
            while left < right:
                sumVal = arr[i] + arr[left] + arr[right]
                if sumVal >= sum:
                    right-=1
                else:
                    ans = ans + (right-left)
                    left+=1
        return ans
        
obj = Solution()
arr = [-2, 0, 1, 3]
n = len(arr)
sum = 2
print(obj.countTriplets(n, sum, arr))
