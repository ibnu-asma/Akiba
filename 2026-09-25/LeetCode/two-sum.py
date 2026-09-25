class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        idxs = defaultdict(int)
        for idx, num in enumerate(nums):
            comp = target - num
            if comp in idxs:
                return [idx, idxs[comp]]
            idxs[num] = idx
        return 
        