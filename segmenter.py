#!/usr/bin/python
# -*- coding: utf-8 -*-
from udicOpenData.dictionary import *
from udicOpenData.stopwords import *
#import jieba
import re

def segment(sentence, cut_all=False):
    #print(sentence)
    sentence = sentence.replace('\n', '').replace('\u3000', '').replace('\u00A0', '')
    #print(sentence)
    #sentence = ' '.join(jieba.cut(sentence, cut_all=cut_all))
    #i=input()
    sentence=list(rmsw(sentence,flag=False))
    #cutword=''
    #for i in sentence:
    #    cutword+=i
    #    cutword+=' '
    
    return sentence
    #return re.sub('[a-zA-Z0-9.。:：,，)）(（！!??”“\"]', '', sentence).split()
