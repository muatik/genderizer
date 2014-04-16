from __future__ import division
import cPickle
import math

from naiveBayesClassifier import tokenizer
from naiveBayesClassifier.trainer import Trainer
from naiveBayesClassifier.classifier import Classifier

from memcacheNamesCollection import MemcacheNamesCollection



class Genderize(object):
    """docstring for Genderize"""
    
    initialized = False
    namesCollection = None
    classifier = None
    lang = 'en'
    modelFileFormat = 'models/model_{}.txt'

    significantDegree = 0.3
    
    surelyMale = 'M'
    surelyFemale = 'F'
    mostlyMale = '?m'
    mostlyFemale = '?f'
    genderUnknown = '?'
    

    @classmethod
    def init(cls, 
        lang='en',
        namesCollection=MemcacheNamesCollection,
        classifierClass=Classifier, 
        tokenizerClass=tokenizer):

        cls.lang = lang
        cls.namesCollection = namesCollection

        modelFileName = cls.modelFileFormat.format(cls.lang)
        with open(modelFileName, 'rb') as modelFile:
            model = cPickle.load(modelFile)
        
        cls.classifier = classifierClass(model, tokenizerClass)

        cls.initialized = True


    @classmethod
    def detect(cls, firstName=None, text=None, lang=None):
        
        if not cls.initialized:
            cls.init()

        if cls.classifier is None:
            raise Exception('No classifier found. You need to set a classifier.')

        if cls.namesCollection is None:
            raise Exception('No names collection found. You need to have names collection.')


        if firstName:
            nameGender = cls.namesCollection.getGender(firstName, lang)
            # if the first name surely is used for only one gender,
            # we can accept this gender.
            if nameGender:
                if nameGender['gender'] == cls.surelyMale:
                    return 'male'
                elif nameGender['gender'] == cls.surelyMale:
                    return 'female'
        else:
            nameGender = None


        # It is not for sure which gender the first name is being used in
        # we try to detect it looking his/her writing style.
        if text:
            probablities = dict(cls.classifier.classify(text))

            # @TODO: NEJDET, you have better explain what we do here.
            print probablities
            classifierScoreLogF = math.log(probablities['female']) / math.log(sum(probablities.values()))
            classifierScoreLogM = math.log(probablities['male']) / math.log(sum(probablities.values()))
            classifierScoreM = classifierScoreLogF / (classifierScoreLogM + classifierScoreLogF)
            classifierScoreF = classifierScoreLogM / (classifierScoreLogM + classifierScoreLogF)
            
            if nameGender and nameGender['gender'].startswith('?'):
                if nameGender['gender'] == cls.mostlyMale and classifierScoreM > 0.6:
                    return 'male'
                elif nameGender['gender'] == cls.mostlyFemale and classifierScoreF > 0.6:
                    return 'female'
                elif nameGender['gender'] != cls.genderUnknown:
                    return None
            
            # If there is no information according to the name and
            # there is significant difference between the two probablity,
            # we can accept the highest probablity.
            if abs(classifierScoreF - classifierScoreM) > cls.significantDegree:
                if probablities['female'] > probablities['male']:
                    return 'female'
                else:
                    return 'male'


found = Genderize.detect(
    firstName = 'mustafa',
    text='akp chp')

print found
