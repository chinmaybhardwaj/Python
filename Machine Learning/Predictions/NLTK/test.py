
# 1. Word tokenizer
# 2. Sentence tokenizer
# 3. Lexicon - words and their meanings
# 4. Corpora - body of text. eg: journals, speeches


# =============================================================================
#  STOP WORDS
# =============================================================================

from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

example_sentence = 'This is an example of showing off stop words filtration.'

stop_words = set(stopwords.words('english'))

words = word_tokenize(example_sentence)
filtered_sentence = []

for w in words:
    if w not in stop_words:
        filtered_sentence.append(w)
#        print(w)
        
        
# using list generators        
#filtered_sentence = [w for w in words if not w in stop_words]

        
# =============================================================================
#     STEMMING WORDS
# =============================================================================

from nltk.stem import PorterStemmer
#from nltk.tokenize import word_tokenize

ps = PorterStemmer()

example_words = ['python','pythoner','pythoning','pythoned','pythonly']

#for w in example_words:
#    print(ps.stem(w))



# =============================================================================
# 
# =============================================================================
