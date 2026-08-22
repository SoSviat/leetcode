class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        # temp_len = len(temperatures)
        # answer = [0] * temp_len
         
        # for i in range(temp_len):
        #     for j in range(i+1, temp_len):
        #         if temperatures[j] > temperatures[i]:
        #             answer[i] = j - i
        #             break
        # return answer

        # O(n2)
        # O(1)

        temp_len = len(temperatures)
        answer = [0] * temp_len
        stack = []

        for i in range(temp_len):
            while stack and temperatures[i] > temperatures[stack[-1]]:
                prev_index = stack.pop()
                answer[prev_index] = i - prev_index
            stack.append(i)

        return answer
        # O(n)
        # O(n)
