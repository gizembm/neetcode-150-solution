class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        """
        Frequency Array yaklaşımı.

        Problem sadece küçük İngilizce harflerden oluştuğu için
        a-z arasındaki 26 karakter için 26 elemanlı bir sayaç
        dizisi kullanabiliriz.

        s içerisindeki karakterler için sayacı artırır,
        t içerisindeki karakterler için azaltırız.

        Sonunda bütün sayaçlar 0 ise stringler anagramdır.

        Zaman Karmaşıklığı: O(n)
        Alan Karmaşıklığı: O(1)
        """

        if len(s) != len(t):
            return False

        count = [0] * 26

        for char in s:
            index = ord(char) - ord("a")
            count[index] += 1

        for char in t:
            index = ord(char) - ord("a")
            count[index] -= 1

        return all(value == 0 for value in count)


if __name__ == "__main__":
    s = "aabc"
    t = "abca"

    solution = Solution()
    result = solution.isAnagram(s, t)

    print(result)