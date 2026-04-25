class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:

        #list_ = deque()
        list_ = set()
    
        for i in range(len(nums)):

            if nums[i] in list_:
                return True
            
            list_.add(nums[i])

            if(len(list_) > k):
                list_.remove(nums[i - k])

        return False
            
