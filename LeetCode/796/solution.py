class Solution:
    def rotateString(self, A: str, B: str) -> bool:
        # if A == B:
        #     return True
        # for i in range(len(A)):
        #     if A[i:len(A)] == B:
        #         return True
        #     A += A[i]
        # return False
        if len(A) == len(B) and B in A+A:
            return True
        return False