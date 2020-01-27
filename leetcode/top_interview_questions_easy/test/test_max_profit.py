from unittest import TestCase

from src import MaxProfit


class TestBestTimeToBuyAndSellStock(TestCase):
    def test_solution(self):
        prices = [7, 1, 5, 3, 6, 4]
        max_profit = MaxProfit.solution(prices)
        assert max_profit == 7, "max profit: {}".format(max_profit)

    def test_solution2(self):
        prices = [7, 1, 5, 3, 6, 4]
        max_profit = MaxProfit.solution2(prices)
        assert max_profit == 7, "max profit: {}".format(max_profit)

    def test_solution3(self):
        prices = [7, 1, 5, 3, 6, 4]
        max_profit = MaxProfit.solution3(prices)
        assert max_profit == 7, "max profit: {}".format(max_profit)
