from nltk.corpus import stopwords
import unittest


def in_stoplist(token):
    stop_words = set(stopwords.words('english'))
    stop_words.update(['.', ',', '"', "'", '?', '!', ':', ';', '(', ')', '[', ']', '{', '}'])
    return token in stop_words

class UTest(unittest.TestCase):
    def setUp(self):
        self.stop_words = set(stopwords.words('english'))
        self.stop_words.update(['.', ',', '"', "'", '?', '!', ':', ';', '(', ')', '[', ']', '{', '}'])

    def test_in(self):
        for tok in self.stop_words:
            self.assertTrue(in_stoplist(tok))

    def test_not_in(self):
        for line in open('sentiment.txt'):
            for tok in line.strip().split():
                if tok not in self.stop_words:
                    self.assertFalse(in_stoplist(tok))

if __name__ == '__main__':
    unittest.main()
