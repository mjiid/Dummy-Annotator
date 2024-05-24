import nltk

class Tokenizer:
    def tokenize(self, text):
        tokens = nltk.word_tokenize(text)
        return tokens
