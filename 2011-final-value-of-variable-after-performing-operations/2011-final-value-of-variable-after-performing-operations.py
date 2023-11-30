class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        answer = 0
        for operation in operations:
            if '-' in operation:
                answer -= 1
            elif '+' in operation:
                answer += 1
        return answer