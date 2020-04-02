import numpy as np
import pandas as pd
import sys
import math
from collections import Counter

from pandas.io import sql

'''
input: user preference as txt file with features in order: 
language, 
service type, 
location
database: bank assistants as dict of dict of lists/int/string

'''
database = {'Rebecca White':{'language':['English','German','Spanish'], 'service':['card','transfer','check'], 'location':['US'], 'availability':1},\
                'Aysha Mathis':{'language':['French','Italian','Spanish'], 'service':['savings','loan','mortgage'], 'location':['UK'], 'availability':1}, \
                'Kimberley Petty':{'language':['Chinese','Japanese','Korean'], 'service':['loan','report','transfer'], 'location':['Australia'], 'availability':0}}

def sort_ranked_list(prefered_list):
    return(sorted(prefered_list, key = lambda x: x[1], reverse = True))

def counter_cosine_similarity(c1, c2):
    terms = set(c1).union(c2)
    dotprod = sum(c1.get(k, 0) * c2.get(k, 0) for k in terms)
    magA = math.sqrt(sum(c1.get(k, 0) ** 2 for k in terms))
    magB = math.sqrt(sum(c2.get(k, 0) ** 2 for k in terms))
    return dotprod / (magA * magB)
#!
def select_bank_assistant(name):
    database[name]['availability'] = 0
    return

def finished_assistant(name):
    database[name]['availability'] = 1

def matching_algorithm(threshold):
    # set up a threshold for banking assistants to get into the list
    matched = []
    for name in database:
        if not database[name]['availability']:
            continue
        else:
            counterA = set(language)
            counterB = set(database[name]['language'])
            #print(counterA.keys())
            #cos_sim_lang = counter_cosine_similarity(counterA, counterB)
            #print(counterB.keys())
            #print(counterA.keys())
            cos_sim_lang = len(counterA.intersection(counterB))/len(counterA)
            #print(cos_sim_lang)
            #cos_sim_lang = len(set(counterA.keys()).intersection(set(counterB.keys()))) / len(counterA.keys())
            #print(cos_sim_lang)
            counterA = set(service)
            counterB = set(database[name]['service'])
            #print(counterA)
            #print(counterB)
            #cos_sim_ser = len(set(counterA.keys()).intersection(set(counterB.keys())))/len(counterA.keys())
            cos_sim_ser =len(counterA.intersection(counterB))/len(counterA)
            #print(cos_sim_ser)
            #print(counterA.keys())

            #print(counterB.keys())
            #print(cos_sim_ser)
            #cos_sim_ser = counter_cosine_similarity(counterA, counterB)
            counterA = set(location)
            counterB = set(database[name]['location'])
            #cos_sim_loc = counter_cosine_similarity(counterA, counterB)
            cos_sim_loc =len(counterA.intersection(counterB))/len(counterA)
            #print(cos_sim_loc)
            score = 0.5 * cos_sim_lang + 0.4 * cos_sim_ser + 0.1 * cos_sim_loc
            if score > threshold:
                bank_assistant = name
                matched.append((bank_assistant,score))
                # best = score
                # database[name]['availability'] = 0
    return matched


if __name__ == '__main__':
    with open(sys.argv[1]) as fp:
        line = fp.readlines()
    language = [x.rstrip() for x in line[0].split(',')]
    service = [x.rstrip() for x in line[1].split(',')]
    location = [x.rstrip() for x in line[2].split(',')]
    #language = line[0].rstrip()
    #print(service)
    #language.type
    #service = line[1].rstrip()
    #location = line[2].rstrip()
    #joined = language + service + location


    threshold = 0.1
    matched = matching_algorithm(threshold)
    #print(matched)
    ranked = sort_ranked_list(matched)
    print(ranked)





