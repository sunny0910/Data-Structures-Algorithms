def word_found(a):
    if not a:
        return
    i = 0
    j = 1
    found_words = []
    while j <= len(a):
        word = a[i:j]
        if word in all_word:
            found_words.append(word)
            i = j
            if j == len(a):
                return found_words
            continue
        j += 1
    return False

all_word = ["i", "like", "sam", "sung", "samsung", "mobile", "ice", "cream", "icecream", "man", "go", "mango"]
x = "ilikesam"
print(word_found(x))