class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        j = 0
        i = 0
        while pushed != []:
            if pushed[i] != popped[j]:
                if i < len(pushed)-1:
                    i += 1  
                else:
                    return False  
            else:
                pushed.pop(i)
                if i != 0:
                    i -= 1
                j += 1

        if pushed == []:
            return True
        else:
            return False