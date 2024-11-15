def single_root_word(root_word, *other_words):
    same_words = []
    for perebor in list(other_words):
        word_lower = str(perebor).lower()
        if word_lower.count(root_word):
            same_words.append(perebor)
    return same_words
print(single_root_word("o","slovo",'prOvoda','ovOs', 'PizdOs', 'zadanie','slojnoe', 'biLO', 'no 9 spravilsa', 'prodam garaz'))