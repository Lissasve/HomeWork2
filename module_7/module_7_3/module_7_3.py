import string


class WordsFinder:
    def __init__(self, *file_names):
        self.file_names = file_names

    def get_all_words(self):
        all_words = {}
        punctuation_del = list(string.punctuation + '-')

        for file_name in self.file_names:
            with open(file_name, 'r', encoding='utf-8') as file:
                line = file.read().lower()
                for char in punctuation_del:
                    line = line.replace(char, ' ')
                words = line.split()
                all_words[file_name] = words
        return all_words

    def find(self, word):
        position_word = {}
        for file_name, words in self.get_all_words().items():
            if word.lower() in words:
                position = words.index(word.lower())
                position_word[file_name] = position
        return position_word

    def count(self, word):
        word_counts = {}
        for file_name, words in self.get_all_words().items():
            if word.lower() in words:
                count = words.count(word.lower())
                word_counts[file_name] = count
        return word_counts


finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words())  # Все слова
print(finder2.find('TEXT'))  # 3 слово по счёту
print(finder2.count('teXT'))  # 4 слова teXT в тексте всего