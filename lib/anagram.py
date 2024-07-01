# your code goes here!

class Anagram:
    def __init__(self, word):
        self.word = word.lower()
        self.sorted_word = sorted(self.word)

    def match(self, words):
        result = []
        for word in words:
            if self._is_anagram(word.lower()):
                result.append(word)
        return result

    def _is_anagram(self, other_word):
        return other_word != self.word and sorted(other_word) == self.sorted_word
