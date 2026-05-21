#weeks13-3.py
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:

        # nums.sort(reverse=True)
        # return nums[k-1]

        #heapify(nums)
        #while nums:
        #    print( heappop(nums) )

        heapify(nums)
        for i in range(len(nums)-k):
            heappop(nums)
        return heappop(nums)
