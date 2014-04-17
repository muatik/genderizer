import os
from pymongo import MongoClient

class MongoNamesCollection(object):
    """
    This is a mongodb interface for the collection of first names.
    
    For the first time, if it is not imported yet, all the first
    names and their extra information will be imported into the 
    mongodb collection.
    """

    mongodbURL = 'mongodb://localhost/'
    database = 'test'
    mongoclient = None
    collection = None
    isInitialized = None
    
    collectionSourceFile = 'data/name_gender.csv'
    collectionName = 'firstNames'
    
    @classmethod
    def init(cls):
        cls.mongoclient = MongoClient(cls.mongodbURL)
        cls.collection = cls.mongoclient['test'][cls.collectionName]

        if not cls.collection.count() > 0:
            cls.loadFromSource()

    
    @classmethod
    def loadFromSource(cls):
        # will produce something like this: 
        # {'kamil': {'tr': 'm'}, 'mustafa': {'en': 'm', 'tr': 'm'}, 'kim': {'sk': 'm', 'nl': 'f'}}
        items = {}
        path = os.path.abspath(__file__)
        dir_path = os.path.dirname(path) + '/'
        for i in open(dir_path + '/' +cls.collectionSourceFile):
            
            item = i.strip().split(',')

            firstName = item[0].lower()

            if len(item) == 2:
                item.append('en')

            cls.collection.insert({
                'firstName' : firstName,
                'gender' : item[1],
                'lang' : item[2],
                })


    @classmethod
    def getGender(cls, firstName, lang='en'):
        if not cls.isInitialized:
            cls.init()

        firstName = firstName.lower()
        nameInfo = cls.collection.find_one({
            'firstName': firstName,
            'lang': lang
            })

        if not nameInfo and lang != 'en':
            return cls.getGender(firstName, 'en')
        elif not nameInfo:
            return None
        
        return {'name': firstName, 'gender': nameInfo['gender'], 'lang': lang}
