class Solution:
    def numberOfPowerfulInt(self, begin: int, end: int, maximum: int, suffix: str) -> int:
        if int(suffix) > end:
            return 0
        
        def calculate(pos, number, matched=0):
            if pos >= len(number) - len(suffix):
                if matched == 0:
                    return 1
                return 1 if int(number[pos:]) >= int(suffix) else 0
            
            if (pos, matched) in cache:
                return cache[(pos, matched)]
            
            result = 0
            if matched == 1:
                for digit in range(min(maximum, int(number[pos])) + 1):
                    if digit == int(number[pos]):
                        result += calculate(pos + 1, number, 1)
                    else:
                        result += calculate(pos + 1, number, 0)
            else:
                for digit in range(maximum + 1):
                    result += calculate(pos + 1, number, 0)
            
            cache[(pos, matched)] = result
            return cache[(pos, matched)]

        cache = {}
        if begin - 1 < int(suffix):
            begin_count = 0
        else:
            begin_count = calculate(0, str(begin - 1), 1)
        
        cache = {}
        if end < int(suffix):
            end_count = 0
        else:
            end_count = calculate(0, str(end), 1)

        return end_count - begin_count
