import heapq
from itertools import combinations

from tqdm import tqdm

# Global language information
vowels = {"а", "е", "ё", "и", "о", "у", "ы", "э", "ю", "я"}
consonants = ["н", "р", "т", "к", "с", "л", "в", "п", "д", "м", "з", "б", "ч", "г", "ц", "ш", "ж", "х", "ф", "й", "щ"]
words = list()
with open("new_nouns.txt", "r") as f:
    for word in f:
        words.append(word.strip())


def evaluate(letters):
    dig2sym = dict()
    sym2dig = dict()
    for i, letter in enumerate(letters):
        dig2sym[str(i)] = letter
        sym2dig[letter] = str(i)

    def word_to_number(word):
        number = ""
        for char in word:
            if char in sym2dig:
                number += sym2dig[char]
                if len(number) >= 3:
                    return None
        if len(number) == 0:
            return None
        return number

    def score(word, letter):
        score = 0
        # Symbols
        score += len(word)
        # Syllables
        score += len([v for v in word if v in vowels])
        # Starts with its letters
        if word[0] == letter:
            score -= 3
        return score

    correspondence = dict()

    for word in words:
        if len(word) < 3:
            continue
        number = word_to_number(word)
        if number is not None:
            current_score = score(word, dig2sym[number[0]])
            if number in correspondence:
                if current_score < correspondence[number][1]:
                    correspondence[number] = (word, current_score)
            else:
                correspondence[number] = (word, current_score)

    mnemonic_score = 0
    for key, value in correspondence.items():
        mnemonic_score += value[1]

    return (letters, correspondence, mnemonic_score)


threshold = 108
best_results = []
combs = list(combinations(consonants, 10))

for letters in tqdm(combs, total=len(list(combs))):
    letters, correspondence, mnemonic_score = evaluate(letters)

    if len(correspondence) < 108:
        continue
    print(letters)
    print(mnemonic_score)
    print(len(correspondence))

    if len(best_results) < 10:
        heapq.heappush(best_results, (-mnemonic_score, letters, correspondence))
    else:
        heapq.heappushpop(best_results, (-mnemonic_score, letters, correspondence))

sorted_best_results = sorted(best_results, key=lambda x: -x[0])


print("We got winners")
for score, letters, correspondence in sorted_best_results:
    print(f"Score: {-score}, Letters: {letters}, Correspondence: {correspondence}")
