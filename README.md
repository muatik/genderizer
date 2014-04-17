Genderize
======================

Genderize is a language independent module which tries to detect gender by looking given first names and/or analyzing sample texts. 

##Installation
You can install this package using the following ```pip``` command:

```sh
$ sudo pip install genderize
```


##Examples

```python
1
print Genderize.detect(firstName = 'John')
# >>> male

print Genderize.detect(firstName = 'Marry')
# >>> female

print Genderize.detect(firstName = 'mustafa')
# >>> male

print Genderize.detect(firstName = 'fatma')
# >>> female

print Genderize.detect(firstName = 'fikret')
# >>> None

print Genderize.detect(firstName = 'fikret', text='galatasary maçı kaçmaz')
# >>> male

print Genderize.detect(firstName = 'fikret', text='annemlerle yemek yedik')
# >>> female

print Genderize.detect(text='askerlik yoklamasını kaçırdım mk')
# >>> male

print Genderize.detect(text='bana çiçek alan erkek için canım feda')
# >>> female

print Genderize.detect(firstName='fatma', text='askerlik yoklamasını kaçırdım mk')
# >>> female

print Genderize.detect(text='futbol sevgi')
# >>> None

print Genderize.detect(text='lan bi siktir git')
# >>> male

```
***Note***: You may claim that women can say ```lan bi siktir git```, of course. But the probability of being female is less than the probability of being male according the trained data of the classifier.

By the way, in Turkish saying 'lan bi siktir git' makes you quite rude.


## How It Works
Genderize is a module which tries to detect gender by looking given first names and/or analyzing sample text of a person. 

If a first name is definitely used for only one gender, the system will accept this gender and will not make any further analysis. For example, while 'Mustafa', 'Osman', 'Hasan' is used in Turkish only for male; 'Fatma', 'Ceyda', 'Elif' only for female.

When looking at first names does not infer any gender for sure, the system will make text analysis if it is given. For example; 'Ekim', 'Meric', or 'Tümay' is used for both male and female.

The text analysis is the classification of sample texts. It simply try to compute the probability of being male or female mining the sample text. In this system Naive Bayesian Classification is adopted and [naiveBayesClassifier][1] is used.

## How To Improve It
TODO: write a step by step guide

##Preparing Language Dependent Training Sets
TODO: give a few examples

## Customization and Optimization
TODO: Tell what options are there and when to choose
```python
MongoNamesCollection.mongodbURL = 'mongodb://192.168.1.170'
Genderize.init(
    lang='tr',
    namesCollection=MongoNamesCollection
)

MemcachedNamesCollection.memcacheHost = '127.0.0.1:11211'
Genderize.init(
    lang='tr',
    namesCollection=MemcachedNamesCollection
)

Genderize.init(
    lang='tr',
    namesCollection=NamesCollection,
    classifier=Classifier(CachedModel.get('tr'), tokenizer)
)

print Genderize.detect(firstName = 'fikret', text='annem')

```

## TODO
* inline docs
* unit-tests

## AUTHORS
* Mustafa Atik [@muatik][2]
* Nejdet Yucesoy @nejdetckenobi


  [1]: https://github.com/muatik/naive-bayes-classifier
  [2]: https://twitter.com/muatik2