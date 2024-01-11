class Solution:
    def squareIsWhite(self, coordinates: str) -> bool:
        alphabet, number = coordinates
        answer = True
        if alphabet in 'aceg':
            if number in '1357':
                answer = False
            else:
                answer = True
        else:
            if number in '1357':
                answer = True
            else:
                answer = False
        return answer