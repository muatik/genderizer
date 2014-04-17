import memcache
import cPickle
import os

class CachedModel(object):
    """
    An interface class which holds model data,  in other saying
    trained data for naiveBayesClassifier.

    The data is prepared and stored pickling in a file. This class
    loads it once and serves the loaded one each time.

    New models can be generated using the ```data/model_generator.py```

    CAUTION:
    The modal data may be very large. Because all the data will be 
    loaded into memory, you need to give some attention to this.
    Maybe you can write your interface which loads only required data,
    or you can write a class which works with memcached.
    """

    isInitialized = None

    lang = 'en'
    loadedLang = 'en'
    modelFileFormat = 'data/model_{}.txt'
    model = None

    @classmethod
    def init(cls):
        if not cls.model:
            path = os.path.abspath(__file__)
            dir_path = os.path.dirname(path) + '/'
            modelFileName = dir_path + cls.modelFileFormat.format(cls.lang)
            with open(modelFileName, 'rb') as modelFile:
                cls.model = cPickle.load(modelFile)
                cls.loadedLang = cls.lang
        cls.isInitialized = True

    @classmethod
    def get(cls, lang='en'):
        cls.lang = lang
        if not cls.isInitialized or cls.lang != cls.loadedLang:
            cls.init()

        return cls.model  
