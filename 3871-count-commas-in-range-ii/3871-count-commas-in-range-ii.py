class Solution:
    def countCommas(self, n: int) -> int:
        ranges = [
            (1000, 10**6 - 1, 1),      
            (10**6, 10**9 - 1, 2),     
            (10**9, 10**12 - 1, 3),     
            (10**12, 10**15 - 1, 4),  
            (10**15, 10**15, 5),  
        ]
        
        total = 0
        for start, end, commas in ranges:
            if n >= start:
                total += (min(n, end) - start + 1) * commas
        return total
