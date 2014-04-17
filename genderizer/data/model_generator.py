import cPickle
from pymongo import MongoClient
from naiveBayesClassifier import tokenizer
from naiveBayesClassifier.trainer import Trainer

"""
This module generates trained data set, in other saying model
for naiveBayesClassifier. It reads pre-classified text such as
tweets. 

Each tweet should follow this structure:
{
    'tweet': 'hello. this is a tweet message'
    'gender': 'male'
}

The gender property can be either male or female.

After training process, the model will be serialized and written 
in a file in order to make it available for other modules.

EXTRA INFORMATION:
cPickle is used for serialization performance. Because we do not
need subclasses serialization, we will not be imposed by the 
disadvantage of cPickle's. 
"""

def generate(mongourl, database, collection, lang):

    c = MongoClient(mongourl)
    tweets = c[database][collection].find()
    trainer = Trainer(tokenizer)
    
    for tweet in tweets:
        trainer.train(tweet['tweet'], tweet['gender'])
    
    modelFileName = 'model_{}.txt'.format(lang)
    with open(modelFileName, 'wb') as modelFile:
        cPickle.dump(trainer.data, modelFile, cPickle.HIGHEST_PROTOCOL)
        print('OK : generated trained data has been writen in the file "{}"'.
            format(modelFileName))

if __name__ == '__main__':
    generate(
        mongourl = 'mongodb://192.168.1.170/test',
        database = 'test',
        collection = 'genderizedTweets',
        lang='tr')