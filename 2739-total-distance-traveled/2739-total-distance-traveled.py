class Solution:
    def distanceTraveled(self, mainTank: int, additionalTank: int) -> int:
        # mainTank 1리터 -> 10km 갈 수 있음
        answer = 0
        while mainTank > 0:
            # main에 5리터 이상 남아있다면
            # -> (main * 10) -> main - 5
            if mainTank >= 5:
                mainTank -= 5
                answer += 5
                # add에 1리터 이상의 연료가 남아있으면
                # -> add - 1 -> main + 1
                if additionalTank >= 1:
                    additionalTank -= 1
                    mainTank += 1
            # main이 5리터보다 적게 들어있다면
            # -> (main * 10)km 만 갈 수 있음
            if mainTank < 5:
                answer += mainTank
                mainTank = 0
        return answer * 10