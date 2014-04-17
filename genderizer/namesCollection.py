import os


class NamesCollection(object):
    """
    This is a primitive interface for the collection of first names.
    
    When the first query is received, it reads all the first
    names and their extra information from source file. So this step
    may take some time.

    After the first request and successful importing, it serves the
    data from memory.

    For more than one request, this class would be ok. But you have
    better choose a reasonable interface such as memcache interface or
    mongodb interface.
    """
    
    isInitialized = None
    
    collectionSourceFile = 'data/name_gender.csv'
    collection = None

    @classmethod
    def init(cls):
        if not cls.collection:
            cls.collection = cls.loadFromSource()
    
    @classmethod
    def loadFromSource(cls):
        # will produce something like this: 
        # {'kamil': {'tr': 'm'}, 'mustafa': {'en': 'm', 'tr': 'm'}, 'kim': {'sk': 'm', 'nl': 'f'}}
        items = {}
        path = os.path.abspath(__file__)
        dir_path = os.path.dirname(path) + '/'
        for i in open(dir_path + '/' + cls.collectionSourceFile):
            
            item = i.strip().split(',')
            firstName = item[0].lower()
            
            if len(item) == 2:
                item.append('en')

            item = {item[2]:item[1]}

            if firstName in items:
                items[firstName] = dict(items[firstName].items() + item.items())
            else:
                items[firstName] = item

        return items


    @classmethod
    def getGender(cls, firstName, lang='en'):
        if not cls.isInitialized:
            cls.init()

        firstName = firstName.lower()
        nameInfo = cls.collection.get(firstName, None)
        if not nameInfo:
            return None

        if nameInfo.get(lang, None):
            return {'name': firstName, 'gender': nameInfo[lang], 'lang': lang}
        elif nameInfo.get('en', None):
            return {'name': firstName, 'gender': nameInfo['en'], 'lang': 'en'}
        else:
            return None
