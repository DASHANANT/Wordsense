from setuptools import setup
from setuptools import find_packages
# with open("README.md", "r") as fh:
#     long_description = fh.read()

setup(
    name="Get_Wordsense",
    author="Anant Dashpute",
    author_email="<anantdashpute@gmail.com>",
    description="This module is used to get Wordsense of ambiguous word",
    # long_description=long_description,
    # long_description_content_type="text/markdown",
    url="https://github.com/DASHANANT/Get_Wordsense",
    packages=find_packages(),    
    py_modules=["Word_sense"],
    install_requires=['nltk'],
    keywords=['WSD', 'Sense', 'Disambiguation', 'Lesk',
              'word-sense', 'stem', 'Knowlege based', 'wordnet', 'NLP'],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
