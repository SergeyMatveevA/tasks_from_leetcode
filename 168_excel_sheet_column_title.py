class Solution:
    def convertToTitle(self, n: int) -> str:
        symbols = [chr(symbol) for symbol in range(65, 91)]
        column_name = ''
        while n:
            n -= 1
            column_name = symbols[n % 26] + column_name
            n = n // 26
        return column_name
