class RecentCounter:

    def __init__(self):
        self.q = deque()


    def ping(self, t: int) -> int:
        self.q.append(t)
        #before len
        period = t - 3000
        while self.q[0] < period:
            self.q.popleft()

        return len(self.q)

    #print(self.q)
# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)