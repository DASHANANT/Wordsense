from nltk.stem import PorterStemmer
from nltk.stem import WordNetLemmatizer
from nltk.corpus import wordnet
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import re
import nltk
nltk.download('stopwords')
stopwords = set(stopwords.words('english'))

functionwords = {'everyone', 'himself', 'it', 'his', 'everything', 'little', 'those', 'inside', 'on', 'off', 'over',
                 'of', 'first', 'within', 'around', 'near', 'so', 'would', 'else', 'for', 'moreover', 'besides',
                 'into', 'while', 'here', 'never', 'such', 'each', 'who', 'anyone', 'through', 'despite', 'might',
                 'that', 'will', 'anything', 'in', 'therefore', 'your', 'someone', 'a', 'few', 'do', 'second', 'down',
                 'themself', 'usually', 'one', 'with', 'any', 'onto', 'all', 'to', 'must', 'herself', 'him', 'most', 'much',
                 'but', 'along', 'should', 'my', 'an', 'no', 'against', 'before', 'could', 'now', 'there', 'meanwhile',
                 'be', 'instead', 'during', 'them', 'from', 'less', 'if', 'something', 'ones', 'he', 'two', 'sometimes',
                 'yours', 'have', 'however', 'otherwise', 'its', 'though', 'often', 'toward', 'than', 'their', 'then',
                 'half', 'least', 'although', 'nothing', 'her', 'next', 'as', 'across', 'always', 'many', 'how', 'anyway',
                 'when', 'this', 'behind', 'own', 'both', 'at', 'itself', 'last', 'hers', 'other', 'they', 'our',
                 'incidentally', 'may', 'whose', 'beside', 'without', 'about', 'she', 'some', 'where', 'can', 'and',
                 'because', 'every', 'theirs', 'twice', 'another', 'since', 'what', 'after', 'which', 'these', 'more',
                 'shall', 'by', 'several', 'the', 'or'}

stopwords = stopwords.update(functionwords)
ps = PorterStemmer()
lm = WordNetLemmatizer()


def stem(word):
    word = lm.lemmatize(word)
    if wordnet.synsets(ps.stem(word)) == wordnet.synsets(word):
        return ps.stem(word)
    else:
        return word


def Get_AmbiguousWords(sentence):
    context = set(word_tokenize(sentence))
    context = list(context)
    for i in range(len(context)):
        context[i] = str(stem(context[i]))
    context = set(context).difference(stopwords)
    AmbiguousWords = []
    for i in context:
        if len(wordnet.synsets(i)) > 2:
            AmbiguousWords.append(i)
    return AmbiguousWords


def Get_Sense(sentence, ambiguous_word, pos=None, synsets=None):

    def tokenized_sent(self, k):
        string = str(k)
        tokens = set(word_tokenize(string))
        tokens = list(tokens)
        for i in range(len(tokens)):
            tokens[i] = str(self.stem(tokens[i]))
        tokens = set(tokens)
        return tokens

    context = set(sentence)
    context = [stem(w) for w in context]

    if synsets is None:
        synsets = wordnet.synsets(ambiguous_word)

    if pos:
        synsets = [ss for ss in synsets if str(ss.pos()) == pos]

    bag = []

    #"Creating A bag of words ,for each synset , using its hypernyms,hyponyms definiation and examples"

    for ss in synsets:
        gloss = set(ss.definition().split())

        for s in ss.hypernyms():
            gloss = gloss.union(tokenized_sent(
                re.sub('[^a-zA-Z.\d\s]', '', str(s.definition()))))
            gloss = gloss.union(tokenized_sent(
                re.sub('[^a-zA-Z.\d\s]', '', str(s.examples()))))
        for s in ss.hyponyms():
            gloss = gloss.union(tokenized_sent(
                re.sub('[^a-zA-Z.\d\s]', '', str(s.definition()))))
            gloss = gloss.union(tokenized_sent(
                re.sub('[^a-zA-Z.\d\s]', '', str(s.examples()))))

        # "to remove stopwords"
        gloss = gloss.difference(stopwords)
        gloss = list(gloss)
        for i in range(len(gloss)):
            # "Stemming each word"
            gloss[i] = str(stem(gloss[i]))
        # "to remove duplicates"
        gloss = set(gloss)
        # "Successful Creation for each synsets"
        bag.append(gloss)

    if not synsets:
        return None

    best_sense = synsets[0]
    max_overlap = 0

    #"Finding Intersection -Stemming makes it more intersections"

    for k in range(len(synsets)):
        overlap = len(context.intersection(bag[k]))
        if overlap > max_overlap:
            max_overlap = overlap
            best_sense = synsets[k]

    return best_sense
    #"Returns best sense of the word"
