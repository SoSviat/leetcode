class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        queue = deque(range(len(tickets)))
        time = 0

        while queue:
            i = queue.popleft()
            tickets[i] -= 1
            time += 1

            if i == k and tickets[i] == 0:
                return time

            if tickets[i] > 0:
                queue.append(i)


        #O(n)
        #O(n)