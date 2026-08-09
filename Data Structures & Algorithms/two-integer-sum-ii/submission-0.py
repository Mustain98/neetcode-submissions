class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        nums=set()
        pos={}
        for i in range(len(numbers)):
            nums.add(numbers[i])
            pos[numbers[i]]=i

        for i in range(len(numbers)):
            req=target-numbers[i]

            if req in nums and i != pos[req]:
                return [i+1,pos[req]+1]

        