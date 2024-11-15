import io
class WordsFinder:
    def __init__(self,*name_file):
        self.name = (name_file)
    def get_all_words(self):
        all_words = {}
        index = [',', '.', '=', '!', '?', ';', ':', ' - ']
        for i in self.name:
            with open(i, 'r', encoding='utf-8') as text:
                text.seek(0)
                all_words[i] = text.read().lower().split()
        for b in list(all_words.values())[0]:
            for s in index:
                if s in b :
                    list(all_words.values())[0][len(b)] = list(all_words.values())[0][len(b)].replace(s,'')
        return all_words
    def find(self,name_word):
        for i in list(self.get_all_words().values())[0]:
            if i == name_word.lower():
                return len(i)-1

    def count(self,count_word):
        count = 0
        for i in list(self.get_all_words().values())[0]:
            if i == count_word.lower():
                count += 1
        return count

finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words())  # Все слова
print(finder2.find('TEXT'))  # 3 слово по счёту
print(finder2.count('teXT'))  # 4 слова teXT в тексте всего