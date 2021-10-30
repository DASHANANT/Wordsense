
Get_Wordsense
=====
The whole idea of word sense is controversial. The meaning of a word is highly contextual and depends on its usage in sentence.

English is very difficult language to learn by robot as a lot of words are Ambiguous( Word with diffrent meanings). 

To solve this state-of-the-art problem, we have implemented the solution using Knowledge-Based Method ,
which concerned with identifying which sense of a word is used in a sentence.


Install
====

```
pip3 install -U nltk
nltk.download('stopwords')
pip3 install -U Get_Wordsense
```

Usage
=====

```python
$ python
>>> from Get_Wordsense import Get_sense
>>> sentence = 'I went to the bank to deposit my money'
>>> ambiguous_word = 'bank'
>>> print Get_sense(sentence, ambiguous_word, pos=None, synsets=None)
'a financial institution that accepts deposits and channels the money into lending activities'
```

Cite
====

To cite `Get_Wordsense`:

Anant Dashpute. 2021. Get_Wordsense: Python Implementation of Get_Wordsense. Retrieved from  https://github.com/DASHANANT/

In `bibtex`:

```
@misc{pywsd14,
author =   {Anant Dashpute},
title =    {Get_Wordsense: Python Implementation of Get_Wordsense},
howpublished = {https://github.com/DASHANANT/},
year = {2021}
}
```

***

References
=========

* Michael Lesk. 1986. Automatic sense disambiguation using machine readable dictionaries: how to tell a pine cone from an ice cream cone. In Proceedings of the 5th annual international conference on Systems documentation (SIGDOC '86), Virginia DeBuys (Ed.). ACM, New York, NY, USA, 24-26. DOI=10.1145/318723.318728 http://doi.acm.org/10.1145/318723.318728

* Zhi Zhong and Hwee Tou Ng. 2010. It makes sense: a wide-coverage word sense disambiguation system for free text. In <i>Proceedings of the ACL 2010 System Demonstrations</i> (<i>ACLDemos '10</i>). Association for Computational Linguistics, USA, 78–83.
