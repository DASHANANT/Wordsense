from nltk.corpus import wordnet
from nltk.stem import WordNetLemmatizer
from nltk.stem import PorterStemmer
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
        context[i]=str(stem(context[i])) 
    context = set(context).difference(stopwords)    
    AmbiguousWords=[]
    for i in context:            
        if len(wordnet.synsets(i))>2:
            AmbiguousWords.append(i)
    return AmbiguousWords
    
    
def Get_Sense(sentence, ambiguous_word, pos=None, synsets=None):       
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
        gloss = gloss.difference(stopword)
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



