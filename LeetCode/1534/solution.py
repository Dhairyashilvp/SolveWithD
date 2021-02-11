class Solution:
    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        n, result = len(arr), 0
        for i in range(n):
            for k in range(i + 1, n):
                if abs(arr[i] - arr[k]) > c: 
                    continue
                temp = 0
                for j in range(i + 1, k):
                    if abs(arr[i] - arr[j]) <= a and abs(arr[j] - arr[k]) <= b:
                        temp += 1
                result += temp
                print(result)
        return result