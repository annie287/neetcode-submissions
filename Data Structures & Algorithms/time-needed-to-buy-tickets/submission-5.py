class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        i = 0
        time = 0

        while tickets[k] != 0:
            if tickets[i] > 0:
                tickets[i] -= 1
                time += 1

            if i >= len(tickets) - 1:
                i = 0
            else:
                i += 1
        return time