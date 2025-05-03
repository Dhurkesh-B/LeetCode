class Solution(object):
    def minDominoRotations(self, tops, bottoms):
        """
        :type tops: List[int]
        :type bottoms: List[int]
        :rtype: int
        """
        def check(x):
            rotations_a = rotations_b = 0
            for i in range(len(tops)):
                # If neither top nor bottom has the value, it's impossible
                if tops[i] != x and bottoms[i] != x:
                    return float('inf')
                elif tops[i] != x:
                    rotations_a += 1  # Need to rotate top to match x
                elif bottoms[i] != x:
                    rotations_b += 1  # Need to rotate bottom to match x
            return min(rotations_a, rotations_b)

        result = min(check(tops[0]), check(bottoms[0]))
        return result if result != float('inf') else -1
