# Given an array of strings strs, group the anagrams together. You can return the answer in any order.

# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.


# Example 1:

# Input: strs = ["eat","tea","tan","ate","nat","bat"]
# Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
# Example 2:

# Input: strs = [""]
# Output: [[""]]
# Example 3:

# Input: strs = ["a"]
# Output: [["a"]]

from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        # solution 1
        # res = defaultdict(list)

        # for s in strs:
        #     count = [0] * 26  # a...z
        #     for c in s:
        #         count[ord(c) - ord("a")] += 1
        #     res[tuple(count)].append(s)
        # return res.values()
        # solution 2
        anagram_map = defaultdict(list)

        for word in strs:
            sorted_word = "".join(sorted(word))
            anagram_map[sorted_word].append(word)

        return list(anagram_map.values())


s = Solution()
strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
print(s.groupAnagrams(strs=strs))
