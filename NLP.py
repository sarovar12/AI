import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk import pos_tag


# nltk.download('punkt')
# nltk.download('stopwords')
# nltk.download('averaged_perceptron_tagger')

# Sample text
text = "NLTK (Natural Language Toolkit) is a leading platform for building Python programs to work with human language data. It provides easy-to-use interfaces to over 50 corpora and lexical resources such as WordNet. NLTK also includes a suite of text processing libraries for classification, tokenization, stemming, tagging, parsing, semantic reasoning, and wrappers for industrial-strength NLP libraries."

# Sentence tokenization
sentences = sent_tokenize(text)
print("Sentence Tokenization:")
for sentence in sentences:
    print(sentence)
print()

# Word tokenization
words = word_tokenize(text)
print("Word Tokenization:")
for word in words:
    print(word)
print()

# Stop words filtering
stop_words = set(stopwords.words("english"))
filtered_words = [word for word in words if word.casefold() not in stop_words]
print("Stop Words Filtering:")
print(filtered_words)
print()

# Word stemming
stemmer = PorterStemmer()
stemmed_words = [stemmer.stem(word) for word in filtered_words]
print("Word Stemming:")
print(stemmed_words)
print()

# POS tagging
pos_tags = pos_tag(words)
print("POS Tagging:")
for word, pos in pos_tags:
    print(f"{word} => {pos}")

#Footer
print("Question no.10")
print("Name: ")
print("Roll no : ")
print("Section:A")

