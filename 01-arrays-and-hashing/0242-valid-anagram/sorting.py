class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        """
        Sorting yaklaşımı.

        İki string anagramsa karakterleri sıralandığında
        aynı sonucu vermeleri gerekir.

        Zaman Karmaşıklığı: O(n log n)
        """

        if len(s) != len(t):
            return False

        return sorted(s) == sorted(t)


if __name__ == "__main__":
    s = "racecar"
    t = "carrace"

    solution = Solution()
    result = solution.isAnagram(s, t)

    print(result)