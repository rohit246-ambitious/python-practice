'''

You are given a string s consisting only lowercase alphabets and an integer k. Your task is to find the length of the longest substring that contains exactly k distinct characters.

Note : If no such substring exists, return -1. 

Examples:

Input: s = "aabacbebebe", k = 3
Output: 7
Explanation: The longest substring with exactly 3 distinct characters is "cbebebe", which includes 'c', 'b', and 'e'.

Input: s = "aaaa", k = 2
Output: -1
Explanation: There's no substring with 2 distinct characters.

Input: s = "aabaaab", k = 2
Output: 7
Explanation: The entire string "aabaaab" has exactly 2 unique characters 'a' and 'b', making it the longest valid substring.

Constraints:
1 ≤ s.size() ≤ 105
1 ≤ k ≤ 26

'''

class Solution:
    def longestKSubstr(self, s, k):
        n = len(s)
        left = 0
        freq = {}
        res = -1
        for right in range(n):
            freq[s[right]] = freq.get(s[right], 0) + 1
            
            while len(freq) > k:
                freq[s[left]] -= 1
                if freq[s[left]] == 0:
                    del freq[s[left]]
                left += 1
                
            if len(freq) == k:
                res = max(res, right-left+1)
        return res
        
obj = Solution()
s="aaaa"
k = 3
print(obj.longestKSubstr(s,k))