class Solution:
    def countTestedDevices(self, batteryPercentages: List[int]) -> int:
        answer = 0
        for i in range(len(batteryPercentages)):
            if batteryPercentages[i] <= 0:
                continue
            answer += 1
            for j in range(i+1, len(batteryPercentages)):
                batteryPercentages[j] -= 1
                if batteryPercentages[j] <= 0:
                    batteryPercentages[j] = 0
        return answer