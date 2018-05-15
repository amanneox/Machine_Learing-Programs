from nltk.stem.porter import PorterStemmer
import re
porter_stemmer = PorterStemmer()

x = input()

x=list(re.split("\s",x))

print(x)

print([porter_stemmer.stem(i) for i in x])
