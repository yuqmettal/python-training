from collections import Counter

def checkMagazine(magazine, note):
    return Counter(note) - Counter(magazine) == {}

magazine = ['ive', 'got', 'a', 'lovely', 'bunch', 'of', 'coconuts']
note = ['ive', 'got', 'some', 'coconuts']
result = checkMagazine(magazine, note)
print(result)

magazine = ['give', 'me', 'one', 'grand', 'today', 'night']
note = ['give', 'one', 'grand', 'today']
result = checkMagazine(magazine, note)
print(result)