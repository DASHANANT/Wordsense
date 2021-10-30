import setuptools


with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="Get_Wordsense",
    version="1.0",
    author="Anant Dashpute",
    REQUIRES_PYTHON = '>=3.6.0'    
    author_email="anantdashpute@gmail.com",
    description="This module used to get meaning of word in a input sentence",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="",
    packages=setuptools.find_packages(),
    install_requires=['nltk','nltk.corpus','nltk.stem']
    keywords=['WSD', 'Sense', 'Disambiguation', 'Lesk', 'word-sense','stem','Knowlege based','wordnet','NLP'],
    classifiers=[
        "Programming Language :: Python 3",
        "Operating System :: OS Independent",
    ],
)