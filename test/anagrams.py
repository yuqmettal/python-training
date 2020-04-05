hola = {"Bob": 1}
print("Bob" in hola)

from collections import Counter

def funWithAnagrams(text):
    anagrams = []
    for ix in range(len(text)):
        lower_anagram = text[ix]
        has_anagram = False
        for current in range(ix + 1, len(text)):
            if sorted(lower_anagram) == sorted(text[current]):
                has_anagram = True
                lower_anagram = lower_anagram if lower_anagram < text[current] else lower_anagram
        if has_anagram:
            if sorted(lower_anagram) in [sorted(x) for x in anagrams]:
                index = None
                for anagram_index in range(len(anagrams)):
                    if sorted(lower_anagram) == sorted(anagrams[anagram_index]):
                        index = anagram_index
                anagram = anagrams.pop(index)
                lower_anagram = lower_anagram if lower_anagram < anagram else anagram
            anagrams.append(lower_anagram)
    return sorted(anagrams)

result = funWithAnagrams(["code", "aaagmnrs", "anagrams", 'doce'])
assert result == ["aaagmnrs", "code"]

result = funWithAnagrams(["poke", "pkoe", "okpe", 'ekop'])
assert result == ["poke"]

