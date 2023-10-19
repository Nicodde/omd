class CountVectorizer:
    def __init__(self):
        self.vocab = {}
        self.feature_names = []

    def fit_transform(self, text):
        if not isinstance(text, list) or not all(
            isinstance(sentence, str) for sentence in text
        ):
            raise ValueError('В инпуте должен быть лист со строками внутри.')

        for sentence in text:
            lower_words = sentence.lower().split()
            for word in lower_words:
                if word not in self.vocab:
                    self.vocab[word] = len(self.vocab)
                    self.feature_names.append(word)

        matrix = []
        for sentence in text:
            word_counts = [0] * len(self.vocab)
            lower_words = sentence.lower().split()
            for word in lower_words:
                word_index = self.vocab[word]
                word_counts[word_index] += 1
            matrix.append(word_counts)

        return matrix

    def get_feature_names(self):
        return self.feature_names


if __name__ == '__main__':
    corpus = [
        'Crock Pot Pasta Never boil pasta again',
        'Pasta Pomodoro Fresh ingredients Parmesan to taste',
    ]
    vectorizer = CountVectorizer()
    count_matrix = vectorizer.fit_transform(corpus)
    print(vectorizer.get_feature_names())
    print(count_matrix)
