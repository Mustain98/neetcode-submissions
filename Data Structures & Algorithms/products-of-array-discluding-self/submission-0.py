class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        p=1;
        b=1;
        rev_list=[]
        for_list=[]
        ans=[]
        for i in range(len(nums)):
            p*=nums[i]
            b*=nums[len(nums)-i-1]
            for_list.append(p)
            rev_list.append(b)
        for i in range(len(nums)):
            pro=1;
            if i > 0:
                pro*=for_list[i-1]
            if i< len(nums)-1:
                pro*=rev_list[len(nums)-i-2]
            ans.append(pro)
        return ans