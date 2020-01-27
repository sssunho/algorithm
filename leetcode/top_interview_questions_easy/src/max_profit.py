# https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/array/564/


class MaxProfit:
    @staticmethod
    def solution(prices: list) -> int:
        if not prices:
            return 0

        max_profit = 0
        for i in range(1, len(prices)):
            if prices[i] > prices[i - 1]:
                max_profit += prices[i] - prices[i - 1]
        return max_profit

    @staticmethod
    def solution2(prices: list) -> int:
        max_profit = 0
        for i in range(len(prices) - 1):
            max_profit += max(prices[i + 1] - prices[i], 0)
        return max_profit

    @staticmethod
    def solution3(prices: list) -> int:
        return sum(
            prices[i + 1] - prices[i]
            for i in range(len(prices) - 1)
            if prices[i + 1] > prices[i]
        )
