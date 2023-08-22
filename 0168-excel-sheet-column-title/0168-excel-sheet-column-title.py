class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        base = 64
        columnTitle = []
        
        while columnNumber > 0:
            remainder = columnNumber % 26
            columnNumber = columnNumber // 26
            if remainder > 0:
                columnTitle.append(chr(base + remainder))
            else:
                columnNumber -= 1
                columnTitle.append("Z")
                
        return "".join(columnTitle[:: -1])
        