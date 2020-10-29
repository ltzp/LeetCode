class Solution(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        result = True
        hash_map = dict()
        word_hash_map = dict()
        words = str.split(" ")
        if len(pattern) != len(words):
            return False
        for i in range(0, len(pattern)):
            if pattern[i] not in hash_map:
                hash_map[pattern[i]] = words[i]
            else:
                if hash_map.get(pattern[i]) != words[i]:
                    result = False
                    break
                else:
                    continue
            if words[i] not in word_hash_map:
                word_hash_map[words[i]] = pattern[i]
            else:
                if word_hash_map.get(words[i]) != pattern[i]:
                    result = False
                    break
                else:
                    continue
        return result


if __name__ == "__main__":
    solve = Solution()
    pattern = "abba"
    str = "dog dog dog dog"
    result = solve.wordPattern(pattern, str)
    print(result)