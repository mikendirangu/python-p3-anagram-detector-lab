# your code goes here!


class Anagram:
    def __init__(self, word):
        """
        Create an Anagram matcher for `word`.
        Comparison is case-insensitive and uses sorted letters.
        """
        self.word = word
        # canonical form used for comparisons (lowercase, sorted letters)
        self._key = sorted(word.lower())

    def match(self, candidates):
        """
        Return a list of candidates that are anagrams of the original word.
        Exact matches (case-insensitive) are excluded.
        """
        matches = []
        base_lower = self.word.lower()

        for candidate in candidates:
            cand_lower = candidate.lower()
            # exclude identical words (case-insensitive)
            if cand_lower == base_lower:
                continue
            if sorted(cand_lower) == self._key:
                matches.append(candidate)

        return matches
