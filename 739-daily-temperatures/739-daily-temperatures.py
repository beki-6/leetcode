class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        n = len(temperatures)
        wait = [0] * n
        for i in range(n):
            while stack != [] and temperatures[i] > temperatures[stack[-1]]:
                wait[stack[-1]] = i-stack[-1]
                stack.pop()
            stack.append(i)

        return wait