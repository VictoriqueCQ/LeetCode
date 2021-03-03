from typing import List
class Solution:
    def maxProduct(self, words: List[str]) -> int:
        return max([len(w1) * len(w2) for w1 in words for w2 in words if not set(w1) & set(w2)] or [0])

        values = [0] * len(words)
        # 用位运算表示一个单词
        for i in range(len(words)):
            for alp in words[i]:
                values[i] |= 1 << (ord(alp) - 97)
        return max([len(words[i]) * len(words[j]) for i in range(len(words)) for j in range(i, len(words)) if
                    not values[i] & values[j]] or [0])

