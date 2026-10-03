class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        groups = {}

        for word in strs:
            key = "".join(sorted(word))

            if key not in groups:
                groups[key] = []

            groups[key].append(word)

        return list(groups.values())


if __name__ == "__main__":
    strs = ["act", "pots", "tops", "cat", "stop", "hat"]

    solution = Solution()
    result = solution.groupAnagrams(strs)

    print(result)