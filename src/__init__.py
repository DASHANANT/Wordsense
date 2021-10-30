import nltk
from nltk.corpus import wordnet
from nltk.stem import WordNetLemmatizer
from nltk.stem import PorterStemmer
from Word_sense import *
from nltk.corpus import stopwords
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



