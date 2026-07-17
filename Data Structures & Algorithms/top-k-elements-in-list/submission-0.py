from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}

        for num in nums:
            freq[num] = freq.get(num, 0) + 1

        sorted_nums = sorted(freq.items(), key=lambda x: x[1], reverse=True)

        res = []

        for i in range(k):
            res.append(sorted_nums[i][0])

        return res