from collections import Counter


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        """
        Counter yaklaşımı.

        Counter, her karakterin kaç kez geçtiğini hesaplar.
        İki Counter aynıysa stringler anagramdır.

        Zaman Karmaşıklığı: O(n)
        Alan Karmaşıklığı: O(n)
        """

        return Counter(s) == Counter(t)


if __name__ == "__main__":
    s = "racecar"
    t = "carrace"

    solution = Solution()
    result = solution.isAnagram(s, t)

    print(result)