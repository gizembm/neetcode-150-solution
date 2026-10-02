class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        """
        Hash Map / Frequency Counting yaklaşımı.

        Her iki string içerisindeki karakterlerin kaç kez
        geçtiğini ayrı dictionary'lerde tutarız.

        Son olarak iki frequency map'i karşılaştırırız.

        Zaman Karmaşıklığı: O(n)
        Alan Karmaşıklığı: O(n)
        """

        if len(s) != len(t):
            return False

        count_s = {}
        count_t = {}

        for char in s:
            count_s[char] = count_s.get(char, 0) + 1

        for char in t:
            count_t[char] = count_t.get(char, 0) + 1

        return count_s == count_t


if __name__ == "__main__":
    s = "aabc"
    t = "abca"

    solution = Solution()
    result = solution.isAnagram(s, t)

    print(result)