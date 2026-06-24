class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        
        nums.sort()
        list_res =[]

        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            start = i + 1
            end = len(nums) - 1

            while start < end:
                res = nums[i] + nums[start] + nums[end]

                if res == 0:
                    list_res += [[nums[i], nums[start], nums[end]]]
                    start += 1
                    end -= 1
                    while start < end and nums[start] == nums[start-1]:
                        start += 1
                    while start < end and nums[end] == nums[end+1]:
                        end -= 1
                elif res < 0:
                    start += 1
                else:
                    end -= 1

        return list_res

        #O(n2)
        #O(1)


        # nums.sort()
        # list_res =[]

        # for i in range(len(nums)):
        #     if i > 0 and nums[i] == nums[i-1]:
        #         continue
        #     first = nums[i]
        #     for j in range(i, len(nums)-1):
        #         if j > 0 and nums[j] == nums[j-1]:
        #             continue
        #         res = first + nums[j+1]
        #         find = 0 - res
        #         if find in nums[j+2:] and [first, nums[j+1], find] not in list_res:
        #             list_res += [[first, nums[j+1], find]]
        # return list_res