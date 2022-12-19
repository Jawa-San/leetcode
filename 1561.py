class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort(reverse = True)
        triplets = len(piles) // 3
        res = 0

        for i in range(1, len(piles) - (triplets), 2):
            res += piles[i]

        return res