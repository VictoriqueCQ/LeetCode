class Solution:
    def sortArrayByParityII(self, A: List[int]) -> List[int]:
        odd, even = [], []
        for num in A:
            if num % 2 == 1:
                odd.append(num)
            else:
                even.append(num)

        res = []
        for i in range(len(odd)):
            res.append(even[i])
            res.append(odd[i])

        return res

