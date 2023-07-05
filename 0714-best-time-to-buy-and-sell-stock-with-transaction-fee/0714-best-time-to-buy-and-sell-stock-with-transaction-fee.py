class Solution(object):
    def maxProfit(self, prices, fee):
        """
        :type prices: List[int]
        :type fee: int
        :rtype: int
        """
        cache = {}

        def buy(index):
            # We could decide to buy or not buy at this index
            return max(main(index + 1, False) - prices[index], main(index + 1, True))

        def sell(index, buy_index):
            # We could decide to sell or not
            return max(
                main(index + 1, True) + prices[index] - fee,
                main(index + 1, False),
            )

        def main(index, turn):
            if (index, turn) in cache:
                return cache[(index, turn)]

            if index == len(prices):
                return 0

            if turn:
                profit = buy(index)
            else:
                profit = sell(index, index)

            cache[(index, turn)] = profit
            return profit

        return main(0, True)
