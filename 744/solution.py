class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        result = "{"
        for i in letters:
            if i > target and i < result:
                result = i
        if result == "{":
            return letters[0]
        return result
