class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        csum = nums[0]
        msum = nums[0]
        for i in range(1,len(nums)):
            csum = max(nums[i],nums[i]+csum)
            msum = max(msum,csum)
        return msum