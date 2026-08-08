class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums: return 0
        nums.sort()
        temp=1
        cnt=1
        for i in range(1,len(nums)):
            if nums[i]==nums[i-1]+1 or nums[i]==nums[i-1]:
                temp+=(nums[i]-nums[i-1]);
            else:
                temp=1
            cnt=max(cnt,temp)
        return cnt
