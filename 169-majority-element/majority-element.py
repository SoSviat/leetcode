class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        candidate = count = 0

        for num in nums:
            if count == 0:
                candidate = num

            if candidate != num:
                count -= 1
            elif candidate == num:
                count += 1 
            
        return candidate
        
        
        # firtst trye
        # max_val = len(nums)//2
        # my_dict = {}

        # for i in range(len(nums)):
        #     if nums[i] in my_dict:
        #         my_dict[nums[i]] += 1
        #     else:
        #         my_dict[nums[i]] = 1

        #     if my_dict[nums[i]] > max_val:
        #            return nums[i]

        #0(n)
        #0(n)