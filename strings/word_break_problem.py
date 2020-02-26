def word_found(a):
    """
    Function to check if the input string can be formed by using the words in the all_words list.
    It keeps two pointers on index 0 and 1, and keeps checking if the substring created is found in all_words list or
    not.
    If present, it checks the other substrings in the input string. If all substrings are found in the list, it returns
    True else False
    :param a: String
    :return: List
    """
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
