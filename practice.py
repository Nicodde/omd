from math import log


class CountVectorizer:
    """
    Позволяет получить терм-документную матрицу
    """

    def __init__(self):
        self.vocab = {}
        self.feature_names = []

    def fit_transform(self, text: list[str]) -> list[list]:
        """
        Берет текст из исходного списка и возвращает терм-документную матрицу
        """
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

    def get_feature_names(self) -> list[list]:
        """
        Возвращает список слов из исходного текста
        """
        return self.feature_names


class TfidfTransformer:
    """
    Класс, преобразующий матрицу счетчиков слов в TF-IDF представление.
    """

    def tf_transform(self, count_matrix: list) -> list[list]:
        """
        Принимает матрицу CountVectorizer и преобразует ее в форму TF.
        TF = повторений / всего
        """
        tf = []
        for words_list in count_matrix:
            total_sum = sum(words_list)
            tf_row = []
            for word in words_list:
                tf_row.append(round(word / total_sum, 3))
            tf.append(tf_row)
        return tf

    def idf_transform(self, count_matrix: list) -> list[float]:
        """
        Принимает матрицу CountVectorizer и преобразует ее в вектор IDF.
        IDF = ln((всего документов + 1) / (документов со словом + 1)) + 1
        """
        num_docs = len(count_matrix)
        num_words = len(count_matrix[0])
        idf = []

        for i in range(num_words):
            count_docs = sum([1 for doc in count_matrix if doc[i] > 0])
            idf_value = round(log((num_docs + 1) / (count_docs + 1)) + 1, 1)
            idf.append(idf_value)

        return idf

    def fit_transform(self, count_matrix: list) -> list[list]:
        """
        Принимает матрицу CountVectorizer и преобразует ее в матрицу TF-IDF.
        TF-IDF = TF * IDF
        """
        tf_matrix = self.tf_transform(count_matrix)
        idf_values = self.idf_transform(count_matrix)
        tfidf_matrix = []
        for i in range(len(tf_matrix)):
            tfidf_row = [
                round(tf * idf, 3) for tf, idf in zip(tf_matrix[i], idf_values)
            ]
            tfidf_matrix.append(tfidf_row)

        return tfidf_matrix


class TfidfVectorizer(CountVectorizer):
    """
    Класс, преобразующий текстовые данные в TF-IDF представление.
    """

    def __init__(self):
        """
        Инициализирует объект TfidfVectorizer.
        """
        super().__init__()
        self.tf_idf_transformer = TfidfTransformer()

    def fit_transform(self, corpus: list[str]) -> list[list]:
        """
        Преобразует текстовые данные в матрицу CountVectorizer
        через метод fit_transform класса CountVectorizer.
        Затем преобразует матрицу в TF-IDF
        через метод fit_transform класса TfidfTransformer.
        """
        count_matrix = super().fit_transform(corpus)
        result = self.tf_idf_transformer.fit_transform(count_matrix)
        return result


if __name__ == '__main__':
    corpus = [
        'Crock Pot Pasta Never boil pasta again',
        'Pasta Pomodoro Fresh ingredients Parmesan to taste',
    ]
    vectorizer = CountVectorizer()
    count_matrix = vectorizer.fit_transform(corpus)
    print(vectorizer.get_feature_names())
    print(count_matrix)

    transformer = TfidfTransformer()
    tf = transformer.tf_transform(count_matrix)
    idf = transformer.idf_transform(count_matrix)
    print(tf)
    print(idf)

    tfidf_matrix = transformer.fit_transform(count_matrix)
    print(tfidf_matrix)

    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform(corpus)
    print(tfidf_matrix)
